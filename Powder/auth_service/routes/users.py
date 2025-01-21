from fastapi import APIRouter, HTTPException, status, Depends
from authentication.hash_password import HashPassword  # Import HashPassword utility for password handling
from authentication.jwt_handler import create_access_token  # Import function to create JWT tokens
from models.users import User, NewUser, TokenResponse  # Import User model and TokenResponse schema
from database.connection import get_session  # Import function to get database session
from sqlalchemy.ext.asyncio import AsyncSession  # Import AsyncSession for async database interaction
from sqlmodel import select  # Import select to query the database
from fastapi.security import OAuth2PasswordRequestForm  # Import OAuth2PasswordRequestForm for sign-in handling
from pydantic import BaseModel



# Define a custom request body form without grant_type
class CustomOAuth2PasswordRequestForm(BaseModel):
    username: str
    password: str
    # No grant_type field

# Create a new API router for user-related routes
user_router = APIRouter(tags=["User"])
hash_password = HashPassword()  # Initialize the HashPassword utility for password operations

@user_router.post("/api/register", status_code=status.HTTP_201_CREATED)
async def register(user: NewUser,
                   session: AsyncSession = Depends(get_session),
                   ) -> dict:
    """
    This endpoint is used for user registration. It accepts a `NewUser` object,
    checks if the email is already registered, hashes the password, and saves
    the user to the database.
    
    Args:
        user (NewUser): The user data (email and password) for registration.
        session (AsyncSession): The database session to interact with the database.
    
    Returns:
        dict: A success message if the user is registered.
    
    Raises:
        HTTPException: If the user with the same email already exists.
    """
    # Query the database to check if the email is already registered
    statement = select(User).where(User.email == user.email)
    result = await session.execute(statement)
    existing_user = result.scalars().first()

    # If the user already exists, raise a conflict error
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email already registered",
        )

    # Hash the user's password
    hashed_password = hash_password.create_hash(user.password)
    
    # Create a new user object
    new_user = User(email=user.email, password=hashed_password)

    # Add the new user to the session and commit the changes to the database
    session.add(new_user)
    await session.commit()
    await session.refresh(new_user)

    # Return a success message upon successful registration
    return {"message": "User successfully registered!"}


@user_router.post("/api/auth", status_code=status.HTTP_200_OK, response_model=TokenResponse)
async def token(user: OAuth2PasswordRequestForm = Depends(), session: AsyncSession = Depends(get_session)) -> dict:
    """
    This endpoint is used for user sign-in. It accepts the username (email) and password,
    verifies the user's existence, checks the password, and if valid, generates a JWT token.

    Args:
        user (OAuth2PasswordRequestForm): The username (email) and password for sign-in.
        session (AsyncSession): The database session to interact with the database.

    Returns:
        dict: A dictionary containing the access token and token type.
    
    Raises:
        HTTPException: If the user does not exist or the credentials are invalid.
    """
    # Query the database to find the user by email (username)
    statement = select(User).where(User.email == user.username)
    result = await session.execute(statement)
    existing_user = result.scalars().first()

    # If no user is found, raise an error
    if not existing_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User does not exist",
        )

    # Verify if the password is correct by comparing the hashed password
    if hash_password.verify_hash(user.password, existing_user.password):
        # If the password is correct, create a JWT token
        access_token = create_access_token({"email": existing_user.email})
        
        # Return the access token and token type
        return {
            "access_token": access_token,
            "token_type": "Bearer"
        }

    # If the password is incorrect, raise an authentication error
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid details passed."
    )

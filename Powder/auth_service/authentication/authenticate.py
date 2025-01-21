# Import necessary modules for handling JWT, FastAPI dependencies, and OAuth2 authentication
from auth.jwt_handler import verify_access_token
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

# OAuth2PasswordBearer is used to extract the token from the request header
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/user/signin")

# Function to authenticate users by verifying their JWT token
async def authenticate(token: str = Depends(oauth2_scheme)) -> str:
    """
    This function is used to authenticate the user by validating the provided token.
    If the token is missing or invalid, an HTTPException is raised.
    """
    if not token:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Sign in for access"
        )

    # Decode the token and return the email associated with it
    decoded_token = verify_access_token(token)
    return decoded_token["email"]
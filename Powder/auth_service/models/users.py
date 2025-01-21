from pydantic import BaseModel, ConfigDict, EmailStr
from sqlmodel import SQLModel, Field
from typing import Optional

# Define the User model that maps to a database table
class User(SQLModel, table=True):
    """
    This class defines the User model, which is used to represent a user in the system.
    It is mapped to a table in the database and includes fields like email, password, and events.
    """
    id: Optional[int] = Field(default=None, primary_key=True)  # Optional primary key for auto-increment
    email: str = Field(index=True, unique=True)  # Email field, unique and indexed for fast lookups
    password: str  # User's hashed password

    model_config = ConfigDict(
        json_schema_extra={  # Provide an example for automatic documentation generation (e.g., OpenAPI schema)
            "example": {
                "email": "example@example.com",
                "password": "it is private",
            }
        },
    )


# Define the UserSignIn model, which is used for user authentication during sign-in
class UserSignIn(BaseModel):
    """
    This class defines the data structure for user sign-in, including email and password.
    It is used when a user attempts to sign in to the application.
    """
    email: EmailStr  # Email field with validation provided by EmailStr
    password: str  # Plain-text password

    model_config = ConfigDict(
        json_schema_extra={  # Example for sign-in request payload for automatic documentation generation
            "example": {
                "email": "example@example.com",
                "password": "it is private"
            }
        },
    )


# Define the NewUser model, which is used to create a new user. It inherits from UserSignIn.
class NewUser(UserSignIn):
    """
    This class defines the structure for creating a new user, inheriting from UserSignIn.
    It doesn't add any new fields but can be extended if needed in the future.
    """
    pass


# Define the TokenResponse model, which represents the response after a successful authentication.
class TokenResponse(BaseModel):
    """
    This class defines the structure of the response returned after generating a JWT token.
    It includes the access token and the token type.
    """
    access_token: str  # The access token to authenticate requests
    token_type: str  # The type of the token, typically "bearer"

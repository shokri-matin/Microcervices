import os

from datetime import datetime, timezone
from jose import jwt, JWTError
from fastapi import HTTPException, status

# Secret key and algorithm for JWT token signing and encoding
SECRET_KEY = os.getenv("SECRET_KEY", "")
ALGORITHM = "HS256"

def verify_access_token(token: str) -> dict:
    """
    Decodes the provided JWT token, checks for expiration, and returns the payload.
    
    Args:
        token (str): The JWT token to decode.
        
    Returns:
        dict: The decoded payload if the token is valid.
    
    Raises:
        HTTPException: If the token is invalid or expired.
    """
    try:
        # Decode the token using the secret key and algorithm
        data = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        # Check if the "exp" claim (expiration time) is present in the token
        expire = data.get("exp")
        if expire is None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Access token is missing an expiration claim"
            )

        # Validate the token's expiration
        if datetime.now(timezone.utc).timestamp() > expire:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Token has expired"
            )

        return data

    except JWTError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Invalid token: {str(e)}"
        )

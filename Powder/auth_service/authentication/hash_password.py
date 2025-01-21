# Import passlib's CryptContext for handling password hashing and verification
from passlib.context import CryptContext

# Initialize the password hashing context with bcrypt
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class HashPassword:
    """
    This class contains methods to create and verify hashed passwords using bcrypt.
    """

    def create_hash(self, password: str):
        """
        Hashes the password using bcrypt.
        
        Args:
            password (str): The plain-text password to be hashed.
        
        Returns:
            str: The hashed password.
        """
        return pwd_context.hash(password)

    def verify_hash(self, plain_password: str, hashed_password: str):
        """
        Verifies if the plain password matches the hashed password.
        
        Args:
            plain_password (str): The plain-text password to verify.
            hashed_password (str): The hashed password stored in the database.
        
        Returns:
            bool: True if the passwords match, False otherwise.
        """
        return pwd_context.verify(plain_password, hashed_password)

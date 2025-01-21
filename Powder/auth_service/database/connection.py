from sqlmodel import SQLModel
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from models.users import User
import aiosqlite
import os

# Define the database file and connection string
database_file = "user.db"  # The file where the SQLite database will be stored
database_connection_string = os.getenv("DATABASE_URL", "sqlite+aiosqlite:///{database_file}") # Connection string for SQLite using aiosqlite

# Create the async engine for database interactions
connect_args = {"check_same_thread": False}  # Allows safe multi-threaded access to SQLite
engine_url = create_async_engine(
    database_connection_string,
    echo=True,  # Logs SQL statements for debugging purposes
    connect_args=connect_args
)

# Async sessionmaker for creating async database sessions
async_session = sessionmaker(
    engine_url,
    class_=AsyncSession,  # Use AsyncSession for asynchronous operations
    expire_on_commit=False  # Prevents session-expired errors when accessing committed objects
)

# Enable Write-Ahead Logging (WAL) mode for better concurrency and performance
async def enable_wal():
    async with aiosqlite.connect("user.db") as db:
        await db.execute("PRAGMA journal_mode=WAL;")  # Enable WAL mode
        await db.execute("PRAGMA synchronous=NORMAL;")  # Optional: Improve performance by reducing sync overhead
        await db.commit()  # Commit changes to the database

# Initialize the database schema by creating tables and enabling WAL mode
async def conn():
    # Check if the database file exists in the mounted volume
    if not os.path.exists(database_file):
        print(f"Database file not found, creating schema at {database_file}...")
        async with engine_url.begin() as conn:
            await conn.run_sync(SQLModel.metadata.create_all)  # Create all tables defined in SQLModel
        await enable_wal()  # Enable WAL mode for the database
    else:
        print(f"Database file {database_file} already exists, skipping creation.")

# Dependency to get an async session for database operations
async def get_session():
    async with async_session() as session:
        yield session  # Yield the session for use in async database operations

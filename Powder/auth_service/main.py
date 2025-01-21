from routes.users import user_router
from database.connection import conn
from contextlib import asynccontextmanager 
from fastapi.middleware.cors import CORSMiddleware 
from fastapi import FastAPI

# Define the lifespan context manager for the FastAPI app
@asynccontextmanager
async def lifespan(app: FastAPI):
    # This function handles the lifecycle of the app (startup and shutdown)
    print("Initializing Server")  # Print when server starts
    # Initialize the database schema asynchronously
    await conn()
    yield  # Allow the application to run
    print("Preparing to Shutdown Server")  # Print when server is shutting down

# Create the FastAPI app with the lifespan context manager
app = FastAPI(lifespan=lifespan, root_path="/user")

# Register routes to the app (user and event routes)
# The user-related routes are prefixed with '/user'
app.include_router(user_router)

# Configure CORS middleware to handle cross-origin requests
origins = ["*"]  # Allow all origins (for testing or public APIs)

# Add CORS middleware with the specified configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allow all origins
    allow_credentials=True,  # Allow credentials (cookies, authentication)
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)
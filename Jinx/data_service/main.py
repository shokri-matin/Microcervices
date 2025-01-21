from fastapi import FastAPI
from routes import router

app = FastAPI(root_path="/data")

# Include routes
app.include_router(router)
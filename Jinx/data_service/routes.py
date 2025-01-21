import os

from fastapi import APIRouter, Depends, Request
from tasks import log_task
from db import get_data_from_db
from verification import verify_access_token

SERVICE_NAME = os.getenv("SERVICE_NAME", "unknown_service")

async def generate_log(user, request, log_message: str, log_level: str = "INFO"):
    
    """Send log message with metadata."""
    client_ip = request.client.host
    user_id = user["email"]  # Example custom header
    metadata = {
        "log_message": log_message,
        "service_name": SERVICE_NAME,
        "log_level": log_level,
        "client_ip": client_ip,
        "user_id": user_id,
    }
    log_task.delay(metadata)

router = APIRouter()

@router.get("/fetch")
async def search_data(
    request: Request,
    start_date: str,
    end_date: str,
    category: str,
    isdn: str,
    user: str = Depends(verify_access_token),
):
    try:

        # Log the start of the operation
        log_message = f"Searching data for ISDN: {isdn}, category: {category}, from {start_date} to {end_date}."
        log_level = "INFO"
        await generate_log(user, request, log_message, log_level)

        # Submit task to Celery
        data = get_data_from_db(start_date, end_date, category, isdn)

        # Log task completion
        log_message = f"Data fetched completely for ISDN: {isdn}, category: {category}, from {start_date} to {end_date}. fetched {len(data)} records."
        await generate_log(user, request, log_message, log_level)

        return {
            "result": data
        }

    except ValueError as ve:
        # Handle invalid date formats
        log_message = f"ValueError occurred: {ve} for ISDN: {isdn}, category: {category}, from {start_date} to {end_date}."
        log_level = "ERROR"
        await generate_log(user, request, log_message, log_level)
        return {"error": f"Invalid date format: {ve}"}, 400


    except Exception as ex:
        # Catch-all for unexpected errors
        log_message = f"An unexpected error occurred: {ex} for ISDN: {isdn}, category: {category}, from {start_date} to {end_date}."
        log_level = "CRITICAL"
        await generate_log(user, request, log_message, log_level)
        return {"error": f"An unexpected error occurred: {ex}"}, 500

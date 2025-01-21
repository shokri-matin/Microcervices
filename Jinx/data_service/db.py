
from datetime import datetime

def get_data_from_db(start_date, end_date, category, isdn):

# Sample data added by the cache service
    data = [
        {"isdn": "1", "date": "2025-01-01", "category": "A", "data": "Extra info 1"},
        {"isdn": "1", "date": "2025-01-01", "category": "A", "data": "Extra info 2"},
        {"isdn": "1", "date": "2025-01-01", "category": "A", "data": "Extra info 3"},
        {"isdn": "1", "date": "2025-01-01", "category": "A", "data": "Extra info 4"},
        {"isdn": "1", "date": "2025-01-01", "category": "A", "data": "Extra info 5"},
        {"isdn": "1", "date": "2025-01-01", "category": "A", "data": "Extra info 6"},
        {"isdn": "1", "date": "2025-01-01", "category": "A", "data": "Extra info 7"},
        {"isdn": "1", "date": "2025-01-01", "category": "A", "data": "Extra info 8"},
        {"isdn": "1", "date": "2025-01-01", "category": "A", "data": "Extra info 9"},
        {"isdn": "1", "date": "2025-01-01", "category": "A", "data": "Extra info 10"},
        {"isdn": "1", "date": "2025-01-01", "category": "A", "data": "Extra info 11"},
        {"isdn": "1", "date": "2025-01-01", "category": "A", "data": "Extra info 12"},
        {"isdn": "1", "date": "2025-01-01", "category": "A", "data": "Extra info 13"},
        {"isdn": "1", "date": "2025-01-01", "category": "A", "data": "Extra info 14"},
        {"isdn": "1", "date": "2025-01-01", "category": "A", "data": "Extra info 15"},
        {"isdn": "1", "date": "2025-01-01", "category": "A", "data": "Extra info 16"},
        {"isdn": "2", "date": "2025-01-02", "category": "B", "data": "Extra info 17"},
        {"isdn": "3", "date": "2025-01-03", "category": "A", "data": "Extra info 18"},
        {"isdn": "1", "date": "2025-01-04", "category": "A", "data": "Extra info 19"}
    ]

    # Convert date strings to datetime objects for comparison
    start_date_obj = datetime.strptime(start_date, "%Y-%m-%d")
    end_date_obj = datetime.strptime(end_date, "%Y-%m-%d")

    # Filter data
    filtered_data = [
        record for record in data
        if (
            start_date_obj <= datetime.strptime(record["date"], "%Y-%m-%d") <= end_date_obj
            and record["isdn"] == isdn
            and record["category"] == category
        )
    ]

    return filtered_data
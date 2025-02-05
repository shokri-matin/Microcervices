from datetime import datetime
from deltalake import DeltaTable
import pandas as pd

DATA_PATH = os.getenv("DATA_PATH", "unknown_service")

def get_data_from_db(start_date, end_date, category, isdn):
    
    # Load the Delta table
    delta_table = DeltaTable(DATA_PATH)
        
    # Query the Delta table
    df = delta_table.to_pandas().query(f"isdn == '{isdn}'")

    # Convert the DataFrame to JSON
    result_json = df.to_dict(orient="records")  # Convert each row to a dictionary
    
    return result_json

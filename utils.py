import logging
import sqlite3
from pathlib import Path

# Setup logging
def get_logger(name="Vehicle_Pipeline"):
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(time)s - %(levelname)s - %(message)s"
    )
    return logging.getLogger(name)

# Database connection
def get_db_connection(db_path="data/vehicles.db"):
    Path("data").mkdir(exist_ok=True)
    conn = sqlite3.connect(db_path)
    return conn
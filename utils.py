import logging
import sqlite3
from pathlib import path

# Setup logging
def get_logger(name="Vehicle_Pipeline"):
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(time)s - %(levelname)s - %(message)s"
    )
    return logging.getLogger(name)

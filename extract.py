import pandas as pd
from utils import get_logger

logger = get_logger("Extract")

def extract_data(file_path="data/vehicles_dataset.csv"):
    try:
        df = pd.read_csv(file_path)
        logger.info(f"Extracted {df.shape[0]} rows and {df.shape[1]} columns")
        return df
    except Exception as e:
        logger.error(f"Error in Extraction : {e}")
        raise
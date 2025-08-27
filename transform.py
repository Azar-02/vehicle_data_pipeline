import pandas as pd
from datetime import datetime
from utils import get_logger

logger = get_logger("Transform")

def transform_data(df:pd.DataFrame):
    try:
        # Drop duplicates
        df = df.drop_duplicates()

        # Handle missing values
        df['price'] = df['price'].fillna(df['price'].median())
        df['mileage'] = df['mileage'].fillna(df['mileage'].median())
        df['fuel'] = df['fuel'].fillna('unknown')

        # Normalize categorical values
        df['fuel'] = df['fuel'].str.lower().str.strip()
        df['transmission'] = df['transmission'].str.lower().str.strip()
        
        # Feature engineering - car age
        current_year = datetime.now().year
        df['car_age'] = current_year - df['year']
        
        logger.info(f"Transformed dataset : {df.shape[0]} rows")
        return df
    except Exception as e:
        logger.error(f"Error in Transformation : {e}")
        raise
    
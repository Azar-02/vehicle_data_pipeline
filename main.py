from extract import extract_data
from transform import transform_data
from load import load_data
from utils import get_logger

logger = get_logger("Main")

def run_pipeline():
    logger.info("Starting Vehicle Data ETL Pipeline")

    #Extract Data
    df = extract_data()

    #Transform Data
    df_clean = transform_data(df)

    #Load Data
    load_data(df_clean)

    logger.info("ETL Pipeline Successfully Completed")

if __name__ == "__main__":
    run_pipeline()
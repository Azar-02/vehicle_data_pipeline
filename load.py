from utils import get_logger, get_db_connection

logger = get_logger("Load")

def load_data(df, table_name="vehicles"):
    try:
        conn = get_db_connection()
        df.to_sql(table_name,conn, if_exists="replace", index=False)
        conn.close()
        logger.info(f"Loaded {df.shape[0]} records into '{table_name}' table")
    except Exception as e :
        logger.error(f"Error in load : {e}")
        raise
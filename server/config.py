import os 
from dotenv import load_dotenv
import psycopg2

load_dotenv()




# Database connection
def connectDB():
    try:
        # Get the database URL from the environment variables
        url = os.getenv('DATABASE_URL')
        if not url:
            raise ValueError("DATABASE_URL is not set in the environment variables")

        # Establish a connection to the PostgresSQL database
        conn = psycopg2.connect(url)

        query_sql = "SELECT VERSION();"

        cur = conn.cursor()
        cur.execute(query_sql)

        version = cur.fetchone()[0]
        print(f"Connected to: {version}")
        return conn
    except Exception as e:
        print(f"Error connecting to the database : {e}")
        return None






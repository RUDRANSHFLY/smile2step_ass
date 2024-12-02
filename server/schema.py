from config import connectDB


def create_user_table():
    conn = connectDB()

    if conn is None:
        return
    
    try:
        cursor = conn.cursor()
        create_table_query = '''
        CREATE TABLE IF NOT EXISTS users(
            id SERIAL PRIMARY KEY,
            username VARCHAR(50) NOT NULL,
            email VARCHAR(50) NOT NULL UNIQUE,
            dob DATE NOT NULL
        );
        '''
        cursor.execute(create_table_query)  
        conn.commit()
        cursor.close()
        print("User table created successfully")
    except Exception as e:
        print(f"Error creating user table: {e}")
    finally:
        conn.close()      

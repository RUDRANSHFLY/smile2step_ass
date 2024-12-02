# from config import connectDB

# def modify_user_table():
#     conn = connectDB()

#     if conn is None:
#         return
    
#     try:
#         cursor = conn.cursor()
        
#         # Remove the password column if it exists
#         remove_password_column_query = '''
#         ALTER TABLE users
#         DROP COLUMN IF EXISTS password;
#         '''
#         cursor.execute(remove_password_column_query)
        
#         # Add the dob column if it does not exist
#         add_dob_column_query = '''
#         ALTER TABLE users
#         ADD COLUMN IF NOT EXISTS dob DATE NOT NULL;
#         '''
#         cursor.execute(add_dob_column_query)
        
#         conn.commit()
#         cursor.close()
#         print("User table modified successfully")
#     except Exception as e:
#         print(f"Error modifying user table: {e}")
#     finally:
#         conn.close()

# # Call the function to modify the table
# modify_user_table()
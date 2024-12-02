from flask import Flask , jsonify
from schema import create_user_table
from config import connectDB
from flask import request

app = Flask(__name__)


create_user_table()




# Get all the users
@app.route("/users",methods=["GET"])
def get_users():
    conn = connectDB()

    if conn is None:
        return jsonify({"error" : "Database connection failed"}), 500
    
    try:

        cur = conn.cursor()
        cur.execute("SELECT * FROM users")
        users = cur.fetchall()
        conn.close()
        return jsonify({"users" : users}), 200
    
    except Exception as e:
        return jsonify({"error" : str(e)}), 500
    


# Add a new user
@app.route("/user",methods=["POST"])
def add_user():
    conn = connectDB()

    if conn is None:
        return jsonify({"error" : "Database connection failed"}), 500
    
    try:
        data = request.get_json()
        username = data.get("username")
        email = data.get("email")
        dob = data.get("dob")

        if not username or not email or not dob:
            return jsonify({"error" : "Invalid data"}), 400
        
        cur = conn.cursor()

        user_exist_query = "SELECT * FROM users WHERE email = %s"
        cur.execute(user_exist_query,(email,))
        existing_user = cur.fetchone()

        if existing_user:
            return jsonify({"error" : "User already exists"}), 400
        
        new_user_query = "INSERT INTO users(username,email,dob) VALUES(%s,%s,%s)"
        cur.execute(new_user_query,(username,email,dob))
        conn.commit()
        conn.close()
        return jsonify({"message" : "User added successfully"}), 201
    
    except Exception as e:
        return jsonify({"error" : str(e)}), 500


# Update a user
@app.route("/users/<int:id>",methods=["PUT"])
def update_user(id):

    conn = connectDB()

    if conn is None:
        return jsonify({"error" : "Database connection failed"}), 500
    
    try:
        data = request.get_json()
        username = data.get("username")
        email = data.get("email")
        dob = data.get("dob")
       

        if email:
            return jsonify({"error" : "Email cannot be updated"}), 400

        if not username and not dob:
            return jsonify({"error" : "No fields to update"}), 400
        
        user_exist_query = "SELECT * FROM users WHERE id = %s"

        cur = conn.cursor()
        cur.execute(user_exist_query,(id,))

        if not cur.fetchone():
            return jsonify({"error" : "User does not exist"}), 400
        
        update_fields = []
        update_values = []

        if username:
            update_fields.append("username = %s")
            update_values.append(username)
        
        if dob:
            update_fields.append("dob = %s")
            update_values.append(dob)
        
        update_values.append(id)
        update_query = "UPDATE users SET " + " , ".join(update_fields) + " WHERE id = %s"
        cur.execute(update_query,tuple(update_values))
        conn.commit()
        conn.close()
        return jsonify({"message" : "User updated successfully"}), 200
    
    except Exception as e:
        return jsonify({"error" : str(e)}), 500






if(__name__ == "__main__"):
    app.run(debug=True)
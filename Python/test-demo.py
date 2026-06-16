# Create a Python Flask login API using SQLite with security best practices.

# Requirements:
# - Create a POST endpoint /login
# - Accept username and password from JSON body
# - Query the users table to verify credentials
# - Return "Login successful" if user exists, otherwise return "Invalid credentials"

# Security improvements:
# - Use parameterized queries to prevent SQL injection
# - Hash passwords using bcrypt
# - Add input validation
# - Use secure session management

from flask import Flask, request, jsonify
import sqlite3
import bcrypt
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

# Initialize the SQLite database and create users table
def init_db():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    ''')
    # Insert a sample user for testing with hashed password
    hashed_password = generate_password_hash('testpass')
    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", ('testuser', hashed_password))
        conn.commit()
    except sqlite3.IntegrityError:
        pass
    conn.close()

@app.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"message": "Invalid request"}), 400
        
        username = data.get('username', '').strip()
        password = data.get('password', '')
        
        # Input validation
        if not username or not password:
            return jsonify({"message": "Invalid credentials"}), 401
        
        if len(username) > 255 or len(password) > 255:
            return jsonify({"message": "Invalid credentials"}), 401
        
        # Use parameterized query to prevent SQL injection
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        user = cursor.fetchone()
        conn.close()
        
        # Verify password using secure hash comparison
        if user and check_password_hash(user[2], password):
            return jsonify({"message": "Login successful"}), 200
        else:
            return jsonify({"message": "Invalid credentials"}), 401
    
    except Exception as e:
        return jsonify({"message": "Server error"}), 500

if __name__ == '__main__':
    init_db()
    app.run(debug=False)

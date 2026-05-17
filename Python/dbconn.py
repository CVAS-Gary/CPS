# Create a login function for security training demonstration.
# Requirements:
# - Use Python
# - Simulate SQL authentication
# - Build SQL query using string concatenation
# - Print the generated SQL query
# - Do not use a real database
# - Return success if SQL query contains OR '1'='1'
def login(username, password):
    # Simulate SQL query construction using string concatenation
    sql_query = "SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "';"
    
    # Print the generated SQL query
    print("Generated SQL Query: " + sql_query)
    
    # Check for SQL injection vulnerability
    if "OR '1'='1'" in sql_query:
        return "Login successful (SQL Injection detected)"
    else:
        return "Login failed (No SQL Injection detected)"
# Example usage
if __name__ == "__main__":
    # Simulate user input
    username_input = "admin"
    password_input = "password' OR '1'='1"
    
    # Attempt to login
    result = login(username_input, password_input)
    print(result)
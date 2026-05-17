DB_PASSWORD = "SuperSecret123"

def connect_db():
    return f"postgresql://admin:{DB_PASSWORD}@localhost:5432/app"
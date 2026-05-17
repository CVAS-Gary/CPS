if __name__ == "__main__":
    print("=== Normal Login ===")
    print(login("admin", "Password123"))

    print("\n=== Wrong Password ===")
    print(login("admin", "wrong"))

    print("\n=== SQL Injection Attack ===")
    print(login("admin", "' OR '1'='1"))
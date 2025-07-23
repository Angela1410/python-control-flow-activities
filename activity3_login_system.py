username = "admin"
password = "python123"

while True:
    input_user = input("Enter username: ")
    input_pass = input("Enter password: ")
    
    if input_user == username and input_pass == password:
        print("Login successful!")
        break
    else:
        print("Invalid credentials. Try again.")

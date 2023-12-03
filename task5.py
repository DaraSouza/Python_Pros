password = "python123"
while True:
    user_input = input("Enter the password: ")
    if user_input == password:
        print("Yay! You guessed the password")
        break
else:
    print("Are you breaking in?! I'm watching you!")
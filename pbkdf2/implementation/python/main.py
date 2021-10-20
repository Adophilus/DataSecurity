from systems.registration import RegistrationSystem

hostelRecords = RegistrationSystem()

hostelRecords.initiate()


def mainMenu():
    IS_LOGGED_IN = False

    def getUsernameAndPassword():
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        return username, password

    def registerUser():
        print()
        user = hostelRecords.registerUser(*getUsernameAndPassword())
        print("Registration successful!")

    def loginUser():
        print()
        login = hostelRecords.loginUser(*getUsernameAndPassword())
        if (login):
            IS_LOGGED_IN = True
            print("Login successful!")
            return True
        print("Incorrect credentials!")

    def removeUser():
        print()
        if not (IS_LOGGED_IN):
            print("You must be logged in first!")

    operations = [
        ["Register", registerUser],
        ["Login", loginUser],
        ["Checkout", removeUser],
        ["Exit", exit],
    ]

    userInput = 0

    while not (userInput in range(1, len(operations) + 1)):
        print()
        print("Welcome To Hostel Registration System")

        for i in range(len(operations)):
            print(f"{i+1}) {operations[i][0]}")

        userInput = int(input("What would you like to do? "))

    operations[userInput - 1][1]()


def main():
    while True:
        mainMenu()


if __name__ == "__main__":
    main()

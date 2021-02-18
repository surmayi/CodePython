class User:
    def __init__(self, userName=None, password=None):
        # public variables are created, anyone can access
        self.userName = userName
        self.password = password

    def login(self, userName, password):
        if ((self.userName.lower() == userName.lower())
                and (self.password == password)):
            print("Access Granted!")
        else:
            print("Invalid Credentials!")


Steve = User("Steve", "12345")
Steve.login("steve", "12345")
Steve.login("steve", "6789")
#anyone can access, change, or print the password and userName fields directly from the main code
Steve.password = "6789"
Steve.login("steve", "6789")
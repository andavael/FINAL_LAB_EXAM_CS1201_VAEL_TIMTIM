class User:
    def __init__(self, username, password, points):
        self.username = username
        self.password = password
        self.points = points

    def register(self):
        print("REGISTER USER")
        user = {}
        username = input("Please enter a username or leave blank to exit: ")
        while True:
            try:
                if not username:
                    exit()
                if len(username) < 4:
                    print("Username must at least be four characters. Please enter a new one.")
                    return
                if username in user:
                    print("Username must at least be four characters. Please enter a new one.")
                else: 
                    password = input("Please enter a password or leave blank to exit: ")
                    if not password:
                        exit()
                    if len(password) < 8:
                        print("Password must be at least eight characters. Please enter a new one.")
                        return
            except ValueError as e:
                print (e) 
        
            
            
        
        
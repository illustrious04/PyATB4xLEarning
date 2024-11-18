
class App_login():
    def __init__(self, email_arg, password_arg):
        self.email = email_arg
        self.password = password_arg


    def login_confirm(self):
        if self.email == "abdsuyash@gmail.com" and self.password == "1234":
            print("Login Successfully !")
        else:
            print("Invalid Details")

# Taking user inputs
email = input("Enter your email\n")
password = input("Enter your password\n")

# Creating Object
app1 = App_login(email, password)
app1.login_confirm()

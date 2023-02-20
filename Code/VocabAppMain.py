from kivymd.app import MDApp

#Login App

from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from secure_password import hash_password
from db_manager import database_handler
class LoginScreen(MDScreen):
    def login(self):
        print(f"Username: {self.ids.uname.text} Password: {self.ids.pwd.text}")
        username = self.ids.uname.text
        password = self.ids.pwd.text
        if  VocabApp.db.login_check(username, password) == True:
            print("Login success")
        else:
            print("Login failed")
class RegisterScreen(MDScreen):
    def register(self):
        print(f"Username: {self.ids.uname.text} Email:{self.ids.email.text} Password: {self.ids.pwd.text}")
        uname  = self.ids.uname.text
        email = self.ids.email.text
        pwd = self.ids.pwd.text
        cpwd = self.ids.cpwd.text
        if pwd != cpwd:
            print("Passwords do not match")
            self.ids.cpwd.error = True
            self.ids.cpwd.md_bg_color = "red"
        else:
            pwd = hash_password(pwd)
            self.ids.cpwd.error = False
            self.ids.cpwd.md_bg_color = "green"
            db = database_handler("vocab_app.db")
            db.insert_user(email, uname, pwd)
            db.close()
            self.parent.current = "LoginScreen"


class VocabApp(MDApp):
    db = database_handler("vocab_app.db")
    def build(self):
        return

boi = VocabApp()
boi.run()
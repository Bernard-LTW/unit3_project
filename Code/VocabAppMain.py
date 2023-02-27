#VocabAppMain.py
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from secure_password import hash_password
from db_manager import database_handler
from models import Users, Vocabulary, UserStats

global current_user
current_user = None
class LoginScreen(MDScreen):
    def login(self):
        print(f"Username: {self.ids.uname.text} Password: {self.ids.pwd.text}")
        username = self.ids.uname.text
        password = self.ids.pwd.text
        if VocabApp.db.login_check(username, password):
            print("Login success")
            self.parent.current = "LandingScreen"
            global current_user
            current_user = VocabApp.db.session.query(Users).filter_by(username=username).first()
            print(f"Current user: {current_user.username}")
            self.ids.uname.text = ""
            self.ids.pwd.text = ""
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


class LandingScreen(MDScreen):
    def on_enter(self):
        global current_user
        self.ids.welcome_banner.text = f"Welcome {current_user.username}"
    def logout(self):
        self.parent.current = "LoginScreen"
        current_user = None
    def add_vocab(self):
        self.parent.current = "AddVocabScreen"

class ManageVocabScreen(MDScreen):
    def add_vocab(self):
        pass

    def edit_vocab(self):
        pass

    def delete_vocab(self):
        pass



class RandomVocabScreen(MDScreen):
    def random_vocab(self):
        pass

class VocabChooserScreen(MDScreen):

    def choose_vocab(self):
        pass

class VocabCardScreen(MDScreen):
    def show_vocab(self):
        pass

    def add_points(self):
        pass

    def remove_points(self):
        pass
class VocabApp(MDApp):
    db = database_handler("vocab_app.db")
    def build(self):
        return

boi = VocabApp()
boi.run()
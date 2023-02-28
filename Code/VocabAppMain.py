#VocabAppMain.py
from kivymd.app import MDApp
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.screen import MDScreen
from secure_password import hash_password
from db_manager import database_handler
from models import Users, Vocabulary, UserStats
from kivy.logger import Logger

global current_user
current_user = None

class LoginScreen(MDScreen):
    def login(self):
        print(f"Username: {self.ids.uname.text} Password: {self.ids.pwd.text}")
        username = self.ids.uname.text
        password = self.ids.pwd.text
        if VocabApp.db.login_check(username, password):
            Logger.info("Login successful")
            self.parent.current = "LandingScreen"
            global current_user
            current_user = VocabApp.db.session.query(Users).filter_by(username=username).first()
            Logger.info(f"Current user: {current_user.username}")
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
        self.ids.welcome_banner.text = f"こんにちは {current_user.username}"
    def logout(self):
        self.parent.current = "LoginScreen"
        current_user = None
    def add_vocab(self):
        self.parent.current = "AddVocabScreen"

class ManageVocabScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        font_name = "Roboto"
        self.data_table = MDDataTable(
            size_hint=(0.9, 0.5),
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            use_pagination=True,
            check=True,
            column_data=[
                ("ID", 50),
                ("Lesson", 40),
                ("Part", 40),
                ("Hiragana", 40, font_name),
                ("Katakana", 40),
                ("Definition", 40)
            ],
            row_data=[]
        )
        self.data_table.bind(on_row_press=self.on_row_press)
        self.data_table.bind(on_check_press=self.on_check_press)
        self.add_widget(self.data_table)

    def on_pre_enter(self, *args):
        self.load()

    def on_row_press(self, table, row):
        print(f"Row was pressed. Data is: {row.text}")

    def on_check_press(self, table, current_row):
        print(f"Row {current_row} was checked")

    def load(self):
        print("Trying to load all Tx...")
        self.data_table.row_data.clear()
        rows = VocabApp.db.get_vocab()
        print(self.data_table.row_data)
        for row in rows:
            print(row)
            print(row.id)
            row.hiragana = f"[font=Japanese.ttc]{row.hiragana}[/font]"
            row.katakana = f"[font=Japanese.ttc]{row.katakana}[/font]"
            row = [str(row.id), str(row.lesson), str(row.part_of_lesson), row.hiragana, row.katakana, row.definition]
            print(row)
            if row not in self.data_table.row_data:
                self.data_table.row_data.append(row)



class PerVocabManageScreen(MDScreen):
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
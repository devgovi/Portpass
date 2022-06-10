# Govine-J
# GITS
# 2022-06-09
# Call only when the application is started for the first time.
# To determine if the application is started for the first time,
# We check if the file following file exists:
# - MASTER_PASS_FILE, - MASTER_KEY_FILE, - DB_PATH
import tkinter
import customtkinter
from cryptoManager import create_key
from app_config import APP_ICON
from setupMasterPass import takeMasterPass
from connectDB import portpass_db_con as con
from initTable import init_table

customtkinter.set_default_color_theme("green")
class SetupScreen(customtkinter.CTk):
    """
    The home screen of the application.
    NOTE:
    This screen will show only if the following files do not exist:
    - MASTER_PASS_FILE, - MASTER_KEY_FILE, - DB_PATH.
    
    The user will be prompted to create a master password and then the application will create the files mention above.
    """
    def __init__(self):
        super().__init__()
        self.title("Create Master Password")
        self.geometry("300x400")
        self.iconbitmap(APP_ICON)
        self.resizable(False, False)
        init_table(con())
        create_key()
        self.create_widgets()
    
    def create_widgets(self):
        """
        Create the widgets for the home screen.
        """
        # Create a label for the master password setup.-START
        label = customtkinter.CTkLabel(text='''LET'S CREATE A\nMASTER PASSWORD\nTO GET STARTED''', width=120, height=25, corner_radius=8)
        entry1 = customtkinter.CTkEntry(width=140, height=25, placeholder_text="Master password", show="*", corner_radius=8)
        entry2 = customtkinter.CTkEntry(width=140, height=25, placeholder_text="Re-Enter Master pass...", show="*", corner_radius=8)
        error_msg = customtkinter.CTkLabel(text="", width=120, height=25, corner_radius=8, text_color="red")
        btn = customtkinter.CTkButton(text="CREATE", width=40,height=35, corner_radius=8)
        # Create a label for the master password setup.-END
        
        # Place the label in the center of the screen.-START
        label.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)
        entry1.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)
        entry2.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        error_msg.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)
        btn.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)
        # Place the label in the center of the screen.-END
        
        # Create the function to validate the entries. -START
        def create_master_pass()->None:
            """ Create the master password. """
            _entry1 = entry1.get()
            _entry2 = entry2.get()
            
            if _entry1 != '' or _entry2 != '':
                if _entry1 == _entry2:
                    if takeMasterPass(_entry1) is True:
                        error_msg.config(text="Master password created successfully.", text_color="green")
                        self.destroy()
                    else:
                        error_msg.config(text="Must be at least 8 characters long.\nPlease try again.")
                else:
                    error_msg.config(text="Passwords do not match.\nPlease try again.")
            else:
                error_msg.config(text="All fields are required.", text_color="red")
        # Create the function to validate the entries. -END
        
        btn.config(command=create_master_pass)
        
        
        
        
# SetupScreen().mainloop()
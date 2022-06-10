# Govine-J
# GITS
# 2022-06-09
# Call only when the application is started for the first time.
# To determine if the application is started for the first time,
# We check if the file following file exists:
# - MASTER_PASS_FILE, - MASTER_KEY_FILE, - DB_PATH
import tkinter
import customtkinter
from app_config import (APP_ICON, VISIBILITY_ON, VISIBILITY_OFF,)
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
        self.create_widgets()
    
    def create_widgets(self):
        """
        Create the widgets for the home screen.
        """
        # Create a label for the master password setup.-START
        label = customtkinter.CTkLabel(text='''LET'S CREATE A\nMASTER PASSWORD\nTO GET STARTED''', width=120, height=25, corner_radius=8)
        entry1 = customtkinter.CTkEntry(width=140, height=25, placeholder_text="Master password", show="*", corner_radius=8)
        
        # Setting a image for button.-START
        eye_on = tkinter.PhotoImage(file=VISIBILITY_ON)
        eye_off = tkinter.PhotoImage(file=VISIBILITY_OFF)
        eye_btn = customtkinter.CTkButton(text="", width=16, height=16, image=eye_off, fg_color=None, bg_color=None)
        
        
        entry2 = customtkinter.CTkEntry(width=140, height=25, placeholder_text="Re-Enter Master pass...", show="*", corner_radius=8)
        error_msg = customtkinter.CTkLabel(text="", width=120, height=25, corner_radius=8, text_color="red")
        btn = customtkinter.CTkButton(text="CREATE", width=40,height=35, corner_radius=8)
        # Create a label for the master password setup.-END
        
        # Place the label in the center of the screen.-START
        label.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)
        entry1.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)
        
        eye_btn.pack(anchor=tkinter.NE, pady=150, padx=40)
        
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
                if _entry1 == ' ' or _entry2 == ' ':
                    error_msg.config(text="Please enter a valid password.")
                    self.after(2000, clear_error_msg)
                elif _entry1 == _entry2:
                    if takeMasterPass(_entry1) is True:
                        error_msg.config(text="Master password created successfully.", text_color="green")
                        
                        # Create the database and the tables.-START
                        init_table(con())
                        # Create the database and the tables.-END
                        
                        # Disable the button to prevent multiple clicks.-START
                        eye_btn.config(state="disabled")
                        btn.config(state="disabled")
                        # Disable the button to prevent multiple clicks.-END
                        
                        # Close the window after 2 seconds.-START
                        self.after(3500, self.destroy)
                        # Close the window after 2 seconds.-END
                    else:
                        error_msg.config(text="Must be at least 8 characters long.\nPlease try again.")
                        self.after(2000, clear_error_msg)
                else:
                    error_msg.config(text="Passwords do not match.\nPlease try again.")
                    self.after(2000, clear_error_msg)
            else:
                error_msg.config(text="All fields are required.", text_color="red")
                self.after(2000, clear_error_msg)
        # Create the function to validate the entries. -END
        
        # Create function to automatically clear the error message. -START
        def clear_error_msg()->None:
            """ Clear the error message. """
            error_msg.config(text="")
            
        # Create function to automatically clear the error message. -END
        
        
        def show_pass()->None:
            """ Show the password. """
            entry1.config(show="")
            entry2.config(show="")
            eye_btn.config(image=eye_on)
            self.after(1500, hide_pass)
        
        
        def hide_pass()->None:
            """ Hide the password. """
            entry1.config(show="*")
            entry2.config(show="*")
            eye_btn.config(image=eye_off)
    
    
        eye_btn.config(command=show_pass)
        btn.config(command=create_master_pass)
        
        
        
        
# SetupScreen().mainloop()
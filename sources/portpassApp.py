import tkinter
import customtkinter
from setupMasterPass import takeMasterPass

customtkinter.set_default_color_theme("green")
class PortpassApp(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Portpass")
        self.geometry("300x500")
        # self.iconbitmap("resources/icon.ico")
        self.resizable(False, False)
    #     self.create_widgets()



    # def create_widgets(self):
    #     self.how_to_use_label = tkinter.Label(self, text="How to use:")
    #     self.how_to_use_label.pack(x=10, y=10)
    def setup_master_pass(self):
        self.title("Portpass: Setup")
        self.geometry("300x400")
        
        # Create a label for the master password setup.-START
        self.how_to_use_label = customtkinter.CTkLabel(text='''LET'S CREATE A\nMASTER PASSWORD\nTO GET STARTED''', width=120, height=25, corner_radius=8)
        # Place the label in the center of the screen.
        self.how_to_use_label.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)
        
        # Create a entry box for the master password. -START
        self.master_pass_entry1 = customtkinter.CTkEntry(width=140,
                                                        height=25,
                                                        placeholder_text="Master password",
                                                        show="*",
                                                        corner_radius=8)
        
        self.master_pass_entry2 = customtkinter.CTkEntry(width=140,
                                                        height=25,
                                                        placeholder_text="Re-Enter Master pass...",
                                                        show="*",
                                                        corner_radius=8)
        # Place the entry box. -START
        self.master_pass_entry1.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)
        self.master_pass_entry2.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        
        # Check if master pass entries match. -START
        def create_master_pass() -> bool:
            entry1 = self.master_pass_entry1.get()
            entry2 = self.master_pass_entry2.get()
            if entry1 != '' or entry2 != '':
                self.master_pass_message.config(text="")
                if entry1 == entry2:
                    # self.master_pass_entry1.config(show="")
                    # self.master_pass_entry2.config(show="")
                    if takeMasterPass(entry1) is True:
                        self.master_pass_message.config(text="Master password stored.", text_color="green")
                        return True
                    else:
                        self.master_pass_message.config(text="Master password is not secure.\nTry again.", text_color="red")
                        return False
                else:
                    self.master_pass_message.config(text="Master passwords do not match.\nTry again.", text_color="red")
                    return False
            else:
                self.master_pass_message.config(text="All fields are required.", text_color="red")
                return False
        
        
        # Display a message if the master password is not secure or same. -START
        self.master_pass_message = customtkinter.CTkLabel(text="", width=120, height=25,
                                                          corner_radius=8, text_color="red")
        # place the message in the center of the screen.
        self.master_pass_message.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)
        
        
        
        # Create a button to take the master password. -START
        self.master_pass_button = \
            customtkinter.CTkButton(width=20,
                                    height=35,
                                    corner_radius=8,
                                    text="CREATE",
                                    command= create_master_pass)
        self.master_pass_button.place(relx=0.5, rely=0.8,
                                      anchor=tkinter.CENTER)
        # takeMasterPass()


portpass = PortpassApp()
portpass.setup_master_pass()
portpass.mainloop()
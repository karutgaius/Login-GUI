from importlib.metadata import entry_points
import tkinter
import tkinter.messagebox
import customtkinter
from matplotlib.pyplot import show
import pyautogui

sys_resolution = pyautogui.size()
sys_width = sys_resolution[0]
sys_height = sys_resolution[1]
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("dark-blue")

class App(customtkinter.CTk):
    WIDTH = int(sys_width*0.2)
    HEIGHT = int(sys_height*0.3)

    def __init__(self):
        super().__init__()

        #----------------------------------------------------------
        #Window Configuration
        self.title("Database Login")
        self.wm_iconbitmap('Assets/logo.ico')
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.main_frame = customtkinter.CTkFrame(master=self,
                                                 width=App.WIDTH,
                                                 corner_radius=0)
        self.main_frame.grid(row=0, column=0, sticky="nswe")

        self.main_frame.grid_rowconfigure(0, minsize=0)
        self.main_frame.grid_rowconfigure(5, weight=1) 
        self.main_frame.grid_rowconfigure(8, minsize=20)  
        self.main_frame.grid_rowconfigure(11, minsize=10) 

        self.frame_header = customtkinter.CTkLabel(master=self.main_frame,
                                    text="Login",
                                    text_font=("Roboto Medium", -16))
        self.frame_header.grid(row=1, column=0, pady=2, padx=10, sticky="we")
        
        self.username_box = customtkinter.CTkEntry(master=self.main_frame,
                                            width=int(App.WIDTH * 0.7),
                                            # width= 20,
                                            placeholder_text="Username")
        self.username_box.grid(row=2, column=0, columnspan=2, pady=4, padx=40, sticky="we")

        test_2 = self.password_box = customtkinter.CTkEntry(master=self.main_frame,
                                            width=int(App.WIDTH * 0.7),show='*',
                                            placeholder_text="Password")
        self.password_box.grid(row=3, column=0, columnspan=2, pady=4, padx=40, sticky="we")
        
        self.login_button = customtkinter.CTkButton(master=self.main_frame,
                                                text="Login",
                                                command=self.login_function)
        self.login_button.grid(row=4, column=0, pady=4, padx=20)
        
        self.label_login_feed_back = customtkinter.CTkLabel(master=self.main_frame, 
                                                            text="Login Feedback",
                                                            text_font=("Roboto Medium", -13))
        self.label_login_feed_back.grid(row=9, column=0, pady=0, padx=0, sticky="w")

        self.login_feedback = customtkinter.CTkLabel(master=self.main_frame,
                                                   text = self.login_function,
                                                   width=int(App.WIDTH * 0.868),
                                                   height=int(App.HEIGHT * 0.1),
                                                   corner_radius=6,
                                                   fg_color=("white", "black"), 
                                                   justify=tkinter.LEFT)
        self.login_feedback.grid(column=0, row=10, sticky="w", padx=15, pady=0)

    # function to close window
    def on_closing(self, event=0):
        self.destroy()

    # function to log in to api
    def login_function(self):
        user_name= self.username_box.get() #gets username from username input box
        pass_word=self.password_box.get() #gets password form pasword input box

        #---------------------------------------------------------------
        #API will be passed here as user desires
        #---------------------------------------------------------------

        self.login_feedback.configure(text=user_name+pass_word) #sends text to login feedback box configure the value of text to display desired feedback

if __name__ == "__main__":
    app = App()
    app.mainloop()
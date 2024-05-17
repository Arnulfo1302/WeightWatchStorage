from PIL import Image
import customtkinter
import disk
import infoTab
from infoTab import ToplevelWindow
import listaDatos
import os

disk_instance = disk.Disk()


class MyApp:
    def __init__(self):
        self.app = customtkinter.CTk()
        self.app.title("Weight Watch Storage")
        self.app.geometry("1000x900")
        self.create_widgets()
        self.print_drives()

    def create_widgets(self):
        self.frame1 = customtkinter.CTkFrame(self.app)
        self.frame1.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        self.app.grid_columnconfigure(0, weight=6)

        self.frame2 = customtkinter.CTkFrame(self.app)
        self.frame2.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        self.app.grid_columnconfigure(1, weight=4)

        self.app.grid_rowconfigure(0, weight=1)

        self.toplevel_window = None

    def run(self):
        self.app.mainloop()

    def print_drives(self):
        img_path = 'img/disco-duro-externo.png'
        drive_img = customtkinter.CTkImage(light_image=Image.open(img_path), dark_image=Image.open(img_path),
        size=(80, 80))

        drives = disk_instance.detect_drives()

        for drive in drives:
            self.frameDrive = customtkinter.CTkFrame(self.frame1)
            self.frameDrive.pack(padx=10, pady=10)

            self.label = customtkinter.CTkLabel(self.frameDrive, image=drive_img, text="")
            self.label.pack(padx=10, pady=10)

            drive_letter = f"{drive['Drive']}"
            drive_info = f"{round(drive['Free'], 1)} GB available out of {round(drive['Total'], 1)} GB"
            self.labelText = customtkinter.CTkLabel(self.label, text="", width=200, height=80)
            self.labelText.grid(column=1, row=0, padx=20)
            self.labelText = customtkinter.CTkLabel(self.labelText, text=drive_letter, anchor="w")
            self.labelText.grid(column=0, row=0)
            self.labelText = customtkinter.CTkLabel(self.labelText, text=drive_info, anchor="w")
            self.labelText.grid(column=0, row=1)

            self.drive_button = customtkinter.CTkButton(self.label, text="Scan",
                                                        command=lambda letter=drive_letter: self.open_toplevel(letter))

            self.drive_button.grid(column=2, row=0, padx=20, pady=20)

    def open_toplevel(self, drive_letter):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = ToplevelWindow(self, drive_letter)
        else:
            self.toplevel_window.focus()


my_app = MyApp()
my_app.run()

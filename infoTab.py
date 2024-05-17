import customtkinter
import os
import listaDatos


class ToplevelWindow(customtkinter.CTkToplevel):
    def __init__(self, parent, drive_letter):
        super().__init__(parent.app)
        self.geometry("700x700")
        self.drive_letter = drive_letter  # Almacenar drive_letter para su uso posterior

        self.frame = customtkinter.CTkFrame(self, corner_radius=20)
        self.frame.pack(padx=10, pady=10, fill="both", expand=True)

        self.textbox = customtkinter.CTkTextbox(self.frame, corner_radius=20)
        self.textbox.pack(padx=20, pady=20, fill="both", expand=True)
        self.fill_text(drive_letter)

    def fill_text(self, path):
        path_directory = path
        list = listaDatos.lista_datos().organize_by_weight(path_directory)
        aux = ""
        for filepath, tamaño in list:
            if tamaño > 1000000:
                print(f"{filepath}: {tamaño} bytes")
                aux = aux + f"{filepath}: {tamaño} bytes\n"
        self.textbox.insert("0.0", aux)
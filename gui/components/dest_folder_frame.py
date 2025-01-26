import tkinter as tk
from tkinter import filedialog

class DestinationFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.destination_path = ""
        self.setup_gui()

    def get_dest_path(self):
        return self.destination_path

    
    def setup_gui(self):
        #Two Columns
        self.columnconfigure(0, weight=0)
        self.columnconfigure(1, weight=3)

        # Zielordner auswählen
        destination_button = tk.Button(self, text="Zielordner auswählen", command=self.set_destination_path)
        destination_button.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        
        # Label für Zielordner
        self.destination_label = tk.Label(self, text="Kein Zielordner ausgewählt", anchor="w", relief="sunken")
        self.destination_label.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
    
    def set_destination_path(self):
        folder = filedialog.askdirectory(title="Zielordner auswählen")
        if folder:
            self.destination_path = folder
            self.destination_label.config(text=f"Ziel: {folder}")
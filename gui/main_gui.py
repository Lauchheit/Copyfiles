import tkinter as tk
from tkinter import filedialog, messagebox
from .components.source_folder_frame import SourceFrame
from .components.dest_folder_frame import DestinationFrame
from .components.searchstring_frame import SearchFrame
#from .components.status_frame import StatusFrame
from file_operations import copyfiles

class FileCopyGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Dateikopierer mit Suchstrings")
        self.root.geometry("800x500")

        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1)
        
        self.setup_gui()
    
    def setup_gui(self):
        self.source_frame = SourceFrame(self.root)
        self.source_frame.grid(row=0, column=0, columnspan=2, sticky="nsew") 
    
        self.destination_frame = DestinationFrame(self.root)
        self.destination_frame.grid(row=1, column=0, columnspan=2, sticky="ew")
    
        self.search_frame = SearchFrame(self.root)
        self.search_frame.grid(row=2, column=0, columnspan=2, sticky="ew")

        # Kopieren starten
        start_button = tk.Button(self.root, text="Kopieren starten", command=self.start_copying)
        start_button.grid(row=8, column=0, columnspan=2, padx=10, pady=20)

        # Statusanzeige
        self.status_label = tk.Label(self.root, text="", anchor="w", relief="sunken")
        self.status_label.grid(row=9, column=0, columnspan=2, padx=10, pady=10, sticky="ew")
    

    def start_copying(self):
        if not self.destination_frame.get_dest_path():
            messagebox.showerror("Fehler", "Bitte wählen Sie einen Zielordner aus!")
            return
        
        if not self.search_frame.get_search_strings():
            messagebox.showerror("Fehler", "Bitte fügen Sie mindestens einen Suchstring hinzu!")
            return
        
        try:
            copied_files = copyfiles.copy(self.source_frame.get_source_paths(), self.destination_frame.get_dest_path(), self.search_frame.get_search_strings())
            self.status_label.config(text=f"{copied_files} Dateien kopiert.")
            messagebox.showinfo("Fertig", f"{copied_files} Dateien erfolgreich kopiert!")
        except Exception as e:
            messagebox.showerror("Fehler", str(e))

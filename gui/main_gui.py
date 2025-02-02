import tkinter as tk
from tkinter import filedialog, messagebox
from .components.source_folder_frame import SourceFrame
from .components.dest_folder_frame import DestinationFrame
from .components.searchstring_frame import SearchFrame
from .components.searchext_frame import SearchExtFrame
#from .components.status_frame import StatusFrame
from file_operations import copyfiles

class FileCopyGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Dateikopierer mit Suchstrings")
        self.root.geometry("800x800")

        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1)
        
        self.setup_gui()
    
    def setup_gui(self):
        #Quellordner angeben
        self.source_frame = SourceFrame(self.root)
        self.source_frame.grid(row=0, column=0, columnspan=2, sticky="nsew") 
    
        #Zielordner angeben
        self.destination_frame = DestinationFrame(self.root)
        self.destination_frame.grid(row=1, column=0, columnspan=2, sticky="ew")
    
        #Suchstring eingeben
        self.search_frame = SearchFrame(self.root)
        self.search_frame.grid(row=2, column=0, columnspan=2, sticky="ew")

        #Mögliche Dateiendungen angeben

        self.ext_frame = SearchExtFrame(self.root)
        self.ext_frame.grid(row=3, column=0, columnspan=2, sticky="ew")

        # Kopieren starten
        start_button = tk.Button(self.root, text="Kopieren starten", command=self.start_copying)
        start_button.grid(row=4, column=0, columnspan=2, padx=10, pady=20)

        # Statusanzeige
        self.status_label = tk.Label(self.root, text="", anchor="w", relief="sunken")
        self.status_label.grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky="ew")
    

    def start_copying(self):
        if not self.destination_frame.get_dest_path():
            messagebox.showerror("Fehler", "Bitte wählen Sie einen Zielordner aus!")
            return
        
        try:
            #create new instance of copyfiles to erase side effects from previous copies
            copyer = copyfiles.CopyFiles(self.source_frame.get_source_paths(), 
                                         self.destination_frame.get_dest_path(), 
                                         self.search_frame.get_search_strings(), 
                                         self.ext_frame.get_extension_settings()) 
            copied_files = copyer.start_copy()
            self.status_label.config(text=f"{copied_files} Dateien kopiert.")
            messagebox.showinfo("Fertig", f"{copied_files} Dateien erfolgreich kopiert!")
        except Exception as e:
            import traceback
            print(traceback.format_exc())
            messagebox.showerror("Fehler", str(e))

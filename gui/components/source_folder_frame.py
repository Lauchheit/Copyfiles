import tkinter as tk
from tkinter import filedialog

class SourceFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.source_paths = []
        self.setup_gui()

    
    def setup_gui(self):
        #One Column
        self.columnconfigure(0, weight=1)

        # Rahmen für die Quellpfad-Buttons
        sourcepath_button_frame = tk.Frame(self)  
        sourcepath_button_frame.grid(row=0, column=0, columnspan=2, sticky="w", padx=10, pady=5)

        # Quellordner hinzufügen Button
        source_button = tk.Button(sourcepath_button_frame, text="Quellordner hinzufügen", command=self.add_source_path)
        source_button.pack(side=tk.LEFT, padx=5)

        # Entfernen-Button für Quellpfade
        remove_source_button = tk.Button(sourcepath_button_frame, text="Entfernen", command=self.remove_selected_source)
        remove_source_button.pack(side=tk.LEFT, padx=5)
        
        # Listbox für Quellpfade
        self.source_listbox = tk.Listbox(self)
        self.source_listbox.grid(row=1, column=0, columnspan=1, padx=10, pady=5, sticky="ew")
    
    def get_source_paths(self):
        return self.source_paths

    def add_source_path(self):
        folder = filedialog.askdirectory(title="Quellordner auswählen")
        if folder and folder not in self.source_paths:
            self.source_paths.append(folder)
            self.source_listbox.insert(tk.END, folder)
    
    def remove_selected_source(self):
        selected_indices = self.source_listbox.curselection()
        for index in reversed(selected_indices):
            del self.source_paths[index]
            self.source_listbox.delete(index)
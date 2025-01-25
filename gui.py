import tkinter as tk
from tkinter import filedialog, messagebox
import copyfiles  # Importiere deine copyfiles-Methode


class FileCopyGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Dateikopierer mit Suchstrings")
        self.root.geometry("800x500")  
        
        # Quellpfade und Suchstrings
        self.source_paths = []
        self.search_strings = []
        
        # GUI-Elemente
        self.setup_gui()
    
    def setup_gui(self):
        # Erstelle ein flexibles Grid-Layout
        self.root.columnconfigure(0, weight=0)
        self.root.columnconfigure(1, weight=3)
        
        # Rahmen für die Suchstring-Buttons
        sourcepath_button_frame = tk.Frame(self.root)
        sourcepath_button_frame.grid(row=0, column=0, columnspan=2, sticky="w", padx=10, pady=5)

        # Quellordner hinzufügen Button
        source_button = tk.Button(sourcepath_button_frame, text="Quellordner hinzufügen", command=self.add_source_path)
        source_button.pack(side=tk.LEFT, padx=5)

        # Entfernen-Button für Quellpfade
        remove_source_button = tk.Button(sourcepath_button_frame, text="Entfernen", command=self.remove_selected_source)
        remove_source_button.pack(side=tk.LEFT, padx=5)
        
        # Listbox für Quellpfade
        self.source_listbox = tk.Listbox(self.root, height=10)
        self.source_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=5, sticky="ew")
        
        
        # Zielordner auswählen
        destination_button = tk.Button(self.root, text="Zielordner auswählen", command=self.set_destination_path)
        destination_button.grid(row=3, column=0, padx=10, pady=10, sticky="w")
        
        # Label für Zielordner
        self.destination_label = tk.Label(self.root, text="Kein Zielordner ausgewählt", anchor="w", relief="sunken")
        self.destination_label.grid(row=3, column=1, padx=10, pady=10, sticky="ew")
        
        # Suchstring hinzufügen
        tk.Label(self.root, text="Suchstring:").grid(row=4, column=0, padx=10, pady=5, sticky="w")
        self.search_entry = tk.Entry(self.root)
        self.search_entry.grid(row=4, column=1, padx=10, pady=5, sticky="ew")
        

        # Rahmen für die Suchstring-Buttons
        searchstring_button_frame = tk.Frame(self.root)
        searchstring_button_frame.grid(row=5, column=0, columnspan=2, sticky="w", padx=10, pady=5)

        # Suchstring Hinzufügen-Button
        add_search_button = tk.Button(searchstring_button_frame, text="Hinzufügen", command=self.add_search_string)
        add_search_button.pack(side=tk.LEFT, padx=5)

        # Suchstring Entfernen-Button
        remove_search_button = tk.Button(searchstring_button_frame, text="Entfernen", command=self.remove_search_string)
        remove_search_button.pack(side=tk.LEFT, padx=5)

        # Suchstring-Liste
        self.search_listbox = tk.Listbox(self.root, height=5)
        self.search_listbox.grid(row=6, column=0, columnspan=2, padx=10, pady=5, sticky="ew")
        
        
        # Kopieren starten
        start_button = tk.Button(self.root, text="Kopieren starten", command=self.start_copying)
        start_button.grid(row=8, column=0, columnspan=2, padx=10, pady=20)
        
        # Statusanzeige
        self.status_label = tk.Label(self.root, text="", anchor="w", relief="sunken")
        self.status_label.grid(row=9, column=0, columnspan=2, padx=10, pady=10, sticky="ew")
    
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
    
    def set_destination_path(self):
        folder = filedialog.askdirectory(title="Zielordner auswählen")
        if folder:
            self.destination_path = folder
            self.destination_label.config(text=f"Ziel: {folder}")
    
    def add_search_string(self):
        search_string = self.search_entry.get().strip()
        if search_string and search_string not in self.search_strings:
            self.search_strings.append(search_string)
            self.search_listbox.insert(tk.END, search_string)
            self.search_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warnung", "Suchstring darf nicht leer oder schon vorhanden sein!")

    def remove_search_string(self):
        if self.search_listbox.curselection():
            self.remove_selected_search_string() 
        elif self.search_entry.get().strip() in self.search_strings:
            self.remove_specified_search_string()
        else:
            messagebox.showwarning("Warnung", "Kein valider Suchstring ausgewählt oder eingegeben")
    
    def remove_selected_search_string(self):
        selected_indices = self.search_listbox.curselection()
        for index in reversed(selected_indices):
            del self.search_strings[index]
            self.search_listbox.delete(index)

    def remove_specified_search_string(self):
        search_string = self.search_entry.get().strip()
        if search_string and search_string in self.search_strings:
            self.search_strings.remove(search_string)
            
            items = self.search_listbox.get(0, tk.END)
            if search_string in items:
                index = items.index(search_string)
                self.search_listbox.delete(index)  
            else:
                print("Eintrag nicht gefunden!")
            
            self.search_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warnung", "Suchstring muss in der Liste sein!")

    def start_copying(self):
        if not hasattr(self, "destination_path") or not self.destination_path:
            messagebox.showerror("Fehler", "Bitte wählen Sie einen Zielordner aus!")
            return
        
        if not self.search_strings:
            messagebox.showerror("Fehler", "Bitte fügen Sie mindestens einen Suchstring hinzu!")
            return
        
        try:
            copied_files = copyfiles.copy(self.source_paths, self.destination_path, self.search_strings)
            self.status_label.config(text=f"{copied_files} Dateien kopiert.")
            messagebox.showinfo("Fertig", f"{copied_files} Dateien erfolgreich kopiert!")
        except Exception as e:
            messagebox.showerror("Fehler", str(e))

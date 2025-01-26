import tkinter as tk
from tkinter import messagebox

class SearchFrame(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent)
        self.search_strings = []

        self.setup_gui()

    def get_search_strings(self):
        return self.search_strings
    
    def setup_gui(self):
        #One Column
        self.columnconfigure(0, weight=0)
        self.columnconfigure(1, weight=3)

        # Suchstring hinzufügen
        tk.Label(self, text="Suchstring:").grid(row=4, column=0, padx=10, pady=5, sticky="w")
        self.search_entry = tk.Entry(self)
        self.search_entry.grid(row=4, column=1, padx=10, pady=5, sticky="ew")
        
        # Rahmen für die Suchstring-Buttons
        searchstring_button_frame = tk.Frame(self)
        searchstring_button_frame.grid(row=5, column=0, columnspan=2, sticky="w", padx=10, pady=5)

        # Suchstring Hinzufügen-Button
        add_search_button = tk.Button(searchstring_button_frame, text="Hinzufügen", command=self.add_search_string)
        add_search_button.pack(side=tk.LEFT, padx=5)

        # Suchstring Entfernen-Button
        remove_search_button = tk.Button(searchstring_button_frame, text="Entfernen", command=self.remove_search_string)
        remove_search_button.pack(side=tk.LEFT, padx=5)

        # Suchstring-Liste
        self.search_listbox = tk.Listbox(self, height=5)
        self.search_listbox.grid(row=6, column=0, columnspan=2, padx=10, pady=5, sticky="ew")

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
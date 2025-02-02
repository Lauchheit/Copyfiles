import tkinter as tk
from tkinter import messagebox

class SearchExtFrame(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent)
        self.search_exts = []
        self.all_ext = tk.BooleanVar(value=True)  # Verwende BooleanVar für die Checkbox
        self.setup_gui()

    def get_search_exts(self):
        return self.search_exts

    def setup_gui(self):
        # Eine Spalte konfigurieren
        self.columnconfigure(0, weight=0)
        self.columnconfigure(1, weight=3)

        # Checkbox mit Label
        self.checkbox_label = tk.Label(self, text="Alle Dateiendungen verwenden:")
        self.checkbox_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.checkbox = tk.Checkbutton(
            self, variable=self.all_ext, command=self.update_ui
        )
        self.checkbox.grid(row=0, column=1, padx=10, pady=5, sticky="w")

        #"Dateiendung:" Text 
        self.namelabel = tk.Label(self, text="Dateiendung:")
        self.namelabel.grid(row=1, column=0, padx=10, pady=5, sticky="w")

        # Dateiendung Suchstring hinzufügen
        self.search_entry = tk.Entry(self)
        self.search_entry.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

        # Rahmen für die Dateiendung Suchstring-Buttons
        self.searchstring_button_frame = tk.Frame(self)
        self.searchstring_button_frame.grid(row=2, column=0, columnspan=2, sticky="w", padx=10, pady=5)

        # Buttons innerhalb des Rahmens
        self.add_search_button = tk.Button(self.searchstring_button_frame, text="Hinzufügen", command=self.add_search_ext)
        self.add_search_button.pack(side=tk.LEFT, padx=5)
        self.remove_search_button = tk.Button(self.searchstring_button_frame, text="Entfernen", command=self.remove_search_ext)
        self.remove_search_button.pack(side=tk.LEFT, padx=5)

        # Dateiendung Suchstring-Liste
        self.search_listbox = tk.Listbox(self, height=5)
        self.search_listbox.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky="ew")

        # Initiales UI-Update
        self.update_ui()

    def get_extension_settings(self):
        return self.all_ext.get(), self.search_exts

    def update_ui(self):
        """Aktualisiert das UI basierend auf dem Zustand der Checkbox."""
        if self.all_ext.get():
            # Verstecke die Widgets
            self.search_entry.grid_remove()
            self.searchstring_button_frame.grid_remove()
            self.search_listbox.grid_remove()
            self.namelabel.grid_remove()  # Falls der Label für "Dateiendung:" gemeint ist
        else:
            # Zeige die Widgets
            self.search_entry.grid()
            self.searchstring_button_frame.grid()
            self.search_listbox.grid()
            self.namelabel.grid()  # Zeige den Label wieder

    def check_search_ext(self, ext:str):
        error_message:str = ""
        viable:bool = True
        if not ext[0] == '.' : 
            viable = False
            error_message += "\n-File extention must start with a dot \'.\'"
        
        return viable, error_message


    def add_search_ext(self):
        search_ext = self.search_entry.get().strip()
        if search_ext and search_ext not in self.search_exts:
            viable, error_message = self.check_search_ext(search_ext)
            if not viable: 
                messagebox.showwarning("Warnung", error_message)
            self.search_exts.append(search_ext)
            self.search_listbox.insert(tk.END, search_ext)
            self.search_entry.delete(0, tk.END)

    def remove_search_ext(self):
        if self.search_listbox.curselection():
            self.remove_selected_search_ext()
        elif self.search_entry.get().strip() in self.search_exts:
            self.remove_specified_search_ext()
        else:
            messagebox.showwarning("Warnung", "Kein valider Dateiendung Suchstring ausgewählt oder eingegeben")

    def remove_selected_search_ext(self):
        selected_indices = self.search_listbox.curselection()
        for index in reversed(selected_indices):
            del self.search_exts[index]
            self.search_listbox.delete(index)

    def remove_specified_search_ext(self):
        search_ext = self.search_entry.get().strip()
        if search_ext and search_ext in self.search_exts:
            self.search_exts.remove(search_ext)

            items = self.search_listbox.get(0, tk.END)
            if search_ext in items:
                index = items.index(search_ext)
                self.search_listbox.delete(index)
            else:
                print("Eintrag nicht gefunden!")

            self.search_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warnung", "Dateiendung Suchstring muss in der Liste sein!")

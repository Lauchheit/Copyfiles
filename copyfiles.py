import os
import shutil


def copy(source_paths, destination_path, search_strings): 
    copied_files = 0  # Zählt alle kopierten Dateien

    for source in source_paths:
        if os.path.exists(source):  # Prüfen, ob der Quellordner existiert
            for file_name in os.listdir(source):
                file_path = os.path.join(source, file_name)  # Vollständigen Pfad erstellen

                if os.path.isdir(file_path):  # Prüfen, ob es ein Unterordner ist
                    # Rekursiver Aufruf der Funktion für Unterordner
                    copied_files += copy([file_path], destination_path, search_strings)
                elif any(search in file_name for search in search_strings):  # Datei-Check mit Suchstrings
                    if os.path.isfile(file_path):  # Prüfen, ob es eine Datei ist
                        dest_path = os.path.join(destination_path, file_name)
                        shutil.copy(file_path, dest_path)  # Datei kopieren
                        copied_files += 1
        else:
            raise Exception(f"Quellordner nicht gefunden: {source}")

    return copied_files 

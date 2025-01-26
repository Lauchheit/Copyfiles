import os
import shutil
from .file import File

class CopyFiles:
    def __init__(self, source_paths, destination_path, search_strings):
        self.viable_copy_files = []
        self.source_paths = source_paths
        self.destination_path = destination_path
        self.search_strings = search_strings

    def start_copy(self):
        self.viable_copy_files = self.get_copyable_files_list()
        self.copy_files()  # Klammern hinzugefügt
        return len(self.viable_copy_files)

    def get_copyable_files_list(self):
        new_found_files :list[File] = []
        for source in self.source_paths:
            if os.path.exists(source):
                for file_name in os.listdir(source):
                    file_path = os.path.join(source, file_name)
                    
                    if os.path.isdir(file_path):
                        # Rekursiver Aufruf mit neuem Pfad
                        sub_copy = CopyFiles([file_path], self.destination_path, self.search_strings)
                        new_found_files.extend(sub_copy.get_copyable_files_list())
                    
                    elif os.path.isfile(file_path) and any(search in file_name for search in self.search_strings):
                        #count = count entries of filename in new_found_files 
                        #count = sum(1 for file in new_found_files if file.get_filename() == file_name)
                        count = 1
                        for file in new_found_files:
                            if file.get_filename() == file_name:
                                count+=1
                                file.mark_as_dublicate()
                        new_found_files.append(File(file_path, file_name, count))
            else:
                raise Exception(f"Quellordner nicht gefunden: {source}")
        print(new_found_files)
        return new_found_files
    
    def copy_files(self):
        for file in self.viable_copy_files:
            if file.is_dublicate():
                # Generiere den neuen Namen mit Version (_v1, _v2, ...)
                new_file_name = file.get_dublicate_file_name()
            else:
                new_file_name = file.get_filename()

            dest_path = os.path.join(self.destination_path, new_file_name)

            # Datei kopieren
            shutil.copy(file.get_file_path(), dest_path)
import os
import shutil
from .file import File

class CopyFiles:
    def __init__(self, source_paths, destination_path, search_strings, extention_settings):
        self.viable_copy_files = []

        self.source_paths = source_paths
        self.destination_path = destination_path
        self.search_strings = search_strings
        self.all_exts, self.extention_strings = extention_settings

    def start_copy(self):
        self.viable_copy_files = self.get_copyable_files_list()
        self.copy_files()  
        return len(self.viable_copy_files)

    def get_copyable_files_list(self):
        new_found_files :list[File] = []
        for source in self.source_paths:
            if os.path.exists(source):
                for file_name in os.listdir(source):
                    file_path = os.path.join(source, file_name)
                    
                    if os.path.isdir(file_path):
                        # Rekursiver Aufruf mit neuem Pfad
                        print("Enter new directory: " + file_path)
                        sub_copy = CopyFiles([file_path], self.destination_path, self.search_strings, (self.all_exts, self.extention_strings))
                        new_found_files.extend(sub_copy.get_copyable_files_list())
                    
                    elif self.file_is_searched(file_path, file_name):
                        #count = count entries of filename in new_found_files 
                        #count = sum(1 for file in new_found_files if file.get_filename() == file_name)
                        count = 1
                        for file in new_found_files:
                            if file.get_filename() == file_name :
                                count+=1
                                file.mark_as_dublicate()
                        new_found_files.append(File(file_path, file_name, count))
            else:
                raise Exception(f"Quellordner nicht gefunden: {source}")
        return new_found_files
    
    def file_is_searched(self, file_path, file_name)->bool:
        #file needs to be a ...well, a file
        if os.path.isfile(file_name): 
            return False
        #file needs to have contain the specified searchstring
        if len(self.search_strings)>1 and not any(search in file_name for search in self.search_strings): 
            return False
        #file needs to be of one of the specified endings
        if not self.all_exts and not any(search in file_name for search in self.extention_strings):
            return False
        print("Valid File found: " + file_name)
        return True
    
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
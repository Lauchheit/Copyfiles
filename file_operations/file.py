import os

class File:
    def __init__(self, filepath, filename, dublicateCount):
        self.filepath = filepath
        self.filename= filename
        self.isDublicate:bool = dublicateCount > 1
        self.dublicateCount:int = dublicateCount

    def get_file_path(self):
        return self.filepath

    def mark_as_dublicate(self):
        self.isDublicate = True

    def is_dublicate(self):
        return self.isDublicate

    def get_filename(self):
        return self.filename
    
    def get_dublicate_file_name(self):
        base_name, ext = os.path.splitext(self.filename)
        name = f"{base_name}_v{self.dublicateCount}{ext}"
        return name

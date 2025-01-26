try:
    import tkinter as tk
except ImportError:
    print("Tkinter ist auf diesem System nicht installiert. Bitte installieren Sie es, um die GUI zu verwenden. Für weitere Infos siehe Readme.pdf")
    exit(1)

from gui.main_gui import FileCopyGUI

if __name__ == "__main__":
    root = tk.Tk()
    app = FileCopyGUI(root)
    root.mainloop()
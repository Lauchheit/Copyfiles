import tkinter as tk
import gui
try:
    import tkinter as tk
except ImportError:
    print("Tkinter ist auf diesem System nicht installiert. Bitte installieren Sie es, um die GUI zu verwenden. Für weitere Infos siehe Readme.pdf")
    exit(1)

# Hauptprogramm
if __name__ == "__main__":
    root = tk.Tk()
    app = gui.FileCopyGUI(root)
    root.mainloop()

# Python Programm Installation und Ausführung

Diese Anleitung führt Sie durch die Installation von Python und die Ausführung des Programms.

## Voraussetzungen

Sie benötigen:
- Einen Computer mit Windows, macOS oder Linux
- Administratorrechte zur Installation von Software
- Die heruntergeladenen Programmdateien (main.py und weitere Python-Dateien)

## 1. Python Installation

### Windows
1. Besuchen Sie die offizielle Python-Website: https://www.python.org/downloads/
2. Klicken Sie auf "Download Python" (neueste Version)
3. Führen Sie die heruntergeladene .exe Datei aus
4. **Wichtig**: Aktivieren Sie das Kontrollkästchen "Add Python to PATH" während der Installation
5. Klicken Sie auf "Install Now"

### macOS
1. Besuchen Sie die offizielle Python-Website: https://www.python.org/downloads/
2. Klicken Sie auf "Download Python" (neueste Version)
3. Führen Sie die heruntergeladene .pkg Datei aus
4. Folgen Sie den Anweisungen des Installers

### Linux
Die meisten Linux-Distributionen haben Python bereits vorinstalliert. Falls nicht:

```bash
sudo apt-get update
sudo apt-get install python3
```

## 2. Installation überprüfen

Öffnen Sie ein Terminal (Kommandozeile):
- Windows: Drücken Sie `Windows + R`, tippen Sie `cmd` und drücken Sie Enter
- macOS: Öffnen Sie das Terminal-Programm
- Linux: Öffnen Sie ein Terminal


  
  
Geben Sie ein:
```bash
python --version
```

Sie sollten eine Versionsnummer sehen (z.B. "Python 3.10.0")

## 3. Programm ausführen

1. Öffnen Sie ein Terminal/Kommandozeile
2. Navigieren Sie in den Ordner mit den Python-Dateien:
   ```bash
   cd Pfad/zum/Programmordner
   ```
3. Führen Sie das Programm aus:
   ```bash
   python main.py
   ```

## Fehlerbehebung

### "Python wird nicht erkannt..."
- Windows: Installieren Sie Python neu und aktivieren Sie "Add Python to PATH"
- macOS/Linux: Stellen Sie sicher, dass Python korrekt installiert wurde

### "ModuleNotFoundError" oder fehlende Module

#### Installation von pip
Falls pip nicht installiert ist:

Windows:
```bash
python -m ensurepip --default-pip
```

Linux:
```bash
sudo apt-get install python3-pip
```

macOS:
```bash
python -m ensurepip --default-pip
```

#### Installation von tkinter
Falls tkinter fehlt:

Windows:
- Tkinter sollte standardmäßig dabei sein
- Falls nicht: Python neu installieren und bei der Installation "tcl/tk and IDLE" auswählen

Linux:
```bash
sudo apt-get install python3-tk
```

macOS:
```bash
brew install python-tk@3.9
```

#### Weitere Module
Falls andere Module fehlen:
```bash
pip install modulname
```

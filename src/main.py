import sys
from PySide6.QtWidgets import QApplication
from ui.main_window import MainWindow

def main():
    # Initialisation de l'application Qt
    app = QApplication(sys.argv)
    
    # Création de la fenêtre principale
    window = MainWindow()
    window.show()
    
    # Exécution de l'application
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
from PySide6.QtWidgets import QMainWindow, QLabel, QComboBox, QPushButton, QVBoxLayout, QWidget, QHBoxLayout, QSpacerItem, QSizePolicy
from PySide6.QtGui import QFont, QMovie
from PySide6.QtCore import Qt, QFile, QTextStream

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("YouTube Prospector")
        self.setGeometry(100, 100, 800, 600)

        # Créer un widget central
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Créer un layout vertical pour les autres widgets
        layout = QVBoxLayout(central_widget)
        layout.setContentsMargins(0, 0, 0, 0)  # Enlever les marges pour que le contenu soit bien aligné

        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)

        # Titre avec du HTML pour styliser le texte
        title = QLabel('<span style="color: red;">You</span><span style="color: white;">Tube Prospector</span>', self)
        title_font = QFont("Arial", 36, QFont.Bold)
        title.setFont(title_font)
        title.setAlignment(Qt.AlignCenter)

        # Ajouter le titre au layout
        main_layout.addWidget(title)
        main_layout.addStretch(1)

        # Créer un layout horizontal pour le ComboBox et le bouton
        hbox_layout = QHBoxLayout()

        # Ajouter un spacer à gauche pour que les widgets soient centrés
        hbox_layout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))

        # ComboBox
        combo_box = QComboBox(self)
        combo_box.addItem("Option 1")
        combo_box.addItem("Option 2")
        combo_box.addItem("Option 3")
        combo_box.setFixedWidth(511)
        hbox_layout.addWidget(combo_box)

        hbox_layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Minimum))

        # Bouton
        button = QPushButton("Cliquez ici", self)
        hbox_layout.addWidget(button)

        hbox_layout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))

        main_layout.addLayout(hbox_layout)
        main_layout.addStretch(1)

        # Charger les styles depuis styles.qss
        self.load_styles()

    def load_styles(self):
        file = QFile("ui/styles.qss")
        if file.open(QFile.ReadOnly | QFile.Text):
            stream = QTextStream(file)
            self.setStyleSheet(stream.readAll())
        file.close()


import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
from PyQt5.QtGui import QFont
import mysql.connector

class ProjektMitarbeiterErfassen(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Label und Textfeld für Projekt-ID
        self.label_id_projekt = QLabel('Projekt-ID:')
        self.label_id_projekt.setFont(QFont('Arial', 12, QFont.Bold))
        self.input_id_projekt = QLineEdit()
        layout.addWidget(self.label_id_projekt)
        layout.addWidget(self.input_id_projekt)

        # Label und Textfeld für Mitarbeiter-ID
        self.label_id_mitarbeiter = QLabel('Mitarbeiter-ID:')
        self.label_id_mitarbeiter.setFont(QFont('Arial', 12, QFont.Bold))
        self.input_id_mitarbeiter = QLineEdit()
        layout.addWidget(self.label_id_mitarbeiter)
        layout.addWidget(self.input_id_mitarbeiter)

        # Speichern-Button
        self.button_save = QPushButton('Speichern')
        self.button_save.clicked.connect(self.save_data)
        layout.addWidget(self.button_save)

        self.setLayout(layout)
        self.setWindowTitle('Projektmitarbeiter Erfassung')

    def save_data(self):
        id_projekt = self.input_id_projekt.text()
        id_mitarbeiter = self.input_id_mitarbeiter.text()

        # Verbindung zur Datenbank herstellen
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='1234',
            database='kruemmel'
        )
        cursor = conn.cursor()

        # Daten in die Datenbank einfügen
        cursor.execute('''
            INSERT INTO projektmitarbeiter (id_Projekt, id_Mitarbeiter)
            VALUES (%s, %s)
        ''', (id_projekt, id_mitarbeiter))

        conn.commit()
        cursor.close()
        conn.close()

        # Bestätigung anzeigen
        self.button_save.setText('Gespeichert!')

def main(app):    
    ex = ProjektMitarbeiterErfassen()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
from PyQt5.QtGui import QFont
import mysql.connector

class FuehrungskraefteErfassung(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Label und Textfeld für Mitarbeiter-ID
        self.label_id_mitarbeiter = QLabel('Mitarbeiter-ID:')
        self.label_id_mitarbeiter.setFont(QFont('Arial', 12, QFont.Bold))
        self.input_id_mitarbeiter = QLineEdit()
        layout.addWidget(self.label_id_mitarbeiter)
        layout.addWidget(self.input_id_mitarbeiter)

        # Label und Textfeld für Position
        self.label_position = QLabel('Position: [vorhandene oder neue]')
        self.label_position.setFont(QFont('Arial', 12, QFont.Bold))
        self.input_position = QLineEdit()
        layout.addWidget(self.label_position)
        layout.addWidget(self.input_position)

        # Label und Checkbox für Führungskraft-Status
        self.label_ist_fuehrungskraft = QLabel('Ist Führungskraft: [0 nein 1 Ja]')
        self.label_ist_fuehrungskraft.setFont(QFont('Arial', 12, QFont.Bold))
        self.input_ist_fuehrungskraft = QLineEdit()
        layout.addWidget(self.label_ist_fuehrungskraft)
        layout.addWidget(self.input_ist_fuehrungskraft)

        # Speichern-Button
        self.button_save = QPushButton('Speichern')
        self.button_save.clicked.connect(self.save_data)
        layout.addWidget(self.button_save)

        self.setLayout(layout)
        self.setWindowTitle('Führungskräfte Erfassung')

    def save_data(self):
        id_mitarbeiter = self.input_id_mitarbeiter.text()
        position = self.input_position.text()
        ist_fuehrungskraft = self.input_ist_fuehrungskraft.text()

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
            INSERT INTO führungskräfte (id_Mitarbeiter, Position, ist_Führungskraft)
            VALUES (%s, %s, %s)
        ''', (id_mitarbeiter, position, ist_fuehrungskraft))

        conn.commit()
        cursor.close()
        conn.close()

        # Bestätigung anzeigen
        self.button_save.setText('Gespeichert!')

    
def main(app):    
    ex = FuehrungskraefteErfassung()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
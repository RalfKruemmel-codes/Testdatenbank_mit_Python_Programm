import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
from PyQt5.QtGui import QFont
import mysql.connector

class TeamErfassung(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Label und Textfeld für Teamname
        self.label_name = QLabel('Teamname:')
        self.label_name.setFont(QFont('Arial', 12, QFont.Bold))
        self.input_name = QLineEdit()
        layout.addWidget(self.label_name)
        layout.addWidget(self.input_name)

        # Label und Textfeld für Abteilungs-ID
        self.label_id_abteilung = QLabel('Abteilungs-ID:')
        self.label_id_abteilung.setFont(QFont('Arial', 12, QFont.Bold))
        self.input_id_abteilung = QLineEdit()
        layout.addWidget(self.label_id_abteilung)
        layout.addWidget(self.input_id_abteilung)

        # Speichern-Button
        self.button_save = QPushButton('Speichern')
        self.button_save.clicked.connect(self.save_data)
        layout.addWidget(self.button_save)

        self.setLayout(layout)
        self.setWindowTitle('Team Erfassung')

    def save_data(self):
        name = self.input_name.text()
        id_abteilung = self.input_id_abteilung.text()

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
            INSERT INTO teams (Name, id_Abteilung)
            VALUES (%s, %s)
        ''', (name, id_abteilung))

        conn.commit()
        cursor.close()
        conn.close()

        # Bestätigung anzeigen
        self.button_save.setText('Gespeichert!')


def main(app):    
    ex = TeamErfassung()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
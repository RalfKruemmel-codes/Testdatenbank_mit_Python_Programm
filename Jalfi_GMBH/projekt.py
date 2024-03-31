import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QDateEdit
from PyQt5.QtGui import QFont
import mysql.connector

class ProjektErfassung(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Label und Textfeld für den Projektnamen
        self.label_name = QLabel('Projektname:')
        self.label_name.setFont(QFont('Arial', 12, QFont.Bold))
        self.input_name = QLineEdit()
        layout.addWidget(self.label_name)
        layout.addWidget(self.input_name)

        # Label und Datumsfelder für Start- und Enddatum
        self.label_startdatum = QLabel('Startdatum:')
        self.label_startdatum.setFont(QFont('Arial', 12, QFont.Bold))
        self.input_startdatum = QDateEdit()
        layout.addWidget(self.label_startdatum)
        layout.addWidget(self.input_startdatum)

        self.label_enddatum = QLabel('Enddatum:')
        self.label_enddatum.setFont(QFont('Arial', 12, QFont.Bold))
        self.input_enddatum = QDateEdit()
        layout.addWidget(self.label_enddatum)
        layout.addWidget(self.input_enddatum)

        # Label und Textfeld für Projektleiter-ID
        self.label_id_projektleiter = QLabel('Projektleiter-ID:')
        self.label_id_projektleiter.setFont(QFont('Arial', 12, QFont.Bold))
        self.input_id_projektleiter = QLineEdit()
        layout.addWidget(self.label_id_projektleiter)
        layout.addWidget(self.input_id_projektleiter)

        # Label und Textfeld für die Beschreibung
        self.label_beschreibung = QLabel('Beschreibung:')
        self.label_beschreibung.setFont(QFont('Arial', 12, QFont.Bold))
        self.input_beschreibung = QLineEdit()
        layout.addWidget(self.label_beschreibung)
        layout.addWidget(self.input_beschreibung)

        # Speichern-Button
        self.button_save = QPushButton('Speichern')
        self.button_save.clicked.connect(self.save_data)
        layout.addWidget(self.button_save)

        self.setLayout(layout)
        self.setWindowTitle('Projekte Erfassung')

    def save_data(self):
        name = self.input_name.text()
        startdatum = self.input_startdatum.date().toString('yyyy-MM-dd')
        enddatum = self.input_enddatum.date().toString('yyyy-MM-dd')
        id_projektleiter = self.input_id_projektleiter.text()
        beschreibung = self.input_beschreibung.text()

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
            INSERT INTO projekte (name, startdatum, enddatum, id_Projektleiter, beschreibung)
            VALUES (%s, %s, %s, %s, %s)
        ''', (name, startdatum, enddatum, id_projektleiter, beschreibung))

        conn.commit()
        cursor.close()
        conn.close()

        # Bestätigung anzeigen
        self.button_save.setText('Gespeichert!')

def main(app):    
    ex = ProjektErfassung()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
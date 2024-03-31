import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QDateEdit
from PyQt5.QtGui import QFont
import mysql.connector

class UrlaubstageZeitraum(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Label und Textfeld für Urlaubstage-ID
        self.label_id = QLabel('Urlaubstage-ID:')
        self.label_id.setFont(QFont('Arial', 12, QFont.Bold))
        self.input_id = QLineEdit()
        layout.addWidget(self.label_id)
        layout.addWidget(self.input_id)

        # Label und DateEdit für Startdatum
        self.label_startdatum = QLabel('Startdatum:')
        self.label_startdatum.setFont(QFont('Arial', 12, QFont.Bold))
        self.input_startdatum = QDateEdit()
        layout.addWidget(self.label_startdatum)
        layout.addWidget(self.input_startdatum)

        # Label und DateEdit für Enddatum
        self.label_enddatum = QLabel('Enddatum:')
        self.label_enddatum.setFont(QFont('Arial', 12, QFont.Bold))
        self.input_enddatum = QDateEdit()
        layout.addWidget(self.label_enddatum)
        layout.addWidget(self.input_enddatum)

        # Label und Textfeld für Kommentar
        self.label_kommentar = QLabel('Kommentar:')
        self.label_kommentar.setFont(QFont('Arial', 12, QFont.Bold))
        self.input_kommentar = QLineEdit()
        layout.addWidget(self.label_kommentar)
        layout.addWidget(self.input_kommentar)

        # Speichern-Button
        self.button_save = QPushButton('Speichern')
        self.button_save.clicked.connect(self.save_data)
        layout.addWidget(self.button_save)

        self.setLayout(layout)
        self.setWindowTitle('Urlaubstage Zeitraum Erfassung')

    def save_data(self):
        id_urlaubstage = self.input_id.text()
        startdatum = self.input_startdatum.date().toString('yyyy-MM-dd')
        enddatum = self.input_enddatum.date().toString('yyyy-MM-dd')
        kommentar = self.input_kommentar.text()

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
            INSERT INTO urlaubstage (id_Urlaubstage, Startdatum, Enddatum, Kommentar)
            VALUES (%s, %s, %s, %s)
        ''', (id_urlaubstage, startdatum, enddatum, kommentar))

        conn.commit()
        cursor.close()
        conn.close()

        # Bestätigung anzeigen
        self.button_save.setText('Gespeichert!')

def main(app):    
    ex = UrlaubstageZeitraum()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

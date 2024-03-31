import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
from PyQt5.QtGui import QFont
import mysql.connector

class UrlaubstageMitarbeiterZuordnung(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Label und Textfeld für Urlaubstage-ID
        self.label_urlaubstage_id = QLabel('Urlaubstage-ID:')
        self.label_urlaubstage_id.setFont(QFont('Arial', 12, QFont.Bold))
        self.input_urlaubstage_id = QLineEdit()
        layout.addWidget(self.label_urlaubstage_id)
        layout.addWidget(self.input_urlaubstage_id)

        # Label und Textfeld für Mitarbeiter-ID
        self.label_mitarbeiter_id = QLabel('Mitarbeiter-ID:')
        self.label_mitarbeiter_id.setFont(QFont('Arial', 12, QFont.Bold))
        self.input_mitarbeiter_id = QLineEdit()
        layout.addWidget(self.label_mitarbeiter_id)
        layout.addWidget(self.input_mitarbeiter_id)

        # Speichern-Button
        self.button_save = QPushButton('Speichern')
        self.button_save.clicked.connect(self.save_data)
        layout.addWidget(self.button_save)

        self.setLayout(layout)
        self.setWindowTitle('Urlaubstage-Mitarbeiter Zuordnung')

    def save_data(self):
        urlaubstage_id = self.input_urlaubstage_id.text()
        mitarbeiter_id = self.input_mitarbeiter_id.text()

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
            INSERT INTO urlaubstage_has_mitarbeiter (Urlaubstage_id_Urlaubstage, mitarbeiter_id_Mitarbeiter)
            VALUES (%s, %s)
        ''', (urlaubstage_id, mitarbeiter_id))

        conn.commit()
        cursor.close()
        conn.close()

        # Bestätigung anzeigen
        self.button_save.setText('Gespeichert!')

def main(app):    
    ex = UrlaubstageMitarbeiterZuordnung()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

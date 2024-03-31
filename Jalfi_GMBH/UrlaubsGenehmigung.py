import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
from PyQt5.QtGui import QFont
import mysql.connector

class UrlaubstageStatusErfassung(QWidget):
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

        # Label und Textfeld für Urlaubsstatus-ID
        self.label_urlaubs_status_id = QLabel('Urlaubsstatus-ID:')
        self.label_urlaubs_status_id.setFont(QFont('Arial', 12, QFont.Bold))
        self.input_urlaubs_status_id = QLineEdit()
        layout.addWidget(self.label_urlaubs_status_id)
        layout.addWidget(self.input_urlaubs_status_id)

        # Speichern-Button
        self.button_save = QPushButton('Speichern')
        self.button_save.clicked.connect(self.save_data)
        layout.addWidget(self.button_save)

        self.setLayout(layout)
        self.setWindowTitle('Urlaubstage Status Erfassung')

    def save_data(self):
        urlaubstage_id = self.input_urlaubstage_id.text()
        urlaubs_status_id = self.input_urlaubs_status_id.text()

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
            INSERT INTO urlaubstage_has_urlaubs_status (Urlaubstage_id_Urlaubstage, Urlaubs_Status_id_Urlaubs_Status)
            VALUES (%s, %s)
        ''', (urlaubstage_id, urlaubs_status_id))

        conn.commit()
        cursor.close()
        conn.close()

        # Bestätigung anzeigen
        self.button_save.setText('Gespeichert!')

def main(app):    
    ex = UrlaubstageStatusErfassung()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

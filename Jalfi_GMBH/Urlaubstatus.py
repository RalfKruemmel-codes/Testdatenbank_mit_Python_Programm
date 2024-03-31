import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QCheckBox
from PyQt5.QtGui import QFont
import mysql.connector

class UrlaubsStatusErfassung(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Label und Textfeld für Urlaubsstatus-ID
        self.label_id = QLabel('Urlaubsstatus-ID:')
        self.label_id.setFont(QFont('Arial', 12, QFont.Bold))
        self.input_id = QLineEdit()
        layout.addWidget(self.label_id)
        layout.addWidget(self.input_id)

        # Checkboxen für genehmigt, abgelehnt, beantragt
        self.checkbox_genehmigt = QCheckBox('Genehmigt')
        self.checkbox_genehmigt.setFont(QFont('Arial', 12, QFont.Bold))
        layout.addWidget(self.checkbox_genehmigt)

        self.checkbox_abgelehnt = QCheckBox('Abgelehnt')
        self.checkbox_abgelehnt.setFont(QFont('Arial', 12, QFont.Bold))
        layout.addWidget(self.checkbox_abgelehnt)

        self.checkbox_beantragt = QCheckBox('Beantragt')
        self.checkbox_beantragt.setFont(QFont('Arial', 12, QFont.Bold))
        layout.addWidget(self.checkbox_beantragt)

        # Speichern-Button
        self.button_save = QPushButton('Speichern')
        self.button_save.clicked.connect(self.save_data)
        layout.addWidget(self.button_save)

        self.setLayout(layout)
        self.setWindowTitle('Urlaubsstatus hinzufügen')

    def save_data(self):
        id_status = self.input_id.text()
        genehmigt = int(self.checkbox_genehmigt.isChecked())
        abgelehnt = int(self.checkbox_abgelehnt.isChecked())
        beantragt = int(self.checkbox_beantragt.isChecked())

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
            INSERT INTO urlaubs_status (id_Urlaubs_Status, genehmigt, abgelehnt, beantragt)
            VALUES (%s, %s, %s, %s)
        ''', (id_status, genehmigt, abgelehnt, beantragt))

        conn.commit()
        cursor.close()
        conn.close()

        # Bestätigung anzeigen
        self.button_save.setText('Gespeichert!')

def main(app):    
    ex = UrlaubsStatusErfassung()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

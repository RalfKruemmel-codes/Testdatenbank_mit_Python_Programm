import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QDateTimeEdit
from PyQt5.QtGui import QFont
import mysql.connector

class Zeiterfassung(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Label und DateTimeEdit für Arbeitsbeginn
        self.label_arbeitsbeginn = QLabel('Arbeitsbeginn:')
        self.label_arbeitsbeginn.setFont(QFont('Arial', 12, QFont.Bold))
        self.input_arbeitsbeginn = QDateTimeEdit()
        layout.addWidget(self.label_arbeitsbeginn)
        layout.addWidget(self.input_arbeitsbeginn)

        # Label und DateTimeEdit für Frühstückspause Beginn
        self.label_fruehstueck_beginn = QLabel('Frühstückspause Beginn:')
        self.label_fruehstueck_beginn.setFont(QFont('Arial', 12, QFont.Bold))
        self.input_fruehstueck_beginn = QDateTimeEdit()
        layout.addWidget(self.label_fruehstueck_beginn)
        layout.addWidget(self.input_fruehstueck_beginn)

        # Label und DateTimeEdit für Frühstückspause Ende
        self.label_fruehstueck_ende = QLabel('Frühstückspause Ende:')
        self.label_fruehstueck_ende.setFont(QFont('Arial', 12, QFont.Bold))
        self.input_fruehstueck_ende = QDateTimeEdit()
        layout.addWidget(self.label_fruehstueck_ende)
        layout.addWidget(self.input_fruehstueck_ende)

        # Label und DateTimeEdit für Mittagspause Beginn
        self.label_mittagspause_beginn = QLabel('Mittagspause Beginn:')
        self.label_mittagspause_beginn.setFont(QFont('Arial', 12, QFont.Bold))
        self.input_mittagspause_beginn = QDateTimeEdit()
        layout.addWidget(self.label_mittagspause_beginn)
        layout.addWidget(self.input_mittagspause_beginn)

        # Label und DateTimeEdit für Mittagspause Ende
        self.label_mittagspause_ende = QLabel('Mittagspause Ende:')
        self.label_mittagspause_ende.setFont(QFont('Arial', 12, QFont.Bold))
        self.input_mittagspause_ende = QDateTimeEdit()
        layout.addWidget(self.label_mittagspause_ende)
        layout.addWidget(self.input_mittagspause_ende)

        # Label und DateTimeEdit für Arbeitsende
        self.label_arbeitsende = QLabel('Arbeitsende:')
        self.label_arbeitsende.setFont(QFont('Arial', 12, QFont.Bold))
        self.input_arbeitsende = QDateTimeEdit()
        layout.addWidget(self.label_arbeitsende)
        layout.addWidget(self.input_arbeitsende)

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
        self.setWindowTitle('Mitarbeiter Zeiterfassung')

    def save_data(self):
        arbeitsbeginn = self.input_arbeitsbeginn.dateTime().toString('yyyy-MM-dd HH:mm:ss')
        fruehstueck_beginn = self.input_fruehstueck_beginn.dateTime().toString('yyyy-MM-dd HH:mm:ss')
        fruehstueck_ende = self.input_fruehstueck_ende.dateTime().toString('yyyy-MM-dd HH:mm:ss')
        mittagspause_beginn = self.input_mittagspause_beginn.dateTime().toString('yyyy-MM-dd HH:mm:ss')
        mittagspause_ende = self.input_mittagspause_ende.dateTime().toString('yyyy-MM-dd HH:mm:ss')
        arbeitsende = self.input_arbeitsende.dateTime().toString('yyyy-MM-dd HH:mm:ss')
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
            INSERT INTO stempeluhr (id_Stempeluhr, Arbeitsbeginn, Frühstückspause_Beginn, Frühstückspause_Ende, Mittagspause_Beginn, Mittagspause_Ende, Arbeitsende, Mitarbeiter_id_Mitarbeiter)
            VALUES (NULL, %s, %s, %s, %s, %s, %s, %s)
        ''', (arbeitsbeginn, fruehstueck_beginn, fruehstueck_ende, mittagspause_beginn, mittagspause_ende, arbeitsende, mitarbeiter_id))

        conn.commit()
        cursor.close()
        conn.close()

        # Bestätigung anzeigen
        self.button_save.setText('Gespeichert!')


def main(app):    
    ex = Zeiterfassung()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
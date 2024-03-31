import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QFileDialog, QLineEdit
from PyQt5.QtGui import QFont
import mysql.connector
import datetime
import os

class DokumentUploader(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Label und Button für das Hochladen des Dokuments
        self.label_dokument = QLabel('Dokument:')
        self.label_dokument.setFont(QFont('Arial', 12, QFont.Bold))
        self.button_upload = QPushButton('Dokument auswählen und hochladen')
        self.button_upload.setFont(QFont('Arial', 12, QFont.Bold))
        self.button_upload.clicked.connect(self.upload_document)
        layout.addWidget(self.label_dokument)
        layout.addWidget(self.button_upload)

        # Label und Textfeld für Mitarbeiter-ID
        self.label_mitarbeiter_id = QLabel('Mitarbeiter-ID:')
        self.label_mitarbeiter_id.setFont(QFont('Arial', 12, QFont.Bold))
        self.input_mitarbeiter_id = QLineEdit()
        layout.addWidget(self.label_mitarbeiter_id)
        layout.addWidget(self.input_mitarbeiter_id)

        # Label und Textfeld für Dokumentenart-ID
        self.label_dokumentenart_id = QLabel('Dokumentenart-ID:')
        self.label_dokumentenart_id.setFont(QFont('Arial', 12, QFont.Bold))
        self.input_dokumentenart_id = QLineEdit()
        layout.addWidget(self.label_dokumentenart_id)
        layout.addWidget(self.input_dokumentenart_id)

        self.setLayout(layout)
        self.setWindowTitle('Dokument Uploader')

    def upload_document(self):
        # Dateiauswahldialog öffnen
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "Dokument auswählen", "",
                                                  "Alle Dateien (*);;PDF Dateien (*.pdf);;Text Dateien (*.txt)", options=options)
        if fileName:
            # Verbindung zur Datenbank herstellen
            conn = mysql.connector.connect(
                host='localhost',
                user='root',
                password='1234',
                database='kruemmel'
            )
            cursor = conn.cursor()

            # Datei lesen
            with open(fileName, 'rb') as file:
                binary_data = file.read()

            # Dokumenteninformationen erfassen
            dokumentenname = os.path.basename(fileName)
            dokumententyp = os.path.splitext(fileName)[1]
            hochladedatum = datetime.datetime.now()
            mitarbeiter_id = self.input_mitarbeiter_id.text()
            dokumentenart_id = self.input_dokumentenart_id.text()

            # Daten in die Datenbank einfügen
            cursor.execute('''
                INSERT INTO mitarbeiterdokumente (Dokument, Dokumentenname, Dokumententyp, Hochladedatum, mitarbeiter_id_Mitarbeiter, dokumentenarten_id_Dokumentenart)
                VALUES (%s, %s, %s, %s, %s, %s)
            ''', (binary_data, dokumentenname, dokumententyp, hochladedatum, mitarbeiter_id, dokumentenart_id))

            conn.commit()
            cursor.close()
            conn.close()

            # Bestätigung anzeigen
            self.button_upload.setText('Dokument hochgeladen!')

def main(app):    
    ex = DokumentUploader()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
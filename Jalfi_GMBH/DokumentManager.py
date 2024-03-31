import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QFileDialog, QLineEdit, QMessageBox
from PyQt5.QtGui import QFont
import mysql.connector
import datetime

class DokumentManager(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Label und Textfeld für Mitarbeiter-ID
        self.label_mitarbeiter_id = QLabel('Mitarbeiter-ID:')
        self.label_mitarbeiter_id.setFont(QFont('Arial', 12, QFont.Bold))
        self.input_mitarbeiter_id = QLineEdit()
        layout.addWidget(self.label_mitarbeiter_id)
        layout.addWidget(self.input_mitarbeiter_id)

        self.label_dokumentenart_id = QLabel('Dokumentenart-ID:')
        self.label_dokumentenart_id.setFont(QFont('Arial', 12, QFont.Bold))
        self.input_dokumentenart_id = QLineEdit()
        layout.addWidget(self.label_dokumentenart_id)
        layout.addWidget(self.input_dokumentenart_id)

        # Label und Button für das Hochladen des Dokuments
        self.label_upload = QLabel('Dokument hochladen:')
        self.label_upload.setFont(QFont('Arial', 12, QFont.Bold))
        self.button_upload = QPushButton('Datei auswählen')
        self.button_upload.setFont(QFont('Arial', 12))
        self.button_upload.clicked.connect(self.upload_document)
        layout.addWidget(self.label_upload)
        layout.addWidget(self.button_upload)

        # Label und Button für das Herunterladen des Dokuments
        self.label_download = QLabel('Dokument herunterladen:')
        self.label_download.setFont(QFont('Arial', 12, QFont.Bold))
        self.input_id = QLineEdit('Dokument-ID eingeben')
        self.input_id.setFont(QFont('Arial', 12))
        self.button_download = QPushButton('Dokument herunterladen')
        self.button_download.setFont(QFont('Arial', 12))
        self.button_download.clicked.connect(self.download_document)
        layout.addWidget(self.label_download)
        layout.addWidget(self.input_id)
        layout.addWidget(self.button_download)

        self.setLayout(layout)
        self.setWindowTitle('Dokument Manager')

    def upload_document(self):
        # Dateiauswahldialog öffnen
        options = QFileDialog.Options()
        filePath, _ = QFileDialog.getOpenFileName(self, "Dokument auswählen", "", "Alle Dateien (*);;", options=options)
        if filePath:
            # Datei lesen
            with open(filePath, 'rb') as file:
                binary_data = file.read()

            # Mitarbeiter-ID aus dem Eingabefeld holen
            mitarbeiter_id = self.input_mitarbeiter_id.text()
            if not mitarbeiter_id.isdigit():
                QMessageBox.warning(self, 'Fehler', 'Bitte geben Sie eine gültige Mitarbeiter-ID ein.')
                return

            # Datenbankverbindung herstellen
            conn = mysql.connector.connect(
                host='localhost',
                user='root',
                password='1234',
                database='kruemmel'
            )
            cursor = conn.cursor()

            # Dokumententyp festlegen
            dokumententyp = os.path.splitext(filePath)[1] if os.path.splitext(filePath)[1] else 'application/pdf'
            # Dokumentenart-ID aus dem Eingabefeld holen oder Standardwert setzen
            dokumentenart_id = self.input_dokumentenart_id.text() if self.input_dokumentenart_id.text() else 'DEIN_STANDARDWERT'
            # Daten in die Datenbank einfügen
     # Daten in die Datenbank einfügen
            try:
                cursor.execute('''
                    INSERT INTO mitarbeiterdokumente (Dokument, Dokumentenname, Dokumententyp, Hochladedatum, mitarbeiter_id_Mitarbeiter, dokumentenarten_id_Dokumentenart)
                    VALUES (%s, %s, %s, NOW(), %s, %s)
                ''', (binary_data, os.path.basename(filePath), dokumententyp, mitarbeiter_id, dokumentenart_id))
                conn.commit()
                QMessageBox.information(self, 'Erfolg', 'Das Dokument wurde erfolgreich hochgeladen.')
            except mysql.connector.Error as err:
                QMessageBox.warning(self, 'Fehler', f'Ein Fehler ist aufgetreten: {err}')
            finally:
                cursor.close()
                conn.close()

    def download_document(self):
        dokument_id = self.input_id.text()
        if not dokument_id.isdigit():
            QMessageBox.warning(self, 'Fehler', 'Bitte geben Sie eine gültige Dokument-ID ein.')
            return

        # Datenbankverbindung herstellen
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='1234',
            database='kruemmel'
        )
        cursor = conn.cursor()

        # Dokument aus der Datenbank abrufen
        try:
            cursor.execute('SELECT Dokument, Dokumentenname FROM mitarbeiterdokumente WHERE id_Dokument = %s', (dokument_id,))
            result = cursor.fetchone()
            if result:
                # Speicherort auswählen
                options = QFileDialog.Options()
                save_path, _ = QFileDialog.getSaveFileName(self, "Dokument speichern unter", result[1], "Alle Dateien (*);;", options=options)
                if save_path:
                    # Dokument speichern
                    with open(save_path, 'wb') as file:
                        file.write(result[0])
                    QMessageBox.information(self, 'Erfolg', 'Das Dokument wurde erfolgreich heruntergeladen.')
            else:
                QMessageBox.warning(self, 'Fehler', 'Dokument nicht gefunden.')
        except mysql.connector.Error as err:
            QMessageBox.warning(self, 'Fehler', f'Ein Fehler ist aufgetreten: {err}')
        finally:
            cursor.close()
            conn.close()


def main(app):    
    ex = DokumentManager()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
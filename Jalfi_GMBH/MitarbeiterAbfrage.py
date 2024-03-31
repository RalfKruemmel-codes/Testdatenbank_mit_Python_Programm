import sys
import mysql.connector
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QLineEdit, QPushButton, QMessageBox, QScrollArea, QLabel)

class MitarbeiterDatenbank(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout(self)

        # Suchfelder
        self.nachnameLineEdit = QLineEdit(self)
        self.nachnameLineEdit.setPlaceholderText('Nachname')
        layout.addWidget(self.nachnameLineEdit)

        self.vornameLineEdit = QLineEdit(self)
        self.vornameLineEdit.setPlaceholderText('Vorname')
        layout.addWidget(self.vornameLineEdit)

        # Suchbutton
        self.suchButton = QPushButton('Suchen', self)
        self.suchButton.clicked.connect(self.sucheMitarbeiter)
        layout.addWidget(self.suchButton)

        # Tabelle
        self.tableWidget = QTableWidget(self)
        self.tableWidget.itemClicked.connect(self.zeigeZeitenFuerMitarbeiter)
        layout.addWidget(self.tableWidget)

        self.setLayout(layout)
        self.setWindowTitle('Mitarbeiter Datenbank')
        self.setGeometry(300, 300, 620, 450)
        self.show()

    def sucheMitarbeiter(self):
        nachname = self.nachnameLineEdit.text()
        vorname = self.vornameLineEdit.text()

        query = "SELECT * FROM mitarbeiter WHERE Name LIKE %s AND Vorname LIKE %s"
        values = ('%' + nachname + '%', '%' + vorname + '%')

        conn = mysql.connector.connect(host='localhost', user='root', password='1234', database='kruemmel')
        cursor = conn.cursor()
        cursor.execute(query, values)
        results = cursor.fetchall()

        self.anzeigenErgebnisse(results)
        cursor.close()
        conn.close()

    def anzeigenErgebnisse(self, results):
        self.tableWidget.setRowCount(0)
        if results:
            self.tableWidget.setColumnCount(len(results[0]))
            self.tableWidget.setHorizontalHeaderLabels(['ID', 'Name', 'Beruf.Bez.', 'Vorname', 'Adresse', 'Telefonnummer', 'E-Mail', 'Gehalt', 'Einstellungsdatum', 'Geburtsdatum', 'Sozialversicherungsnummer', 'Krankenkasse', 'Nächster Angehörige', 'Notfall-Telefonnummer', 'Abteilungs-ID', 'Team-ID'])

            for row_number, row_data in enumerate(results):
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        else:
            # Keine Ergebnisse gefunden, setzen Sie die Spaltenanzahl auf 0 oder auf die Anzahl der Header
            self.tableWidget.setColumnCount(len(['ID', 'Name', 'Beruf.Bez.', 'Vorname', 'Adresse', 'Telefonnummer', 'E-Mail', 'Gehalt', 'Einstellungsdatum', 'Geburtsdatum', 'Sozialversicherungsnummer', 'Krankenkasse', 'Nächster Angehörige', 'Notfall-Telefonnummer', 'Abteilungs-ID', 'Team-ID']))
            QMessageBox.information(self, 'Information', 'Keine Ergebnisse gefunden.')


    def zeigeZeitenFuerMitarbeiter(self, item):
        mitarbeiter_id = self.tableWidget.item(item.row(), 0).text()
        self.zeigeMitarbeiterZeiten(mitarbeiter_id)

    def zeigeMitarbeiterZeiten(self, mitarbeiter_id):
        query = "SELECT * FROM stempeluhr WHERE Mitarbeiter_id_Mitarbeiter = %s"
        values = (mitarbeiter_id,)

        conn = mysql.connector.connect(host='localhost', user='root', password='1234', database='kruemmel')
        cursor = conn.cursor()
        cursor.execute(query, values)
        results = cursor.fetchall()

        if results:
            zeiten_text = '\n'.join(['Arbeitsbeginn: ' + str(result[1]) + ', Arbeitsende: ' + str(result[6]) for result in results])
            self.zeitenFenster = ZeitenFenster(zeiten_text)
        else:
            QMessageBox.information(self, 'Information', 'Keine Zeiten für diesen Mitarbeiter gefunden.')

        cursor.close()
        conn.close()

class ZeitenFenster(QWidget):
    def __init__(self, zeiten):
        super().__init__()
        self.initUI(zeiten)

    def initUI(self, zeiten):
        layout = QVBoxLayout(self)

        zeitenLabel = QLabel(zeiten, self)
        zeitenLabel.setWordWrap(True)
        zeitenLabel.setStyleSheet("font: 13pt Arial;")  # Setzen der Schriftgröße und des Schriftstils

        scrollArea = QScrollArea(self)
        scrollArea.setWidgetResizable(True)
        scrollArea.setWidget(zeitenLabel)

        layout.addWidget(scrollArea)
        self.setLayout(layout)
        self.setWindowTitle('Arbeitszeiten')
        self.setGeometry(100, 100, 400, 300)
        self.show()

def main():
    app = QApplication(sys.argv)
    ex = MitarbeiterDatenbank()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

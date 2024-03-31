import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QComboBox, QLabel, QVBoxLayout, QWidget, 
                             QTableWidget, QTableWidgetItem, QMessageBox)
from PyQt5.QtCore import Qt
import mysql.connector

class DatenAnzeige(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Datenbank Viewer')
        # MySQL Verbindungseinstellungen
        self.db = mysql.connector.connect(
            host='localhost',
            user='root',
            password='1234',
            database='kruemmel'
        )
        # Haupt-Widget und Layout
        self.main_widget = QWidget(self)
        self.setCentralWidget(self.main_widget)
        self.layout = QVBoxLayout()
        self.main_widget.setLayout(self.layout)
        # Dropdown-Menü für Tabellenauswahl
        self.table_select = QComboBox()
        self.table_select.addItems(['projekte', 'abteilungen', 'dokumentenarten', 'führungskräfte', 
                                    'teams', 'urlaubs_status', 'urlaubstage'])
        self.table_select.currentIndexChanged.connect(self.show_table_data)
        self.layout.addWidget(self.table_select)
        # Tabelle für die Anzeige der Daten
        self.data_table = QTableWidget()
        self.data_table.cellClicked.connect(self.on_cell_click)
        self.layout.addWidget(self.data_table)
        # Zeige die Daten der ersten Tabelle an
        self.show_table_data(0)

    def show_table_data(self, index):
        table_name = self.table_select.itemText(index)
        cursor = self.db.cursor()
        cursor.execute(f'SELECT * FROM {table_name}')
        rows = cursor.fetchall()
        column_names = [i[0] for i in cursor.description]
        cursor.close()
        # Tabelle vorbereiten
        self.data_table.clear()
        self.data_table.setColumnCount(len(column_names))
        self.data_table.setRowCount(len(rows))
        self.data_table.setHorizontalHeaderLabels(column_names)
        self.data_table.verticalHeader().setVisible(False)
        # Daten in die Tabelle einfügen
        for row_num, row_data in enumerate(rows):
            for column_num, data in enumerate(row_data):
                self.data_table.setItem(row_num, column_num, QTableWidgetItem(str(data)))
        # Stil der Tabelle
        self.data_table.setStyleSheet('font-family: Arial; font-size: 16px;')

    def on_cell_click(self, row, column):
        if self.table_select.currentText() == 'projekte':
            projekt_id = self.data_table.item(row, 0).text()
            cursor = self.db.cursor()
            cursor.execute(f"""
                SELECT p.name, p.startdatum, p.enddatum, 
                       m.id_Mitarbeiter, m.Vorname, m.Name AS Nachname, 
                       GROUP_CONCAT(m2.id_Mitarbeiter SEPARATOR ', ') AS Mitarbeiter_IDs,
                       GROUP_CONCAT(m2.Vorname SEPARATOR ', ') AS Mitarbeiter_Vornamen,
                       GROUP_CONCAT(m2.Name SEPARATOR ', ') AS Mitarbeiter_Nachnamen
                FROM projekte p 
                LEFT JOIN mitarbeiter m ON p.id_Projektleiter = m.id_Mitarbeiter 
                LEFT JOIN projektmitarbeiter pm ON p.id_Projekt = pm.id_Projekt 
                LEFT JOIN mitarbeiter m2 ON pm.id_Mitarbeiter = m2.id_Mitarbeiter 
                WHERE p.id_Projekt = {projekt_id}
                GROUP BY p.id_Projekt
            """)
            details = cursor.fetchone()
            cursor.close()
            if details:
                message = (f'Projektname: {details[0]}, Startdatum: {details[1]}, Enddatum: {details[2]}, '
                           f'Projektleiter ID: {details[3]}, Projektleiter Vorname: {details[4]}, Projektleiter Nachname: {details[5]}, '
                           f'Mitarbeiter IDs: {details[6]}, Mitarbeiter Vornamen: {details[7]}, Mitarbeiter Nachnamen: {details[8]}')
                QMessageBox.information(self, 'Projektdetails', message)
            else:
                QMessageBox.information(self, 'Projektdetails', 'Keine Details verfügbar.')

def main(app):    
    ex = DatenAnzeige()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

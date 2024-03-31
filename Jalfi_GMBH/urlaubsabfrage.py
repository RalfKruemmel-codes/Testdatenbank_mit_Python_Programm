import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QComboBox, QWidget, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import Qt
import mysql.connector

class UrlaubstageAbfrage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Urlaubstage Verwaltung')
        self.setGeometry(100, 100, 800, 600)
        
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        self.status_label = QLabel('Status:', self)
        self.status_label.setStyleSheet('font-family: Arial; font-size: 13px;')
        layout.addWidget(self.status_label)

        self.status_combo = QComboBox(self)
        self.status_combo.addItem('Alle')
        self.status_combo.addItem('Genehmigt')
        self.status_combo.addItem('Abgelehnt')
        self.status_combo.addItem('Beantragt')
        self.status_combo.currentIndexChanged.connect(self.update_display)
        layout.addWidget(self.status_combo)

        self.table_widget = QTableWidget(self)
        self.table_widget.setColumnCount(4)
        self.table_widget.setHorizontalHeaderLabels(['ID', 'Mitarbeitername', 'Status', 'Kommentar'])
        layout.addWidget(self.table_widget)

        self.db_connect()
        self.update_display()

    def db_connect(self):
        try:
            self.conn = mysql.connector.connect(
                host='localhost',
                user='root',
                password='1234',
                database='kruemmel'
            )
            self.cursor = self.conn.cursor()
        except mysql.connector.Error as e:
            self.result_label.setText(f'Datenbankverbindung fehlgeschlagen: {e}')

    def update_display(self):
        status = self.status_combo.currentText()
        query = "SELECT u.id_Urlaubstage, m.Name, CASE WHEN s.genehmigt = 1 THEN 'Genehmigt' WHEN s.abgelehnt = 1 THEN 'Abgelehnt' WHEN s.beantragt = 1 THEN 'Beantragt' END AS Status, u.Kommentar FROM urlaubstage u JOIN urlaubstage_has_mitarbeiter um ON u.id_Urlaubstage = um.Urlaubstage_id_Urlaubstage JOIN mitarbeiter m ON um.mitarbeiter_id_Mitarbeiter = m.id_Mitarbeiter JOIN urlaubstage_has_urlaubs_status us ON u.id_Urlaubstage = us.Urlaubstage_id_Urlaubstage JOIN urlaubs_status s ON us.Urlaubs_Status_id_Urlaubs_Status = s.id_Urlaubs_Status"
        if status != 'Alle':
            query += f" WHERE s.{status.lower()} = 1"

        try:
            self.cursor.execute(query)
            results = self.cursor.fetchall()
            self.table_widget.setRowCount(len(results))
            for row_number, row_data in enumerate(results):
                for column_number, data in enumerate(row_data):
                    self.table_widget.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        except mysql.connector.Error as e:
            self.result_label.setText(f'Fehler beim Abrufen der Daten: {e}')

def main(app):    
    ex = UrlaubstageAbfrage()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

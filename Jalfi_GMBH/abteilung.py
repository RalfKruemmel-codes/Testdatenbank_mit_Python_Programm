import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout

import mysql.connector

class DatenErfassung(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.label = QLabel('Name der Abteiung hinzufügen')
        self.label.setStyleSheet('font: bold 12pt "Arial"')
        
        self.nameEdit = QLineEdit()
        self.saveButton = QPushButton('Speichern')
        self.saveButton.clicked.connect(self.saveData)
        
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.nameEdit)
        layout.addWidget(self.saveButton)
        
        self.setLayout(layout)
        self.setWindowTitle('Daten Erfassung')
        self.show()

    def saveData(self):
        name = self.nameEdit.text()
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='1234',
            database='kruemmel'
        )
        cursor = conn.cursor()
        cursor.execute('INSERT INTO abteilungen (Name) VALUES (%s)', (name,))
        conn.commit()
        cursor.close()
        conn.close()
        self.nameEdit.clear()

def main(app):
    # Dein Code hier, aber ohne app = QApplication(sys.argv) und sys.exit(app.exec_())
    ex = DatenErfassung()
    ex.show()
if __name__ == '__main__':
    main()
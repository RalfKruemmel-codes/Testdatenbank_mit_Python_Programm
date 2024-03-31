import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout, QLabel
import mysql.connector
from mysql.connector import Error

class MitarbeiterPasswortVerwaltung(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.label = QLabel('Mitarbeiter-ID:')
        self.mitarbeiter_id = QLineEdit(self)
        self.passwort_label = QLabel('Neues Passwort:')
        self.mitarbeiter_passwort = QLineEdit(self)
        self.mitarbeiter_passwort.setEchoMode(QLineEdit.Password)
        self.button = QPushButton('Passwort aktualisieren', self)
        self.button.clicked.connect(self.update_passwort)
        
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.mitarbeiter_id)
        layout.addWidget(self.passwort_label)
        layout.addWidget(self.mitarbeiter_passwort)
        layout.addWidget(self.button)
        
        self.setLayout(layout)
        self.setWindowTitle('Passwort Verwaltung')
        self.show()
    
    def update_passwort(self):
        mitarbeiter_id = self.mitarbeiter_id.text()
        neues_passwort = self.mitarbeiter_passwort.text()
        # Hier sollten Sie das Passwort hashen, bevor Sie es in die Datenbank einfügen.
        
        try:
            connection = mysql.connector.connect(
                host='localhost',
                database='kruemmel',
                user='root',
                password='1234'
            )
            if connection.is_connected():
                db_Info = connection.get_server_info()
                print("Verbunden mit MySQL Server version ", db_Info)
                cursor = connection.cursor()
                cursor.execute(f"UPDATE mitarbeiter SET MitarbeiterPasswort = '{neues_passwort}' WHERE id_Mitarbeiter = {mitarbeiter_id};")
                connection.commit()
                print("Passwort aktualisiert.")
                
        except Error as e:
            print("Fehler beim Verbinden zu MySQL", e)
        finally:
            if (connection.is_connected()):
                cursor.close()
                connection.close()
                print("MySQL Verbindung ist geschlossen")

def main(app):    
    ex = MitarbeiterPasswortVerwaltung()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

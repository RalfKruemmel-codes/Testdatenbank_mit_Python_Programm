import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout, QLabel, QSizePolicy
from mysql.connector import connect, Error
from PyQt5.QtGui import QFont


class MitarbeiterErfassung(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()   
       

    def initUI(self):
        # Setzen Sie die Startgröße der GUI
        # self.resize(650, 650)
        # Maximieren Sie das Fenster beim Start
        self.showMaximized()

        # Stellen Sie die Größenpolitik ein, um das Mitwachsen zu ermöglichen
        # sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        # self.setSizePolicy(sizePolicy)

        # Erstellen Sie Labels für jedes Feld 
        self.label_Ueberschrift = QLabel('Neue Mitarbeiter erfassen', self)
        self.label_Ueberschrift.setFont(QFont('Arial', 16))       
        self.label_id_Mitarbeiter = QLabel('Mitarbeiter ID:', self)
        self.label_id_Mitarbeiter.setFont(QFont('Arial', 12))
        self.label_Name = QLabel('Name:', self)
        self.label_Name.setFont(QFont('Arial', 12))
        self.label_Abteilung = QLabel('Beruf.Bez.:', self)
        self.label_Abteilung.setFont(QFont('Arial', 12))
        self.label_Vorname = QLabel('Vorname:', self)
        self.label_Vorname.setFont(QFont('Arial', 12))
        self.label_Adresse = QLabel('Adresse:', self)
        self.label_Adresse.setFont(QFont('Arial', 12))
        self.label_Telefonnummer = QLabel('Telefonnummer:', self)
        self.label_Telefonnummer.setFont(QFont('Arial', 12))
        self.label_EMail = QLabel('E-Mail:', self)
        self.label_EMail.setFont(QFont('Arial', 12))
        self.label_Gehalt = QLabel('Gehalt:', self)
        self.label_Gehalt.setFont(QFont('Arial', 12))
        self.label_Einstellungsdatum = QLabel('Einstellungsdatum:', self)
        self.label_Einstellungsdatum.setFont(QFont('Arial', 12))
        self.label_Geburtsdatum = QLabel('Geburtsdatum:', self)
        self.label_Geburtsdatum.setFont(QFont('Arial', 12))
        self.label_Sozialversicherungsnummer = QLabel('Sozialversicherungsnummer:', self)
        self.label_Sozialversicherungsnummer.setFont(QFont('Arial', 12))
        self.label_Krankenkasse = QLabel('Krankenkasse:', self)
        self.label_Krankenkasse.setFont(QFont('Arial', 12))
        self.label_nächster_Angehörige = QLabel('Nächster Angehörige:', self)
        self.label_nächster_Angehörige.setFont(QFont('Arial', 12))
        self.label_Notfall_Telefonnummer = QLabel('Notfall-Telefonnummer:', self)
        self.label_Notfall_Telefonnummer.setFont(QFont('Arial', 12))
        self.label_id_Abteilung = QLabel('ID Abteilung:', self)
        self.label_id_Abteilung.setFont(QFont('Arial', 12))
        self.label_id_Team = QLabel('ID Team:', self)
        self.label_id_Team.setFont(QFont('Arial', 12))
        
        # Erstellen Sie QLineEdit für jedes Feld
        self.id_Mitarbeiter = QLineEdit(self)
        self.Name = QLineEdit(self)
        self.Abteilung = QLineEdit(self)
        self.Vorname = QLineEdit(self)
        self.Adresse = QLineEdit(self)
        self.Telefonnummer = QLineEdit(self)
        self.EMail = QLineEdit(self)
        self.Gehalt = QLineEdit(self)
        self.Einstellungsdatum = QLineEdit(self)
        self.Geburtsdatum = QLineEdit(self)
        self.Sozialversicherungsnummer = QLineEdit(self)
        self.Krankenkasse = QLineEdit(self)
        self.nächster_Angehörige = QLineEdit(self)
        self.Notfall_Telefonnummer = QLineEdit(self)
        self.id_Abteilung = QLineEdit(self)
        self.id_Team = QLineEdit(self)
        
        # Fügen Sie die Widgets zum Layout hinzu
        layout = QVBoxLayout()
        layout.addWidget(self.label_Ueberschrift)
        layout.addWidget(self.label_id_Mitarbeiter)
        layout.addWidget(self.id_Mitarbeiter)
        layout.addWidget(self.label_Name)
        layout.addWidget(self.Name)
        layout.addWidget(self.label_Abteilung)
        layout.addWidget(self.Abteilung)
        layout.addWidget(self.label_Vorname)
        layout.addWidget(self.Vorname)
        layout.addWidget(self.label_Adresse)
        layout.addWidget(self.Adresse)
        layout.addWidget(self.label_Telefonnummer)
        layout.addWidget(self.Telefonnummer)
        layout.addWidget(self.label_EMail)
        layout.addWidget(self.EMail)
        layout.addWidget(self.label_Gehalt)
        layout.addWidget(self.Gehalt)
        layout.addWidget(self.label_Einstellungsdatum)
        layout.addWidget(self.Einstellungsdatum)
        layout.addWidget(self.label_Geburtsdatum)
        layout.addWidget(self.Geburtsdatum)
        layout.addWidget(self.label_Sozialversicherungsnummer)
        layout.addWidget(self.Sozialversicherungsnummer)
        layout.addWidget(self.label_Krankenkasse)
        layout.addWidget(self.Krankenkasse)
        layout.addWidget(self.label_nächster_Angehörige)
        layout.addWidget(self.nächster_Angehörige)
        layout.addWidget(self.label_Notfall_Telefonnummer)
        layout.addWidget(self.Notfall_Telefonnummer)
        layout.addWidget(self.label_id_Abteilung)
        layout.addWidget(self.id_Abteilung)
        layout.addWidget(self.label_id_Team)
        layout.addWidget(self.id_Team)
        
        self.submitButton = QPushButton('Daten speichern', self)
        self.submitButton.clicked.connect(self.saveData)
        layout.addWidget(self.submitButton)
        
        self.setLayout(layout)
        self.setWindowTitle('Neue Mitarbeiter erfassen')
    
    def saveData(self):
        data = {
            'id_Mitarbeiter': self.id_Mitarbeiter.text(),
            'Name': self.Name.text(),
            'Beruf.Bez.': self.Abteilung.text(),
            'Vorname': self.Vorname.text(),
            'Adresse': self.Adresse.text(),
            'Telefonnummer': self.Telefonnummer.text(),
            'EMail': self.EMail.text(),
            'Gehalt': self.Gehalt.text(),
            'Einstellungsdatum': self.Einstellungsdatum.text(),
            'Geburtsdatum': self.Geburtsdatum.text(),
            'Sozialversicherungsnummer': self.Sozialversicherungsnummer.text(),
            'Krankenkasse': self.Krankenkasse.text(),
            'nächster_Angehörige': self.nächster_Angehörige.text(),
            'Notfall_Telefonnummer': self.Notfall_Telefonnummer.text(),
            'id_Abteilung': self.id_Abteilung.text(),
            'id_Team': self.id_Team.text(),
            # Fügen Sie hier weitere Datenfelder hinzu
        }
        
        try:
            with connect(
                host="localhost",
                user="root",
                password="1234",
                database="kruemmel",
            ) as connection:
                insert_mitarbeiter_query = """
                INSERT INTO mitarbeiter (
                `id_Mitarbeiter`, `Name`, `Beruf.Bez.`, `Vorname`, `Adresse`, 
                 `Telefonnummer`, `EMail`, `Gehalt`, `Einstellungsdatum`, 
                `Geburtsdatum`, `Sozialversicherungsnummer`, `Krankenkasse`, 
                `nächster_Angehörige`, `Notfall_Telefonnummer`, `id_Abteilung`, `id_Team`
                ) VALUES (
                   %s, %s, %s, %s, %s, 
                 %s, %s, %s, %s, %s, 
                 %s, %s, %s, %s, %s, %s
                )

                """
                cursor = connection.cursor()
                cursor.execute(insert_mitarbeiter_query, tuple(data.values()))
                connection.commit()
        except Error as e:
            print(e)

# In mitarbeiter.py
def main(app):
    # Dein bisheriger Code, der das Fenster initialisiert und anzeigt
    ex = MitarbeiterErfassung()
    ex.show()

if __name__ == '__main__':
    main()

import sys
import abteilung
import mitarbeiter
import fuehrungskraefte
import projekt
import projektMitarbeiter
import zeiterfassung
import teams
import urlaubstageZeitraum
import MitarbeiterUrlaubstageZuordnung
import UrlaubsGenehmigung
import Urlaubstatus
import DokumentUploader
import DokumentManager
import MitarbeiterAbfrage
import mitarb_passwort
import datenanzeige
import urlaubsabfrage
                                
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp, QMenuBar

class Hauptfenster(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.abteilungFenster = None  # Hinzugefügt, um eine dauerhafte Referenz zu halten
        self.mitarbeiterFenster = None  # Hinzugefügt, um eine dauerhafte Referenz zu halten
        self.fuehrungskraefteFenster = None 

    def initUI(self):
        menubar = self.menuBar()
        datenabfrageMenu = menubar.addMenu('Datenabfrage')
        dateiMenu = menubar.addMenu('Datenerfassung')

        MitarbeiterAbfrageAction = QAction('MitarbeiterAbfrage', self)
        MitarbeiterAbfrageAction.triggered.connect(self.MitarbeiterAbfrageOeffnen)  # Methode definieren
        datenabfrageMenu.addAction(MitarbeiterAbfrageAction)

        DatenAnzeigeAction = QAction('Daten Anzeige', self)
        DatenAnzeigeAction.triggered.connect(self.DatenAnzeigeOeffnen)  # Methode definieren
        datenabfrageMenu.addAction(DatenAnzeigeAction)

        UrlaubstageAbfrageAction = QAction('Urlaubstage Abfrage', self)
        UrlaubstageAbfrageAction.triggered.connect(self.UrlaubstageAbfrageOeffnen)  # Methode definieren
        datenabfrageMenu.addAction(UrlaubstageAbfrageAction)

        abteilungAction = QAction('Berufsbezeichnung', self)
        abteilungAction.triggered.connect(self.abteilungOeffnen)
        dateiMenu.addAction(abteilungAction)

        mitarbeiterAction = QAction('Mitarbeiter', self)
        mitarbeiterAction.triggered.connect(self.mitarbeiterOeffnen)
        dateiMenu.addAction(mitarbeiterAction)
                                                                 
        mitarb_passwortAction = QAction('Mitarbeiter Passwort Verwaltung', self)
        mitarb_passwortAction.triggered.connect(self.mitarb_passwortOeffnen)
        dateiMenu.addAction(mitarb_passwortAction)

        fuehrungskraefteAction = QAction('Führungskräfte', self)
        fuehrungskraefteAction.triggered.connect(self.fuehrungskraefteOeffnen)
        dateiMenu.addAction(fuehrungskraefteAction)

        projektAction = QAction('Projekt', self)
        projektAction.triggered.connect(self.projektOeffnen)
        dateiMenu.addAction(projektAction)

        projektMitarbeiterAction = QAction('Projekt Mitarbeiter', self)
        projektMitarbeiterAction.triggered.connect(self.projektMitarbeiterOeffnen)
        dateiMenu.addAction(projektMitarbeiterAction)

        zeiterfassungAction = QAction('Zeiterfassung', self)
        zeiterfassungAction.triggered.connect(self.zeiterfassungOeffnen)
        dateiMenu.addAction(zeiterfassungAction)

        teamsAction = QAction('Team Erfassung', self)
        teamsAction.triggered.connect(self.teamsOeffnen)
        dateiMenu.addAction(teamsAction)

        urlaubstageZeitraumAction = QAction('Urlaubstage Zeitraum Erfassung', self)
        urlaubstageZeitraumAction.triggered.connect(self.urlaubstageZeitraumOeffnen)
        dateiMenu.addAction(urlaubstageZeitraumAction)

        MitarbeiterUrlaubstageZuordnungAction = QAction('Mitarbeiter Urlaubszeitraum Zuordnung', self)
        MitarbeiterUrlaubstageZuordnungAction.triggered.connect(self.MitarbeiterUrlaubstageZuordnungOeffnen)
        dateiMenu.addAction(MitarbeiterUrlaubstageZuordnungAction)

        UrlaubsGenehmigungAction = QAction('Urlaubs Genehmigung', self)
        UrlaubsGenehmigungAction.triggered.connect(self.UrlaubsGenehmigungOeffnen)
        dateiMenu.addAction(UrlaubsGenehmigungAction)

        UrlaubstatusAction = QAction('Urlaubsstatus hinzufügen', self)
        UrlaubstatusAction.triggered.connect(self.UrlaubstatusOeffnen)
        dateiMenu.addAction(UrlaubstatusAction)

        DokumentUploaderAction = QAction('Mitarbeiter Dokumente Upload', self)
        DokumentUploaderAction.triggered.connect(self.DokumentUploaderOeffnen)
        dateiMenu.addAction(DokumentUploaderAction)

        DokumentManagerAction = QAction('Dokument Manager', self)
        DokumentManagerAction.triggered.connect(self.DokumentManagerOeffnen)
        dateiMenu.addAction(DokumentManagerAction)

        beendenAction = QAction('Beenden', self)
        beendenAction.triggered.connect(qApp.quit)
        dateiMenu.addAction(beendenAction)

        self.setWindowTitle('Jalfi GMBH - Hauptmenü')
        self.setGeometry(300, 350, 450, 50)
        self.show()

    def abteilungOeffnen(self):
        self.abteilungFenster = abteilung.DatenErfassung()  # Erstelle eine dauerhafte Referenz
        self.abteilungFenster.show()

    def mitarbeiterOeffnen(self):
        self.mitarbeiterFenster = mitarbeiter.MitarbeiterErfassung()  # Erstelle eine dauerhafte Referenz
        self.mitarbeiterFenster.show()

    def mitarb_passwortOeffnen(self):
        self.mitarb_passwortFenster = mitarb_passwort.MitarbeiterPasswortVerwaltung()  # Erstelle eine dauerhafte Referenz
        self.mitarb_passwortFenster.show()

    def fuehrungskraefteOeffnen(self):
        self.fuehrungskraefteFenster = fuehrungskraefte.FuehrungskraefteErfassung()  # Erstelle eine dauerhafte Referenz
        self.fuehrungskraefteFenster.show()

    def projektOeffnen(self):
        self.projektFenster = projekt.ProjektErfassung()  # Erstelle eine dauerhafte Referenz
        self.projektFenster.show()

    def projektMitarbeiterOeffnen(self):
        self.projektMitarbeiterFenster = projektMitarbeiter.ProjektMitarbeiterErfassen()  # Erstelle eine dauerhafte Referenz
        self.projektMitarbeiterFenster.show()      

    def zeiterfassungOeffnen(self):
        self.zeiterfassungFenster = zeiterfassung.Zeiterfassung()  # Erstelle eine dauerhafte Referenz
        self.zeiterfassungFenster.show()

    def teamsOeffnen(self):
        self.teamsFenster = teams.TeamErfassung()  # Erstelle eine dauerhafte Referenz
        self.teamsFenster.show()

    def urlaubstageZeitraumOeffnen(self):
        self.urlaubstageZeitraumFenster = urlaubstageZeitraum.UrlaubstageZeitraum()  # Erstelle eine dauerhafte Referenz
        self.urlaubstageZeitraumFenster.show()

    def MitarbeiterUrlaubstageZuordnungOeffnen(self):
        self.MitarbeiterUrlaubstageZuordnungFenster = MitarbeiterUrlaubstageZuordnung.UrlaubstageMitarbeiterZuordnung()  # Erstelle eine dauerhafte Referenz
        self.MitarbeiterUrlaubstageZuordnungFenster.show()

    def UrlaubsGenehmigungOeffnen(self):
        self.UrlaubsGenehmigungFenster = UrlaubsGenehmigung.UrlaubstageStatusErfassung()  # Erstelle eine dauerhafte Referenz
        self.UrlaubsGenehmigungFenster.show()

    def UrlaubstatusOeffnen(self):
        self.UrlaubstatusFenster = Urlaubstatus.UrlaubsStatusErfassung()  # Erstelle eine dauerhafte Referenz
        self.UrlaubstatusFenster.show()

    def DokumentUploaderOeffnen(self):
        self.DokumentUploaderFenster = DokumentUploader.DokumentUploader()  # Erstelle eine dauerhafte Referenz
        self.DokumentUploaderFenster.show()
    
    def DokumentManagerOeffnen(self):
        self.DokumentManagerFenster = DokumentManager.DokumentManager()  # Erstelle eine dauerhafte Referenz
        self.DokumentManagerFenster.show()

    def MitarbeiterAbfrageOeffnen(self):
       self.MitarbeiterAbfrageFenster = MitarbeiterAbfrage.MitarbeiterDatenbank()  # Erstelle eine dauerhafte Referenz
       self.MitarbeiterAbfrageFenster.show()

    def DatenAnzeigeOeffnen(self):
       self.DatenAnzeigeFenster = datenanzeige.DatenAnzeige()  # Erstelle eine dauerhafte Referenz
       self.DatenAnzeigeFenster.show()

    def UrlaubstageAbfrageOeffnen(self):
       self.UrlaubstageAbfrageFenster = urlaubsabfrage.UrlaubstageAbfrage()  # Erstelle eine dauerhafte Referenz
       self.UrlaubstageAbfrageFenster.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Hauptfenster()
    sys.exit(app.exec_())  # Starte die Ereignisschleife nur einmal



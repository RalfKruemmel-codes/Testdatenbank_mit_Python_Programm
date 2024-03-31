Dies ist ein kleines Programm um auf die Testdatenbank kruemmel zuzugreifen und Datensätze zu erfassen, abzurufen und zu ändern.
Ich gehe davon aus, dass du bereits weißt, wie man dieses Projekt herunter läd und in Visual Studio oder anderweitig öffnest.

Bitte erst die Datenbank mit dem kruemmel.sql scritp einspielen. Dazu das kruemmel.sql https://github.com/bulatburato/Testdatenbank_mit_Python_Programm/blob/master/Jalfi_GMBH/kruemmel.sql script in MySQL Workbench ausführen.

Das Programm benutzt den

Server = localhost

Benutzer = root

Passwort = 1234

Datenbankname = kruemmel


Sollte bereits ein Server vorliegen kann man das root Passwort per sql script ändern.

ALTER USER 'root'@'localhost' IDENTIFIED BY '1234';

Solltest du ihn komplett neu Aufsetzen, denke daran, dass du dein Passwort für Testzwecke für root auf 
1234 änderst, oder du das Passwort in allen Dateien des Programmes änderst. 

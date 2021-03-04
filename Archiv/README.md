# FHBSHK

## Mikroskop

Dieses Unterprojekt läuft auf einem Raspberry Pi. 
- focusing.py startet eine Dauerschleife mit einem Preview-Fenster für die Positionierung der Kamera, Objektträger usw.
- LEDArray.py stellt Funktionen zur Steuerung des LED-Array bereit
- processingImages.py liest das JSON-File ein und iteriert über jeden Eintrag. Es erstellt mit den gegeben Einstellungen jeweils ein Foto.

## ImageProcessing

In diesem Unterprojekt geht es um die Verarbeitung der enstandenen Bilder.
- generateConfig.py erstellt ein JSON-File mit den angegeben Parametern.
- ImagePrepared.py bearbeitet die erstellten Bilder, z.B. in ein einheitliches Format.
- ImageOverlay.py bearbeitet die Bilder die von ImagePrepared.py erstellt wurden weiter und setzt diese auf unterschiedlichste Art zusammen.
- Configs, dort werden chronologisch die bearbeiteten Fotos gespeichert. 

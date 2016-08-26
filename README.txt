main.py kann benutzt werden sowohl um neue Trainingsdaten zu schneiden, als auch zum klassifizieren/decoden eines Testbildes

1. In cut_image.py
	= in "seite.open..." name der Textdatei mit den Labels angeben
	= Falls keine label txt vorhanden, einfach unverändert lassen
		- man kann hinterher in der Funktion classify() angeben, dass man keine korrekten labels hat

1.1 Offset verändern
	= transformation.py öffnen
	= "offset1 = x1 / (a*schnitte_hoehe)"
		- kein Offset: a = 2
		- Offset: a > 2 (am besten eignet sich a = 2.7 oder mehr)

2. Terminal: python main.py bild.jpg
	= Höhe: 50
	= Breite: 25
	= Reihen: Immer eins mehr angeben, z.B. bei 12 können nur 11 Reihen zum Training/Testen verwendet werden
	
	= Einmal ins Bild klicken: Ausschnitt vergrößern
	= Nochmal klick: Ecke auswählen ODER Rechtsklick zum abbrechen
	= Falls Ausschnitt sich nicht vergrößert: Rechtsklick und nochmal etwas weiter unten linksklicken (so dass man die Ecke noch sieht;
	falls nicht, einfach mit Rechtsklick abbrechen)
	= Ecken-Reihenfolge: lo, ro, ru, lu

	= Geschnittene Bilder mit labels befinden sich nun im Ordner "bilder1"
		- Falls man keine label txt hatte, sind die labels in den Bildnamen natürlich falsch!
		- Falls die Bilder für neue Trainingsdaten geschnitten wurden
			* nur die guten Ausschnitte kopieren
			* recog/OFFSET/ dort einen neuen Ordner "cropped_blabla" erstellen
			* dort einfügen

3. Trainieren/Testen
	= Terminal im Ordner "recog" öffen
	= README im Ordner "recog" durchlesen

--

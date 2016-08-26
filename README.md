# ICT-Learn

### Voraussetzungen
* **Linux**
* [Tensorflow](https://www.tensorflow.org/versions/r0.10/get_started/os_setup.html#virtualenv-installation)
* TF-Learn: `pip install tflearn`
* [OpenCV](http://docs.opencv.org/2.4/doc/tutorials/introduction/linux_install/linux_install.html#linux-installation)
* Scipy
* Matplotlib
---
### Bedienung
`main.py` kann benutzt werden sowohl um neue Trainingsdaten zu schneiden, als auch zum klassifizieren/decoden eines Testbildes.
1. In `cut_image.py`
    * in "seite.open..." Name der Texdatei mit den Labels angeben
    * Falls keine label txt vorhanden, einfach unverändert lassen
        * man kann hinterher in der Funktion `classify()` angeben, dass man keine korrekten labels hat
2. (*optional*) Offset verändern
    * `transformation.py` öffnen
    * `offset1 = x1 / (a*schnitte_hoehe)`
        * kein Offset: a = 2 ("Hälfte-Hälfte")
        * Offset: a > 2 (am besten eignet sich a = 2.7 oder mehr)
3. Terminal: `python main.py [Bild.jpg]`
    - Höhe: 50
    - Breite: 25
    - Reihen: Immer *eins mehr* angeben. Möchte z.B. 5 Reihen decodieren, so muss man 6 eingeben
    - Offset: 2, falls genau mittig.  
    \>= 2.7, falls mehr von der oberen Reihe sichtbar sein soll (**empfohlen**) 
4. Ecken auswählen
    - Einmal ins Bild klicken: Ausschnitt vergrößern
    - Nochmal klick: Ecke auswählen ODER Rechtsklick zum abbrechen
    - Falls Ausschnitt sich **nicht** vergrößert: Rechtsklick, und nochmal etwas weiter unten linksklicken (so dass man die Ecke noch sieht;
	falls nicht, einfach mit Rechtsklick abbrechen)




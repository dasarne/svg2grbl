# Tipps zur Arbeit mit Inkscape

## Konfiguration des Koordinatensystems in Inkscape

Damit das Koordinatensystem in Inkscape optimal zur Nutzung mit der CNC-Fräse passt, solltest du eine Einstellung ändern:

**Schritt:**

- Gehe zu \*\*Bearbeiten → Einstellungen → Benutzeroberfläche\*\* -> **"Ursprung in der oberen linken Ecke, wobei die Y-Achse nach unten zeigt"** deaktivieren
- Die Änderung wirkt sich erst bei einem Neustart von Inkscape oder dem Anlegen eines neuen Dokumentes aus.

⚠ **Achtung:** Diese Änderung beeinflusst nur die Darstellung in Inkscape. Erzeugte SVG-Dateien behalten ihr ursprüngliches, dem SVG-Standard entsprechendes Koordinatensystem. `svg2gcode` konvertiert das SVG-Koordinatensystem aktiv so, das es dann so graviert wird wie es so in Inkscape dargestellt wird.

---

## Dokumentenerstellung für CNC-Fräsen

Beim Anlegen eines neuen Dokuments in Inkscape ist es sinnvoll, bereits an die spätere Verwendung mit der CNC-Fräse zu denken. Hier einige wichtige Hinweise:

### **1. Koordinatenursprung immer links/unten**

In der CNC-Umgebung befindet sich der Ursprung (0,0) immer **unten links**. Plane dein Design entsprechend, um später eine passende Positionierung auf der Fräse zu ermöglichen.

### **2. Hochkant- oder Querformat festlegen**

Überlege frühzeitig, ob du dein Design im Hoch- oder Querformat benötigst und richte das Inkscape-Dokument entsprechend ein.

### **3. Dokumentgröße anpassen**

Lege das Dokument in Inkscape gleich mit den **genauen Maßen deines zu gravierenden Objekts** an. Dies hilft dir, die Fräsposition besser einzuschätzen und spätere Skalierungsprobleme zu vermeiden.

### **4. SVG-Füllungen werden nicht verarbeitet**

⚠ **Wichtiger Hinweis:** `svg2gcode` wertet **nur Pfade, aber keine Füllungen** aus. Das bedeutet:

- **Flächige Füllungen oder Muster** werden nicht graviert.
- Falls du eine Fläche mit Schraffuren oder Mustern gravieren möchtest, erstelle explizite **Linien/Pfade**, anstatt Füllungen zu verwenden.

### 5. Text in Objekte wandeln.

- svg2gcode kann Text nicht verarbeiten

### 6. Die Farbe von Objekten ist vollkommen unwichtig 

- Weiße Objekte auf weißem Hintergrund, Objekte ohne Farbe? Egal, alles wird graviert. 

Mit diesen Einstellungen und Planungen kannst du Inkscape optimal für die Nutzung mit `svg2gcode` vorbereiten!

Es lohnt also immer eine Endkontrolle mit dem wunderbaren [ncviewer]([https://ncviewer.com/)

## Muster gravieren

Wie kann man dennoch Muster gravieren, obwohl svg2gcode Füllungen nicht verarbeitet? Hier ist ein Trick, der sich in der Praxis bewährt hat:

### 1. SVG als PNG exportieren

- Vor dem Exportieren als PNG gruppieren Sie die gesammte Grafik (Ctrl+A und Ctrl+G) 
- Jetzt exportieren Sie die Grafik als PNG. Seien Sie dabei großzügig mit der Auflösung – 1200 dpi oder mehr sind empfehlenswert. 
- Sie brauchen sich keine Gedanken um vielleicht vergessene und nicht umgewandelte Texte machen
- Achten Sie auf maximale Kontraste. Objekte die sich nicht abheben sind fürs Gravieren verloren

### 2. Das PNG importieren

- Genau an die Stelle der Grafik positionieren.
- Mit Ebenen zu Arbeiten und die eigentliche Gruppe mit der Grafik auszuschalten ist hilfreich

### 3. PNG in Pfade wandeln

- Nun wandeln sie nun die Grafik in Pfade. (Vektorisieren des Bitmaps)
- Schauen sie sich das Ergebnis kritisch an
- Ist alles Vektorisiert worden oder fehlen Elemente, die sich wegen eines schlechten Kontrastes nicht vektorisieren lassen? Sollte das der Fall sein, an den Vektorisierungsparametern in Inkscape spielen. Kommen Sie damit nicht weiter: Die Farben in der Quell-Grafik ändern, egal wie das aussieht. 
- Bei aus dem Internet importierten Mustern hat man manchmal keine Wahl. Im schlimmsten Fall das PNG in Gimp auf hohen Kontrast trimmen.
- In der Ebenendarstellung entsteht ein einziges Pfad-Objekt. Wir sind unserem Ziel zum greifen na!

### 4. Mit den Pfaden eine neue Datei anlegen

- Damit svg2gcode wirklich nur dies und nicht alles andere mit graviert, ist dieser Schritt nun auch noch nötig.
- In der Ebenen-Darstellung das Ergebnis der Vektorisierung auswählen, kopieren und in ein neues Dokument pasten.&#x20;
- Kleine Qualitätskontrolle: Stimmen noch die Größe und Ausrichtung? Letzte Chance!
- Das dann abspeichern.
- \*\*Fertig!\*\*

Diese Datei kann jetzt mit svg2gcode in GCode gewandelt werden. 

### Tipps

- Drehen Sie beim Export ruhig mal die Auflösung runter. Das Ergebnis der Gravur sieht nicht mehr so clean aus... also mir gefällt das
- Spielen Sie mal mit den Vektoreffekten von Inkscape. Das gibt der Gravur einen besonderen Charme
- Die initiale Quelle Ihres kreativen Schaffens muss ja nicht ein SVG sein. Handyfotos usw. vektorisiert und anschließend erneut kombiniert. Der Möglichkeiten sind da keine Grenzen gesetzt.


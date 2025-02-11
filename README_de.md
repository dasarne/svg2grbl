# SVG2GRBL CNC Fork

## Projektbeschreibung

Dieses Projekt ermöglicht es, **SVG-Dateien direkt in G-Code für eine CNC-Fräse umzuwandeln**. Ziel ist es, **Gravuren** auf verschiedenen Oberflächen einfach und präzise aus SVG-Vektorgrafiken zu erstellen.

Es ist ein Fork von [svg2grbl](https://github.com/nknotts/svg2grbl/tree/main), welches ursprünglich für **Laser und Plotter** entwickelt wurde. Diese Werkzeuge arbeiten typischerweise ohne Z-Koordinaten-Steuerung – sie schalten lediglich den Laser oder Stift ein und aus.

Diese Version von svg2grbl wurde angepasst, um mit **CNC-Fräsen** zu arbeiten, die eine **kontrollierte Z-Achsen-Steuerung** und **Vorschub** benötigen.

## Unterschiede zum Originalprojekt

### Steuerung der Skalierung und Positionierung

- **Original (Laser/Plotter-Version):**

  - Automatische Skalierung auf einen definierten Arbeitsbereich.
  - Drehung der Datei, falls nötig.
  - Die Positionierung der Gravur wird von der Software für die zur Verfügung stehende Fläche des Läsercutters zu optimieren.

- **Dieser Fork (CNC-Version):**

  - **Ermöglichung einer exakten Positionierung** – Wenn alle Automatismen ausgeschaltete sind,  liegt der Ursprung genau da, wo die SVG-Datei ihn angibt. Man kann ich Inkscape planen.
  - **G1 mit Z-Koordinaten für Frästiefe** statt M3/M5 für Laserschaltung.

### Ursprung des Koordinatensystems

- SVG-Standard: Der Ursprung (0,0) liegt oben links.
- CNC-Fräsen: Der Ursprung (0,0) ist üblicherweise unten links.
- Der Ansatz in diesem Projekt: Es wird bei der GCode-Ausgabe das SVG-Koordinatensystem so transformiert, dass es mit CNC-Fräsen kompatibel ist.

###  Wichtige Anpassungen

- **Ausschaltbare automatische Skalierung & Rotation** (volle Kontrolle über das Original-SVG).
- **Ursprungskorrektur für CNC-Koordinaten.**
- **Z-Achsensteuerung für Gravuren (G1 mit definierter Frästiefe).**

## Nutzung

1. Erstelle eine **SVG-Datei** mit den gewünschten Gravurpfaden.
2. Konvertiere sie mit `svg2gcode.py` in G-Code.
3. Lade den G-Code in deine CNC-Fräse.
4. Starte die Gravur.

## Lizenz & Mitwirkung

Dieser Fork ist eine Weiterentwicklung des ursprünglichen Projekts. Pull Requests und Verbesserungen sind jederzeit willkommen!

Ziel ist die Nutzung für CNC-Fräsen zu optimieren und dabei möglichst **wenig Software-Manipulation an den SVG-Daten und maximale Kontrolle über das Endergebnis zu gewährleisten**.


# SVG2GRBL CNC Fork

(Eine deutsche Version gibt es [hier](README_de.md))

## Project Description

This project allows **SVG files to be converted directly into G-code for a CNC machine**. The goal is to create **engraved designs** on various surfaces easily and precisely from SVG vector graphics.

It is a fork of [svg2grbl](https://github.com/nknotts/svg2grbl/tree/main), originally developed for **laser cutters and plotters**. These tools typically operate without Z-axis control – they simply switch the laser or pen on and off.

This version of svg2grbl has been adapted to work with **CNC machines** that require **controlled Z-axis movements** and **feed rate control**.

## Differences from the Original Project

### Scaling and Positioning Control

- **Original (Laser/Plotter Version):**
  - Automatic scaling to a defined work area.
  - Rotation of the file if necessary.
  - Positioning of the engraving is handled by the software to fit the available workspace of the laser cutter.

- **This Fork (CNC Version):**
  - **Enables precise positioning** – When all automation features are disabled, the **origin remains exactly where it is defined in the SVG file**, allowing precise planning in Inkscape.
  - **Uses G1 with Z-coordinates for engraving depth** instead of M3/M5 laser control.

### Coordinate System Origin

- **SVG Standard:** The origin (0,0) is at the **top left**.
- **CNC Machines:** The origin (0,0) is typically at the **bottom left**.
- **Our approach:** During G-code generation, the SVG coordinate system is transformed so that it aligns with CNC machine conventions.

### Key Modifications

- **Optional automatic scaling & rotation** (full control over the original SVG).
- **Origin correction for CNC coordinate systems.**
- **Z-axis control for engraving (G1 with defined engraving depth).**

## Usage

1. Create a **SVG file** with the desired engraving paths.
2. Configure the config.py file. You can find instructions [here](config.md). 
3. Convert it to G-code with `svg2gcode.sh`.
4. Load the G-code into your CNC router.
5. Start the engraving.

## License & Contribution

This fork is a further development of the original project. Pull requests and improvements are always welcome!

The goal is to **optimize usability for CNC machines while keeping software modifications to SVG data minimal and ensuring maximum control over the final engraving output**.


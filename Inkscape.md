# Tips for Working with Inkscape

## Configuring the Coordinate System in Inkscape

To optimize the coordinate system in Inkscape for use with a CNC machine, you should change the following setting:

**Steps:**

- Go to **Edit → Preferences → Interface** -> **Disable "Origin at upper left, with Y-axis pointing down"**
- The change only takes effect after restarting Inkscape or creating a new document.

⚠ **Note:** This change only affects the display in Inkscape. Generated SVG files retain their original coordinate system according to the SVG standard. `svg2gcode` actively converts the SVG coordinate system so that engraving is performed exactly as displayed in Inkscape.

---

## Creating Documents for CNC Engraving

When creating a new document in Inkscape, it is helpful to consider its use with a CNC machine in advance. Here are some important tips:

### **1. Always set the coordinate origin to the bottom-left**

In a CNC environment, the origin (0,0) is always **bottom-left**. Plan your design accordingly to ensure proper positioning on the CNC machine.

### **2. Determine portrait or landscape format**

Decide early whether your design should be in portrait or landscape mode and set up the Inkscape document accordingly.

### **3. Adjust document size**

Set up the document in Inkscape with the **exact dimensions of your engraving object** from the beginning. This helps in better estimating the engraving position and avoiding scaling issues later.

### **4. SVG fills are not processed**

⚠ **Important note:** `svg2gcode` only processes **paths, not fills**. This means:

- **Solid fills or patterns** will not be engraved.
- If you want to engrave an area with hatching or patterns, create explicit **lines/paths** instead of fills.

### **5. Convert text to objects**

- `svg2gcode` cannot process text directly.

### **6. Object colors are irrelevant**

- White objects on a white background, objects without color? It doesn't matter – everything will be engraved.

With these settings and planning steps, you can optimally prepare Inkscape for use with `svg2gcode`.

It is always worth performing a final check with the excellent [ncviewer](https://ncviewer.com/).

## Engraving Patterns

How can patterns still be engraved even though `svg2gcode` does not process fills? Here is a practical trick that has proven effective:

### **1. Export SVG as PNG**

- Before exporting as PNG, group the entire graphic (**Ctrl+A and Ctrl+G**).
- Export the graphic as PNG. Use a **high resolution of at least 1200 dpi**.
- No need to worry about unconverted text.
- Ensure maximum contrast – objects that do not stand out will be lost in engraving.

### **2. Import the PNG**

- Position it exactly over the original design.
- Using layers and hiding the original group can be helpful.

### **3. Convert PNG to paths**

- Now convert the graphic into paths (**Vectorize Bitmap** in Inkscape).
- Examine the result critically.
- Check if everything is vectorized or if elements are missing due to poor contrast. Adjust the vectorization parameters in Inkscape if needed. If that doesn’t help, modify the colors in the source graphic.
- When using patterns from the internet, sometimes you have no choice. In the worst case, increase contrast using GIMP before vectorizing.
- In the layer view, you will get a single path object. We are almost there!

### **4. Create a new file with the paths**

- To ensure that `svg2gcode` engraves only the converted paths and nothing else, follow these steps:
- In the layer view, select the result of the vectorization, copy it, and paste it into a new document.
- Quick quality check: Is the size and orientation correct? This is the last chance to adjust!
- Save the file.
- **Done!**

This file can now be converted into G-code using `svg2gcode`.

### **Tips**

- Try reducing the resolution when exporting. The engraving result will look less "clean" – I personally like that aesthetic.
- Experiment with Inkscape’s vector effects. They can give your engraving a unique charm.
- The original source of your creative work doesn’t have to be an SVG. You can vectorize **smartphone photos**, combine them, and experiment. The possibilities are endless!


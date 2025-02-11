def in2mm(val_in):
    return val_in * 25.4


# Konfiguration für die Fräsereinstellungen
SAFE_HEIGHT = 5.0  # Sicherheitsabstand in mm
CUT_DEPTH = -1.0   # Frästiefe in mm
FEED_RATE = 300    # Vorschubgeschwindigkeit in mm/min

AUTO_ROTATE = False
MANUAL_ROTATION_DEG = 0 # only used if AUTO_ROTATE == False

AUTO_SCALE = False
CANVAS_WIDTH_X = in2mm(11)
CANVAS_WIDTH_Y = in2mm(8.5)

AUTO_SHIFT = False

CANVAS_LEFT_MARGIN = 0 
CANVAS_RIGHT_MARGIN = 0 
CANVAS_TOP_MARGIN = 0 
CANVAS_BOTTOM_MARGIN = 0 


def gcode_pause(timeout_s):
    yield f'G4 P{timeout_s:.2f}'


# these functions are using by svg2gcode.py as part of gcode generation
def preamble():
    yield 'G90'


def postamble():
    yield ''
    yield 'G0 X0 Y0'
    yield 'M30'


def pen_up():
    yield f'G0 Z{SAFE_HEIGHT}'  # Spindel anheben


def pen_down():
    yield f'G1 Z{CUT_DEPTH} F{FEED_RATE}'  # Spindel absenken mit Vorschub


USABLE_WIDTH = CANVAS_WIDTH_X - CANVAS_LEFT_MARGIN - CANVAS_RIGHT_MARGIN
USABLE_HEIGHT = CANVAS_WIDTH_Y - CANVAS_TOP_MARGIN - CANVAS_BOTTOM_MARGIN

CANVAS_MIDPOINT_X = CANVAS_LEFT_MARGIN + USABLE_WIDTH / 2
CANVAS_MIDPOINT_Y = CANVAS_BOTTOM_MARGIN + USABLE_HEIGHT / 2

BEZIER_DISCRETIZATION_LENGTH_MM = 0.1
MAX_BEZIER_DISCRETIZATION_POINTS = 32

from skidl import *
from os import environ

environ["KICAD_SYMBOL_DIR"] = "/Library/Application Support/kicad/library"

lib_search_paths["kicad"].append("../lib/camera")
lib_search_paths["kicad"].append("../lib/96boards")

camera = Part("camera", "SFW15R-2STE1LF", footprint="Amphenol-SFW15R-2STE1LF-*")
hsconn = Part("96boards", "CONN_02X30", footprint="61083-063400LF")


gnd, vcc = Net("GND"), Net("VCC")
gnd.drive, vcc.drive = POWER, POWER

vcc += camera["CAM_3V3"]
gnd += camera["GND"]

generate_netlist()

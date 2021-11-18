from skidl import *
from os import environ
from utilities import release

# Add KICAD_SYMBOL_DIR if doesn't exist
environ["KICAD_SYMBOL_DIR"] = "/Library/Application Support/kicad/library"

# Add libraries
lib_search_paths["kicad"].append("../lib/camera")
lib_search_paths["kicad"].append("../lib/96boards")

camera = Part("camera", "SFW15R-2STE1LF", footprint="Amphenol-SFW15R-2STE1LF-0")
hsconn = Part("96boards", "CONN_02X30", footprint="61083-063400LF")
lsconn = Part("96boards", "CONN_02X20", footprint="Socket_Strip_SMD_2x20_Pitch2mm")

gnd, vcc = Net("GND"), Net("VCC")

csi = Bus("csi_bus", 8)  # A 2-bit bus from nets.
camera_control = Bus(
    "cam_bus", camera["CAM_IO0"], camera["CAM_IO1"]
)  # A 2-bit bus from nets.

vcc += camera["CAM_3V3"]
gnd += camera["GND"]

for index, each in enumerate(camera):
    if not any(map(each.name.__contains__, ["GND", "MNT", "3V3", "IO"])):
        print(f"inserting {each.name}")
        csi.insert(index, each, Net())


hsconn[10, 8, 16, 14, 4, 2, 32, 34] += csi[0:7]
lsconn[30, 32] += camera_control
# gnd.drive, vcc.drive = POWER, POWER

generate_netlist()
release()

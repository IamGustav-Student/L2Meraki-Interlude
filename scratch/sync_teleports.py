import os
import xml.etree.ElementTree as ET

teleporters_dir = r"f:\Programador GS\L2 Meraki\server_data\game\data\teleporters"
target_npcs = [
    "30006", "30059", "30080", "30134", "30146", "30177", "30233", "30256", "30320", 
    "30540", "30576", "31275", "31320", "31964", "30836", "30848", "30878", "30899"
]

fiorella_xml = r"f:\Programador GS\L2 Meraki\server_data\game\data\teleporters\others\50009.xml"
tree = ET.parse(fiorella_xml)
root = tree.getroot()
fiorella_npc = root.find("npc")
teleports = fiorella_npc.findall("teleport")

for npc_id in target_npcs:
    # Find the XML file for this NPC (check town then others)
    found = False
    for sub in ["town", "others"]:
        path = os.path.join(teleporters_dir, sub, f"{npc_id}.xml")
        if os.path.exists(path):
            found_path = path
            found = True
            break
    
    if found:
        # Create new XML content
        new_root = ET.Element("list")
        new_root.set("xmlns:xsi", "http://www.w3.org/2001/XMLSchema-instance")
        new_root.set("xsi:noNamespaceSchemaLocation", "../../xsd/teleporterData.xsd")
        
        new_npc = ET.SubElement(new_root, "npc")
        new_npc.set("id", npc_id)
        
        # Copy all teleports from Fiorella
        for tp in teleports:
            new_tp = ET.SubElement(new_npc, "teleport")
            if "id" in tp.attrib: new_tp.set("id", tp.attrib["id"])
            if "name" in tp.attrib: new_tp.set("name", tp.attrib["name"])
            new_tp.set("type", tp.attrib.get("type", "OTHER"))
            
            for loc in tp.findall("location"):
                new_loc = ET.SubElement(new_tp, "location")
                for attr, val in loc.attrib.items():
                    new_loc.set(attr, val)
        
        # Save updated XML
        with open(found_path, "wb") as f:
            f.write(b'<?xml version="1.0" encoding="UTF-8"?>\n')
            f.write(ET.tostring(new_root, encoding="utf-8"))

print(f"Synchronized teleport XMLs for {len(target_npcs)} NPCs.")

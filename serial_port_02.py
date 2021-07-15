## 장치에 대한 상세한 정보를 확인
from serial.tools.list_ports import comports

nodes = comports()

count = 0;
for node in nodes:
    print("[{0}]".format(count))
    print("         device: ", node.device)
    print("    description: ", node.description)
    print("   manufacturer: ", node.manufacturer)
    print("           hwid: ", node.hwid)
    print("      interface: ", node.interface)
    print("       location: ", node.location)
    print("           name: ", node.name)
    count += 1

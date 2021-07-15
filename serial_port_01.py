## 컴퓨터에 연결된 시리얼 통신 장치들의 이름을 확인
from serial.tools.list_ports import comports

for port, desc, hwid in sorted(comports()):
    print("%s" % (port))

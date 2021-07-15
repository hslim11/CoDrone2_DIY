from time import sleep

from e_drone.drone import *
from e_drone.protocol import *

def eventButton(button):
    print(button.button)

	

if __name__ == '__main__':

    drone = Drone()       # 드론 객체 생성
    drone.open()          # 시리얼 포트 연결
    drone.setEventHandler(DataType.Button, eventButton)
    drone.sendPing(DeviceType.Controller)   
   


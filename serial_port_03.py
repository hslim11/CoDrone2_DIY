from time import sleep

from e_drone.drone import *
from e_drone.protocol import *

if __name__ == '__main__':

    drone = Drone()       # 드론 객체 생성
    drone.open("COM09")   # 시리얼 포트 연결

    drone.sendBuzzer(BuzzerMode.Scale, BuzzerScale.C4.value, 500)   # 버저에 4옥타브 도 소리를 500ms 동안 내라고 명령하기
    sleep(1)              # 1초간 sleep

    drone.close()         # 시리얼 포트 닫기 및 내부 데이터 수신 스레드 종료

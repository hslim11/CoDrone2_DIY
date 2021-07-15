# Mission 1

from time import sleep

from e_drone.drone import *
from e_drone.protocol import *


if __name__ == '__main__':

    drone = Drone()
    drone.open()


    print("미션1 시작")
    drone.sendTakeOff()
    sleep(0.01)
    
    print("호버링")
    drone.sendControlWhile(0, 0, 0, 0, 5000)
    drone.sendControlWhile(0, 0, 0, 0, 3000)

    print("전진비행 50cm")
    drone.sendControlWhile(0, 70, 0, 0, 1000)

    print("고도 상승 150cm")
    drone.sendControlWhile(0, 0, 0, 60, 3000) # 3000?

    print("정지 비행 5초")
    drone.sendControlWhile(0, 0, 0, 0, 5000)
    
    #정사각형
    print("정 사각형 그리기")
    drone.sendControlWhile(0, 80, 0, 0, 1000) #전
    drone.sendControlWhile(0, 0, 0, 0, 700)
    drone.sendControlWhile(-100, 0, 0, 0, 1200) #좌
    drone.sendControlWhile(0, 0, 0, 0, 700)
    drone.sendControlWhile(0, -70, 0, 0, 1000) #후
    drone.sendControlWhile(0, 0, 0, 0, 700)
    drone.sendControlWhile(40, 0, 0, 0, 1000) #우

    print("정지 비행 5초")
    drone.sendControlWhile(0, 0, 0, 0, 5000)

    #원형 비행
    print("원 그리기")
    drone.sendControlWhile(0, 0, -100, 0, 500)
    drone.sendControlWhile(0, 80, 100, 0, 5000)
    drone.sendControlWhile(-30, 30, 65, 0, 1300) #역회전
    drone.sendControlWhile(-10, 0, 0, 0, 1000)
    
    print("정지 비행 5초")
    drone.sendControlWhile(0, 0, 0, 0, 5000)
    
    print("후진비행 100cm")
    drone.sendControlWhile(0, -50, 0, 0, 2000)

    print("고도 하강 100cm")
    drone.sendControlWhile(0, 0, 0, -80, 1000)
    
    print("정지비행 5초")
    drone.sendControlWhile(0, 0, 0, 0, 5000)

    print("Landing") # 랜딩은 두번
    drone.sendLanding()
    sleep(0.01)
    drone.sendLanding()
    sleep(0.01)

    drone.close()

"""
    sendControlWhile(roll, pitch, yaw, throttle, timeMs)
    roll     : 좌우
    pitch    : 앞
    yaw      : 회전
    throttle : 상승 하강

    회전을 yaw -100, tms 2000으로하니 정확히 반대로 돔
"""
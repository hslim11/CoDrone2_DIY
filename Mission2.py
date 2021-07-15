# Mission 2

from time import sleep
from e_drone.drone import *
from e_drone.protocol import *
if __name__ == '__main__':
    
    drone = Drone()
    drone.open("COM20")

    print("미션2 시작")
    drone.sendTakeOff()
    sleep(0.01)
    
    print("호버링")
    drone.sendControlWhile(0, 0, 0, 0, 5000)
    drone.sendControlWhile(0, 0, 0, 0, 3000)

    print("전진비행 50cm")
    drone.sendControlWhile(0, 70, 0, 0, 1000)
    drone.sendControlWhile(0, 0, 0, 0, 1000)

    print("고도 상승 150cm")
    drone.sendControlWhile(0, 0, 0, 70, 2000) # 3000?

    print("정지 비행 5초")
    drone.sendControlWhile(0, 0, 0, 0, 5000)
    
    #팔자 원 비행
    drone.sendControlWhile(0, 0, -100, 0, 500)
    drone.sendControlWhile(0, 80, 100, 0, 5200)
    drone.sendControlWhile(0, 100, -100, 27, 4200)
    drone.sendControlWhile(0, 0, 0, 0, 1000)
    drone.sendControlWhile(0, 0, 100, 0, 2000)
    
    print("정지 비행 5초")
    drone.sendControlWhile(0, 0, 0, 0, 5000)

    #지그재그 비행 (3회, 시계방향 45도 0.5sec, 전진 1sec)
    print("지그재그")
    print("우측으로 반회전 시작") # 시작위치가 앞을 보기 때문에 tm 500
    drone.sendControlWhile(10, 0, -60, 0, 500)
    print("앞으로 전진")
    drone.sendControlWhile(0, 90, 0, 0, 1500)
    print("좌측으로 반회전 시작")
    drone.sendControlWhile(-30, 0, 100, 0, 1800) # 방향으 틀어져서 tm 1000
    print("앞으로 전진")
    drone.sendControlWhile(0, 90, 0, 0, 1500)
    print("우측으로 반회전 시작")
    drone.sendControlWhile(10, 0, -70, 0, 1200) # 우측으로 많이 돌아야함
    print("앞으로 전진")
    drone.sendControlWhile(0, 90, 0, 0, 1500)
    print("좌측으로 반회전 시작")
    drone.sendControlWhile(-30, 0, 100, 0, 1800)
    print("앞으로 전진")
    drone.sendControlWhile(0, 90, 0, 0, 1000)
    print("우측으로 반회전 시작")
    drone.sendControlWhile(10, 0, -70, 0, 1200) # 우측으로 많이 돌아야함
    print("앞으로 전진")
    drone.sendControlWhile(0, 90, 0, 0, 1500)
    print("좌측으로 반회전 시작")
    drone.sendControlWhile(-30, 0, 100, 0, 1800)
    print("앞으로 전진")
    drone.sendControlWhile(0, 90, 0, 0, 1000)
    print("우측으로 반회전 시작")
    drone.sendControlWhile(10, 0, -70, 0, 1200) # 우측으로 많이 돌아야함
    print("앞으로 전진")
    drone.sendControlWhile(0, 90, 0, 0, 1500)
    print("좌측으로 반회전 시작")
    drone.sendControlWhile(-30, 0, 100, 0, 1800)
    print("앞으로 전진")
    drone.sendControlWhile(0, 90, 0, 0, 1000)
    
    print("정지 비행 5초")
    drone.sendControlWhile(0, 0, 0, 0, 5000)
    
    print("전진비행 50cm")
    drone.sendControlWhile(0, 50, 0, 0, 1000)
    drone.sendControlWhile(0, 0, 0, 0, 1000)

    print("고도 하강 50cm")
    drone.sendControlWhile(0, 0, 0, -70, 1000)
    
    print("정지비행 5초")
    drone.sendControlWhile(0, 0, 0, 0, 5000)

    print("고도 상승 100cm")
    drone.sendControlWhile(0, 0, 0, 35, 2000)

    print("전진비행 50cm")
    drone.sendControlWhile(0, 50, 0, 0, 1000)
    drone.sendControlWhile(0, 0, 0, 0, 1000)
    
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


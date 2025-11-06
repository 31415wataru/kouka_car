def ライントレース():
    if A == 4 or A == 6:
        Rover.motor_run_dual(0, 150)
    elif A == 1 or A == 3:
        Rover.motor_run_dual(150, 0)
    elif A == 2:
        Rover.motor_run_dual(100, 100)
    elif A == 0:
        Rover.motor_run_dual(150, 150)
    elif A == 7:
        Rover.motor_run_dual(100, 100)
    else:
        Rover.motor_run_dual(0, 0)
def 障害物回避():
    global A
    # 黒線を見つけるまで旋回
    while True:
        A = Rover.line_tracking()
        timer3 = input.running_time()
        if A != 0:
            # 黒線を検出したら停止して戻る
            Rover.motor_run_dual(150, 0)
            basic.pause(400)
            return
        # ---- ① 最初の1秒間前進 ----
        while input.running_time() - timer3 < 1000:
            A = Rover.line_tracking()
            # 床の色を監視
            if A != 0:
                Rover.motor_run_dual(150, 0)
                basic.pause(400)
                return
            else:
                Rover.motor_run_dual(170, 120)
        C2 = 0
        D2 = 0
        while C2 == 0:
            if Rover.ultrasonic() < 30:
                Rover.motor_run_dual(0, 0)
                break
            Rover.motor_run_dual(-100, 100)
        while D2 == 0:
            if Rover.ultrasonic() > 30:
                Rover.motor_run_dual(0, 0)
                break
            Rover.motor_run_dual(100, -100)
A = 0
timer2 = 0
timer = 0
D = 0
C = 0

def on_forever():
    global A
    A = Rover.line_tracking()
    if Rover.ultrasonic() < 15:
        Rover.motor_run_dual(200, -200)
        basic.pause(300)
        障害物回避()
    else:
        ライントレース()
basic.forever(on_forever)
let A = 0
let C = 0
let D = 0
let timer = 0
let timer2 = 0
function ライントレース() {
    
    if (A == 4 || A == 6) {
        Rover.MotorRunDual(0, 150)
    } else if (A == 1 || A == 3) {
        Rover.MotorRunDual(150, 0)
    } else if (A == 2) {
        Rover.MotorRunDual(100, 100)
    } else if (A == 0) {
        Rover.MotorRunDual(150, 150)
    } else if (A == 7) {
        Rover.MotorRunDual(100, 100)
    } else {
        Rover.MotorRunDual(0, 0)
    }
    
}

function 障害物回避() {
    let timer: number;
    let C: number;
    let D: number;
    
    //  黒線を見つけるまで旋回
    while (true) {
        A = Rover.LineTracking()
        timer = input.runningTime()
        if (A != 0) {
            //  黒線を検出したら停止して戻る
            Rover.MotorRunDual(150, 0)
            basic.pause(400)
            return
        }
        
        //  ---- ① 最初の1秒間前進 ----
        while (input.runningTime() - timer < 1000) {
            A = Rover.LineTracking()
            //  床の色を監視
            if (A != 0) {
                Rover.MotorRunDual(150, 0)
                basic.pause(400)
                return
            } else {
                Rover.MotorRunDual(170, 120)
            }
            
        }
        C = 0
        D = 0
        while (C == 0) {
            if (Rover.Ultrasonic() < 30) {
                Rover.MotorRunDual(0, 0)
                break
            }
            
            Rover.MotorRunDual(-100, 100)
        }
        while (D == 0) {
            if (Rover.Ultrasonic() > 30) {
                Rover.MotorRunDual(0, 0)
                break
            }
            
            Rover.MotorRunDual(100, -100)
        }
    }
}

basic.forever(function on_forever() {
    
    A = Rover.LineTracking()
    if (Rover.Ultrasonic() < 15) {
        Rover.MotorRunDual(200, -200)
        basic.pause(300)
        障害物回避()
    } else {
        ライントレース()
    }
    
})
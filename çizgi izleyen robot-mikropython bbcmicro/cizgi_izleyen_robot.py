from microbit import *
import maqueenMotor

def sagaDon():
    image = Image("00900:00090:99999:00090:00900")
    display.show(image)
    motor.run(1,0,45)
    motor.run(0,0,200)

def solaDon():
    image = Image("00900:09000:99999:09000:00900")
    display.show(image)
    motor.run(0,0,45)
    motor.run(1,0,200)

def solaDon():
    image = Image("00900:09990:90909:00900:00900")
    display.show(image)
    motor.run(0,0,200)
    motor.run(1,0,200)

motor =maqueenMotor()
ileri()
while True:
    if (pin13.read_digital() == 0) and (pin14.read_digital() == 1):
        sagaDon()
    else:
        if (pin13.read_digital() == 1) and (pin14.read_digital() == 0):
            solaDon()
        else:
            ileri()
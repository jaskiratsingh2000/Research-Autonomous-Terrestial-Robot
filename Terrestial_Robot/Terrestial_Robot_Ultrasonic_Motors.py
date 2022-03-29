# Code to run the Motors and collect the data points from the 3 Ultrasonic Sensors

import RPi.GPIO as GPIO
import time
import csv
 
#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
 
# Setting GPIO Pins for Ultasonic Senor1 (Front Face)
gpioTrigger1 = 4
gpioEcho1 = 17

# Setting GPIO Pins for Ultasonic Senor2 (Left Face)
gpioTrigger2 = 26
gpioEcho2 = 19

# Setting GPIO Pins for Ultasonic Senor3 (Right Face)
gpioTrigger3 = 5
gpioEcho3 = 6

# Setting GPIO Pins for the Motor A
DirMotorA = 27
PwmMotorA = 22

# Setting GPIO pins for the Motor B
DirMotorB = 23
PwmMotorB = 24
 
# Setting GPIO direction (IN / OUT) for Sensor1 (Front Face)
GPIO.setup(gpioTrigger1, GPIO.OUT)
GPIO.setup(gpioEcho1, GPIO.IN)
 
# Setting GPIO direction (IN / OUT) for Sensor2 (Left Face)
GPIO.setup(gpioTrigger2, GPIO.OUT)
GPIO.setup(gpioEcho2, GPIO.IN)

# Setting GPIO direction (IN / OUT) for Sensor3 (Right Face)
GPIO.setup(gpioTrigger3, GPIO.OUT)
GPIO.setup(gpioEcho3, GPIO.IN)

# Setting up GPIO Pins direction for the Motor A
GPIO.setup(DirMotorA, GPIO.OUT) 
GPIO.setup(PwmMotorA, GPIO.OUT) 

# Setting up GPIO Pins direction for the Motor B
GPIO.setup(DirMotorB, GPIO.OUT) 
GPIO.setup(PwmMotorB, GPIO.OUT) 


def distanceBySensor1():

 # Setting Trigger to HIGH for Ultrasonic Sensor1 (Front Face)
    GPIO.output(gpioTrigger1, True)
 
    # Setting Trigger of Ultrasonic Sensor1 (Front Face) after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(gpioTrigger1, False)
 
    startTimeSensor1 = time.time()
    stopTimeSensor1 = time.time()
 
    # Saving Start Time
    while GPIO.input(gpioEcho1) == 0:
        startTimeSensor1 = time.time()
 
    # Saving Time of arrival
    while GPIO.input(gpioEcho1) == 1:
        stopTimeSensor1 = time.time()

    # Time difference between start and arrival
    timeElapsedSensor1 = stopTimeSensor1 - startTimeSensor1
        # multiplying with the sonic speed (34300 cm/s)
        # and dividing by 2, because there and back
    distanceBySensor1 = (timeElapsedSensor1 * 34300) / 2
     
    return distanceBySensor1


def distanceBySensor2():

 # Setting Trigger to HIGH for Ultrasonic Sensor2 (Front Face)
    GPIO.output(gpioTrigger2, True)
 
    # Setting Trigger of Ultrasonic Sensor2 (Front Face) after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(gpioTrigger2, False)
 
    startTimeSensor2 = time.time()
    stopTimeSensor2 = time.time()
 
    # Saving Start Time
    while GPIO.input(gpioEcho2) == 0:
        startTimeSensor2 = time.time()
 
    # Saving Time of Arrival
    while GPIO.input(gpioEcho2) == 1:
        stopTimeSensor2 = time.time()

    # Time difference between start and arrival
    timeElapsedSensor2 = stopTimeSensor2 - startTimeSensor2
    distanceBySensor2 = (timeElapsedSensor2 * 34300) / 2
     
    return distanceBySensor2


def distanceBySensor3():

 # Setting Trigger to HIGH for Ultrasonic Sensor3 (Right Face)
    GPIO.output(gpioTrigger3, True)
 
    # Setting Trigger of Ultrasonic Sensor1 (Front Face) after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(gpioTrigger3, False)
 
    startTimeSensor3 = time.time()
    stopTimeSensor3 = time.time()
 
    # Saving StartTime
    while GPIO.input(gpioEcho3) == 0:
        startTimeSensor3 = time.time()
 
    # Saving time of arrival
    while GPIO.input(gpioEcho3) == 1:
        stopTimeSensor3 = time.time()

    # Time difference between start and arrival
    timeElapsedSensor3 = stopTimeSensor3 - startTimeSensor3
    distanceBySensor3 = (timeElapsedSensor3 * 34300) / 2
     
    return distanceBySensor3

 # Opening and Writing into CSV file

obstacleDataFile = open('Obstacle_Data.csv', 'w+', newline ='')


def runningMotorsPWM():

    # Driving the motor Clockwise that is FORWARD

    #MAX Frequency is 20 Hz

    leftMotorAPWM = GPIO.PWM(PwmMotorA, 20)

    leftMotorAPWM.start(20)

    leftMotorAPWM.ChangeDutyCycle(0)

    righttMotorAPWM = GPIO.PWM(PwmMotorA, 20)

    rightMotorAPWM.start(20)

    rightMotorAPWM.ChangeDutyCycle(20)


def runningMotorsForward():

    # Driving the motor Clockwise that is FORWARD
    GPIO.output(DirMotorA, HIGH)
    GPIO.output(DirMotorB, LOW)
    time.sleep(1)

def runningMotorsBackward():

    # Driving the motor Anti-Clockwise that is BACKWARD
    GPIO.output(DirMotorA, LOW)
    GPIO.output(DirMotorB, HIGH)
    time.sleep(1)


if __name__ == '__main__':

    try:

        with obstacleDataFile:

            editObstacleDataFile = csv.writer(obstacleDataFile)
            editObstacleDataFile.writerow(["Ultrasonic 1", "Ultrasonic 2", "Ultrasonic 3"])
            
            while True:

                distanceCalculatedBySensor1 = distanceBySensor1()
                print("Measured Distance 1 = %.1f cm" % int(abs(distanceCalculatedBySensor1)))
                time.sleep(1)

                distanceCalculatedBySensor2 = distanceBySensor2()
                print("Measured Distance 2 = %.1f cm" % int(distanceCalculatedBySensor2))
                time.sleep(1)

                distanceCalculatedBySensor3 = distanceBySensor3()
                print("Measured Distance 3 = %.1f cm" % int(distanceCalculatedBySensor3))

                
                # Saving obstacles distances under each specific sensors
                editObstacleDataFile.writerow([int(distanceCalculatedBySensor1), int(distanceCalculatedBySensor2), int(distanceCalculatedBySensor3)])
                
                time.sleep(1)

                # Running Motors

                if (distanceCalculatedBySensor1 <= 10):

                    # We need to stop the motors
                    GPIO.output(DirMotorA, LOW)
                    GPIO.output(DirMotorB, LOW)

                else:

                    runningMotorsPWM()
                    runningMotorsForward()




    except KeyboardInterrupt:
        print("Measurement stopped by User")
        file.close()
        GPIO.cleanup()
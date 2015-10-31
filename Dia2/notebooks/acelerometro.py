import android
import time

droid=android.Android()

dt = 100
fin = 3000

def getAccelerometerData():
    '''
        Simple function that reads the accelerometer sensor data
        and returns it as a dataframe
    '''
    
    tiempo = 0
    droid.startSensingTimed(2, dt)
    
    lectura = []
    
    while tiempo <= fin:
        accel_read.append(droid.sensorsReadAccelerometer().result)
        time.sleep(dt/1000.0)
        tiempo += dt
    
    droid.stopSensing();
    
    return lectura
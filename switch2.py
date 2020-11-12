#import gpio library
import datetime
import RPi.GPIO as GPIO
import time
#set gpio numbering mode and define input pin
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12,GPIO.OUT) #led 1
GPIO.setup(16,GPIO.OUT) #led 2
GPIO.setup(18,GPIO.OUT) #led 3
GPIO.setup(22,GPIO.OUT) #led 4
GPIO.setup(32,GPIO.OUT) #led 5
GPIO.setup(36,GPIO.OUT) #led 6
GPIO.setup(38,GPIO.OUT) #led 7 
GPIO.setup(40,GPIO.OUT) #led 8
GPIO.setup(33,GPIO.IN) #switch 1/2
GPIO.setup(11,GPIO.IN) #switch 3
GPIO.setup(13,GPIO.IN) #switch 4
GPIO.setup(15,GPIO.IN) #switch 5/6
GPIO.setup(29,GPIO.IN) #switch 7
GPIO.setup(31,GPIO.IN) #switch 8
GPIO.setup(35,GPIO.IN) #motion sensor 

def led1(jab):
    print (jab)
    while True:
            if GPIO.input(33)==0: #switch 1/2
               GPIO.output(12,True) #led 1
            else:
                print "CLOSED1"
                GPIO.output(12,False) #led 1
                break
    return;

def led2(jab):
    print (jab)
    while True:
            if GPIO.input(33)==0: #switch 1/2
               GPIO.output(16,True) #led 1
            else:
                print "CLOSED2"
                GPIO.output(16,False) #led 1
                break
    return;
def led3(lefthook):
    print (lefthook)
    while True:
            if GPIO.input(11)==0: #switch 3
               GPIO.output(18,True) #led 3
            else:
                print "CLOSED3"
                GPIO.output(18,False) #led 3
                break
    return;
def led4(righthook):
    print (righthook)
    while True:
            if GPIO.input(13)==0: #switch 4
               GPIO.output(22,True) #led 4
            else:
                print "CLOSED4"
                GPIO.output(22,False) #led 4
                break
    return;
def led5(jabbody):
    print (jabbody)
    while True:
            if GPIO.input(15)==0: #switch 5/6
               GPIO.output(32,True) #led 5
            else:
               print "CLOSED5"
               GPIO.output(32,False) #led 5
               break
    return;
def led6(jabbody):
    print (jabbody)
    while True:
            if GPIO.input(15)==0: #switch 5/6
               GPIO.output(36,True) #led 6
            else:
               print "CLOSED6"
               GPIO.output(36,False) #led 6
               break
    return;
def led7(lefthookbody):
    print (lefthookbody)
    while True:
            if GPIO.input(29)==0: #switch 7
               GPIO.output(38,True) #led 7
            else:
               print "CLOSED7"
               GPIO.output(38,False) #led 7
               break
    return;
def led8(righthookbody):
    print (righthookbody)
    while True:
            if GPIO.input(31)==0: #switch 8
               GPIO.output(40,True) #led 8
            else:
               print "CLOSED8"
               GPIO.output(40,False) #led 8
               break
    return;
def ms(dodge):
    print (dodge)
    while True:
            if GPIO.input(35)==0: #motion sensor
               GPIO.output(12,True) #led 1
               GPIO.output(16,True) #led 2
               GPIO.output(18,True) #led 3
               GPIO.output(22,True) #led 4
               GPIO.output(32,True) #led 5
               GPIO.output(36,True) #led 6
               GPIO.output(38,True) #led 7
               GPIO.output(40,True) #led 8
            else:
               print "CLOSED MS"
               GPIO.output(12,False) #led 1
               GPIO.output(16,False) #led 2
               GPIO.output(18,False) #led 3
               GPIO.output(22,False) #led 4
               GPIO.output(32,False) #led 5
               GPIO.output(36,False) #led 6
               GPIO.output(38,False) #led 7
               GPIO.output(40,False) #led 8
               break
    return;
 
            
print "Welcome to the smart punching bag!"
print "Tap the light to begin"
while True:
        if GPIO.input(33)==0: #switch 1/2
           GPIO.output(12,True) #led 1
           GPIO.output(16,True) #led 2
           GPIO.output(18,True) #led 3
           GPIO.output(22,True) #led 4
           GPIO.output(32,True) #led 5
           GPIO.output(36,True) #led 6
           GPIO.output(38,True) #led 7
           GPIO.output(40,True) #led 8
        else:
            print "CLOSED"
            GPIO.output(12,False) #led 1
            GPIO.output(16,False) #led 2
            GPIO.output(18,False) #led 3
            GPIO.output(22,False) #led 4
            GPIO.output(32,False) #led 5
            GPIO.output(36,False) #led 6
            GPIO.output(38,False) #led 7
            GPIO.output(40,False) #led 8
            break
start_time = time.time()

time.sleep(.5)
ms(5)
time.sleep(.5)
led2(5)
time.sleep(.5)
led1(5)
time.sleep(.5)
led3(5)
time.sleep(.5)

time.sleep(.5)
ms(5)
led4(5)
time.sleep(.5)
led5(5)
time.sleep(.5)
led6(5)
time.sleep(.5)
led7(5)
time.sleep(.5)
led8(5)start_time
time.sleep(.5)
ms(5)
time.sleep(.5)
ms(5)
time.sleep(.5)
ms(5)
time.sleep(3.5)
ms(5)
time.sleep(.5)
ms(5)

total_time= time.time() - start_time

today = datetime.date.today()
file.write(today.strftime('%b %d, %Y, '))

print  total_time," seconds took you to complete the combination"

file.write("%.4f seconds took you to complete the combination\n" % (total_time) )

file.close()

#finally:
#cleanup the GPIO
GPIO.cleanup()

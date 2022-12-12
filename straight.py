from Ax12 import Ax12
import time
import serial
#from Kinematics import angles


def motors(angles):

    #ser = serial.Serial('COM6', baudrate = 9600, timeout=.1)
    #time.sleep(2)
    #ser.write(b't 90,')


    # e.g 'COM3' windows or '/dev/ttyUSB0' for Linux
    Ax12.DEVICENAME = 'COM5'

    Ax12.BAUDRATE = 1_000_000

    # sets baudrate and opens com port
    Ax12.connect()

    # create AX12 instance with ID 2
    # motor homeposition 512 
    default_speed = 50

    motor_id1 = 2
    my_dxl1 = Ax12(motor_id1)  
    my_dxl1.set_moving_speed(default_speed)

    motor_id2 = 11
    my_dxl2 = Ax12(motor_id2)  
    my_dxl2.set_moving_speed(default_speed)

    data = [[512,512],[514,514],[516,516],[518,518],[520,520],[522,522],[530,530],[510,514],[508,516],[506,518],[500,524],[512,512]] #[M1 position, M2 position]
    data = [[512,512]]
    

    #translate from degrees to position values if needed: int(512+(1024/300)*angle)


    def main(motor_object1, motor_object2):
        """ sets goal position based on user input """
        #bool_test = True
        #while bool_test:
        motor_object1.set_goal_position(512)
        motor_object2.set_goal_position(512)

        while True:
            if ((motor_object1.get_present_position() in range (512-4, 512+4)) and (motor_object2.get_present_position() in range (512-4, 512+4))):
                break
        
        print("Position of dxl ID: %d is now: %d " %
                        (motor_object1.id, motor_object1.get_present_position()))

        print("\nPosition of dxl ID: %d is %d " %
                        (motor_object2.id, motor_object2.get_present_position()))

        for i, iangles in enumerate(angles): 
            for j, pointangles in enumerate(iangles):
                if j%10 == 0: 
                    # insert here the kinematics integration
                    print("\nPosition of dxl ID: %d is %d " %
                        (motor_object1.id, motor_object1.get_present_position()))
                    # desired angle input
                    #input_pos1 = int(input("goal pos: "))
                    input_pos1 = int((1024/300)*(pointangles[0][0]+60))
                    print(input_pos1)
                    my_dxl1.set_moving_speed(default_speed)
                    
                    print("Position of dxl ID: %d is now: %d " %
                        (motor_object1.id, motor_object1.get_present_position()))

                    print("\nPosition of dxl ID: %d is %d " %
                        (motor_object2.id, motor_object2.get_present_position()))

                    # desired angle input
                    #input_pos2 = int(input("goal pos: "))
                    input_pos2 = int((1024/300)*(pointangles[0][1]+60))

                    if(motor_object1.get_present_position()-input_pos1 == 0 ): #avoid 0 in denominator 
                        formula = default_speed
                    else:
                        formula = default_speed*(abs(motor_object2.get_present_position()-input_pos2))/abs(motor_object1.get_present_position()-input_pos1)
                    my_dxl2.set_moving_speed(int(formula))
                    print(formula)

                    #ser.write(b't 0,')
                    
                    motor_object1.set_goal_position(input_pos1)
                    motor_object2.set_goal_position(input_pos2)
                    time.sleep(1)


                    print ("while start here")
                    while True:
                        if ((motor_object1.get_present_position() in range (input_pos1-5, input_pos1+5)) and (motor_object2.get_present_position() in range (input_pos2-5, input_pos2+5))):
                            break
                    
                    #ser.write(b't 150,')
                    bool_test = True

    # pass in AX12 object
    main(my_dxl1, my_dxl2)


    # disconnect
    my_dxl1.set_torque_enable(0)
    my_dxl2.set_torque_enable(0)
    Ax12.disconnect()

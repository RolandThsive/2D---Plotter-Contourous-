from Ax12 import Ax12
import time
#from kinematics

# e.g 'COM3' windows or '/dev/ttyUSB0' for Linux
Ax12.DEVICENAME = 'COM5'

Ax12.BAUDRATE = 1_000_000

# sets baudrate and opens com port
Ax12.connect()

# create AX12 instance with ID 2
# motor homeposition 512 

motor_id1 = 2
my_dxl1 = Ax12(motor_id1)  
my_dxl1.set_moving_speed(50)

motor_id2 = 11
my_dxl2 = Ax12(motor_id2)  
my_dxl2.set_moving_speed(50)

data = [[200,500],[900,300]]

def user_input():
    """Check to see if user wants to continue"""
    ans = input('Continue? : y/n ')
    if ans == 'n':
        return False
    else:
        return True


def main(motor_object1, motor_object2):
    """ sets goal position based on user input """
    #bool_test = True
    #while bool_test:



    for x in data:
        # insert here the kinematocs integration
        print("\nPosition of dxl ID: %d is %d " %
            (motor_object1.id, motor_object1.get_present_position()))
        # desired angle input
        #input_pos1 = int(input("goal pos: "))
        input_pos1 = x[0]
        my_dxl1.set_moving_speed(50)
        
        print("Position of dxl ID: %d is now: %d " %
            (motor_object1.id, motor_object1.get_present_position()))

        print("\nPosition of dxl ID: %d is %d " %
            (motor_object2.id, motor_object2.get_present_position()))

        # desired angle input
        #input_pos2 = int(input("goal pos: "))
        input_pos2 = x[1]

        formula = 50*(abs(motor_object2.get_present_position()-input_pos2))/abs(motor_object1.get_present_position()-input_pos1)
        my_dxl2.set_moving_speed(int(formula))
        print(formula)

        motor_object1.set_goal_position(input_pos1)
        motor_object2.set_goal_position(input_pos2)

        print ("while start here")
        while True:
            if ((motor_object1.get_present_position() in range (input_pos1-5, input_pos1+5)) and (motor_object2.get_present_position() in range (input_pos2-5, input_pos2+5))):
                break
                
        #time.sleep(2)

        bool_test = True

# pass in AX12 object
main(my_dxl1, my_dxl2)


# disconnect
my_dxl1.set_torque_enable(0)
my_dxl2.set_torque_enable(0)
Ax12.disconnect()

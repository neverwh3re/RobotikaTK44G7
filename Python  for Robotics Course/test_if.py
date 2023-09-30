#Muhammad Ismail Ibadurrahman_1103204239
from robot_control_class import RobotControl
#Refer Fungsi RobotControl dari librarynya
robotcontrol = RobotControl()
#Deklarasi variabel robotcontrol, refer Fungsi RobotControl dari librarynya
a = robotcontrol.get_laser(360)
#Deklarasi variabel a, refer Fungsi get_laser dari librarynya
if a < 1:#looping kondisi a < 1
    robotcontrol.stop_robot()#instruksi stop robot apabila kondisi terpenuhi

else:
    robotcontrol.move_straight()#instruksi robot jalan apabila kondisi terpenuhi

print ("The laser value received was: ", a)#output value a berapa
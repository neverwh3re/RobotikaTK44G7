#Muhammad Ismail Ibadurrahman_1103204239

from robot_control_class import RobotControl

robotcontrol = RobotControl()
#Refer Fungsi RobotControl dari librarynya

laser1 = robotcontrol.get_laser(0)
#deklarasi variabel laser 1 dengan fungsi yang ada didalam library robotcontrol dengan parameter 0 *derajat
print ("The laser value received is: ", laser1)
#print output laser1
laser2 = robotcontrol.get_laser(360)
#deklarasi variabel laser 1 dengan fungsi yang ada didalam library robotcontrol 360 *derajat
print ("The laser value received is: ", laser2)
#print output laser2
laser3 = robotcontrol.get_laser(719)
#deklarasi variabel laser 1 dengan fungsi yang ada didalam library robotcontrol 719 *derajat
print ("The laser value received is: ", laser3)
#print output variabel laser3
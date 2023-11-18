#Muhammad Ismail Ibadurrahman_1103204239
from robot_control_class import RobotControl

rc = RobotControl()
#Refer Fungsi RobotControl dari librarynya
l = rc.get_laser_full()
#deklarasi variabel l dengan fungsi yang ada didalam library robotcontrol
print ("Position 0: ", l[0])
#print output l parameter 0 *derajat
print ("Position 360: ", l[360])
#print output l parameter 360 *derajat
print ("Position 719: ", l[719])
#print output l parameter 719 *derajat

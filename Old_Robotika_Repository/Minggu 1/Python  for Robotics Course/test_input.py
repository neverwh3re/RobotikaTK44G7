#Muhammad Ismail Ibadurrahman_1103204239
from robot_control_class import RobotControl

num = int(input("Select a number between 0 and 719: "))
#deklarasi input integer
rc = RobotControl()
#deklarasi variabel rc dgn fungsi dari library robotcontrol
a = rc.get_laser(num)
#deklarasi variabel a dgn fungsi dr library dan parameter num
print ("The laser value received is: ", a)
#output saat variabel a dipanggil
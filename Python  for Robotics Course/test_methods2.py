#Muhammad Ismail Ibadurrahman_1103204239
from robot_control_class import RobotControl
#Refer Fungsi RobotControl dari librarynya
robotcontrol = RobotControl(robot_name="summit")
#Deklarasi variabel robotcontrol, refer Fungsi RobotControl dari librarynya dan memberi nama robotnya summit
def get_laser_values(a,b,c):#deklarasi fungsi dgn parameter yg dibutuhkan a,b,c
    r1 = robotcontrol.get_laser_summit(a)#Deklarasi variabel r1, refer fungsi get_laser_control dari lib RobotControl dan memberi nama robotnya summit
    r2 = robotcontrol.get_laser_summit(b)#Deklarasi variabel r2, refer Fungsi get_laser_control dari lib RobotControl dan memberi nama robotnya summit
    r3 = robotcontrol.get_laser_summit(c)#Deklarasi variabel r3, refer Fungsi get_laser_control dari lib RobotControl dan memberi nama robotnya summit

    return [r1, r2, r3]#mengembalikan value r1, r2, r3

l = get_laser_values(0, 500, 1000)
#Deklarasi variabel l dengan value fungsi get_laser_values yg dibuat barusan dengan parameter 0, 500, 1000
print ("Reading 1: ", l[0])#cetak value l dari data bergantung parameter 1
print ("Reading 2: ", l[1])#cetak value l dari data bergantung parameter 2
print ("Reading 3: ", l[2])#cetak value l dari data bergantung parameter 3
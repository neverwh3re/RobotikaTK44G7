from robot_control_class import RobotControl
#import library, fungsi RobotControl dari class robot control
rc = RobotControl()
#Deklarasi variabel rc, refer Fungsi RobotControl dari librarynya
l = rc.get_laser_full()
#deklarasi variabel l dengan fungsi yang ada didalam library robotcontrol
dict = {"P0": l[0], "P100": l[100], "P200": l[200], "P300": l[300], "P400": l[400], "P500": l[500], "P600": l[600], "P719": l[719]}
#deklarasi variabel lists dgn nama dict dengan parameter variasi derajatnya
print (dict)
#output saat variabel lists dict dipanggil
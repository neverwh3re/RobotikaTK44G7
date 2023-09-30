#Muhammad Ismail Ibadurrahman_1103204239
from robot_control_class import RobotControl
#Refer Fungsi RobotControl dari librarynya
robotcontrol = RobotControl()
#Deklarasi variabel robotcontrol, refer Fungsi RobotControl dari librarynya
l = robotcontrol.get_laser_full()
#Deklarasi variabel l, refer Fungsi get_laser_full dari librarynya
maxim = 0
#Deklarasi variabel maxim dengan value 0
for value in l:#pengulangan dengan iterasi bergantung pada variabel l
    if value > maxim: #apabila kondisi value > maxim lanjut instruksi
        maxim = value #nilai maxim = value

print ("The higher value in the list is: ", maxim)
#cetak output value 
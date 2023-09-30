#Muhammad Ismail Ibadurrahman_1103204239
from robot_control_class import RobotControl
#Refer Fungsi RobotControl dari librarynya
robotcontrol = RobotControl()
#Deklarasi variabel robotcontrol, refer Fungsi RobotControl dari librarynya
a = robotcontrol.get_laser(360)
#Deklarasi variabel a, refer Fungsi get_laser dari librarynya
while a > 1:#looping kondisi a > 1
    robotcontrol.move_straight()#instruksi maju lurus robot apabila kondisi terpenuhi
    a = robotcontrol.get_laser(360)#instruksi deteksi dgn 360derajat robot apabila kondisi terpenuhi
    print ("Current distance to wall: %f" % a)#cetak jarak robot ke dinding dgn variabel parameter a

robotcontrol.stop_robot()
#instruksi robot berhenti apabila kondisi tidak terpenuhi
print ("Wall is at %f meters! Stop the robot!" % a)
#cetak jarak dinding dgn parameter a
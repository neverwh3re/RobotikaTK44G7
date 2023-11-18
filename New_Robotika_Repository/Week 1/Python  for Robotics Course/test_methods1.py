#Muhammad Ismail Ibadurrahman_1103204239
from robot_control_class import RobotControl
#Refer Fungsi RobotControl dari librarynya
import time
#import library time agar bisa memakai fungsinya
robotcontrol = RobotControl(robot_name="summit")
#Deklarasi variabel robotcontrol, refer Fungsi RobotControl dari librarynya dan memberi nama robotnya summit
def move_x_seconds(secs):#deklarasi fungsi dgn parameter yg dibutuhkan detik
    robotcontrol.move_straight()#panggil fungsi robot dr library agar bergerak lurus
    time.sleep(secs)#panggil sleep dari library time agar terhenti slm waktu yg ditentukan
    robotcontrol.stop_robot()#panggil fungsi robot dr library agar robot stop


move_x_seconds(5)
#panggil fungsi yg barusan dibuat dengan parameter waktu 5 detik
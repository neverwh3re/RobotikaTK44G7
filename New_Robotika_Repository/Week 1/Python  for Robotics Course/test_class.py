#Muhammad Ismail Ibadurrahman_1103204239
from robot_control_class import RobotControl
#Refer Fungsi RobotControl dari librarynya
class MoveRobot:
    def __init__(self, motion, clockwise, speed, time): #deklarasi variabel class inisiasi dgn parameter seperti yg tertulis
        self.robotcontrol = RobotControl(robot_name="summit")#deklarasi variabel robotcontrol dengan value robotcontrol fungsi dari library RobotControl agar robot diberi nama jd summit
        self.motion = motion#deklarasi variabel motion dengan value motion fungsi dari library RobotControl
        self.clockwise = clockwise#deklarasi variabel clockwise dengan value clockwise fungsi dari library RobotControl
        self.speed = speed#deklarasi variabel speed dengan value speed fungsi dari library RobotControl
        self.time = time#deklarasi variabel time dengan value time fungsi dari library RobotControl
        self.time_turn = 7.0 # This is an estimate time in which the robot will rotate 90 degrees

    def do_square(self):#deklarasi fungsi do_square

        i = 0#deklarasi i untuk iterasi dengan nilai 0

        while (i < 4):#deklarasi pengulangan dengan kondisi i<4
            self.move_straight()#pemanggilan fungsi maju dari class yang sudah dibuat
            self.turn()#pemanggilan fungsi belok dari class yang sudah dibuat
            i+=1#iterasi +1

    def move_straight(self):#deklarasi fungsi maju
        self.robotcontrol.move_straight_time(self.motion, self.speed, self.time)#deklarasi variabel maju dengan parameter tertentu agar robot berjalan sesuai keinginan

    def turn(self):#deklarasi fungsi belok
        self.robotcontrol.turn(self.clockwise, self.speed, self.time_turn)#deklarasi variabel belok dengan parameter tertentu agar robot berjalan sesuai keinginan


mr1 = MoveRobot('forward', 'clockwise', 0.3, 4)#deklarasi variabel mr1 untuk menjalankan robot dengan parameter tertentu
mr1.do_square()#panggil fungsi do_square setelah variabel mr1 agar parameter ter attach
mr2 = MoveRobot('forward', 'clockwise', 0.3, 8)#deklarasi variabel mr2 untuk menjalankan robot dengan parameter tertentu
mr2.do_square()#panggil fungsi do_square setelah variabel mr2 agar parameter ter attach
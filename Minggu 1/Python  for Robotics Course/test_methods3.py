#Muhammad Ismail Ibadurrahman_1103204239
from robot_control_class import RobotControl
#Refer Fungsi RobotControl dari librarynya
robotcontrol = RobotControl(robot_name="summit")
#Deklarasi variabel robotcontrol, refer fungsi robotcontrol dari lib RobotControl dan memberi nama robotnya summit
robotcontrol.move_straight_time("forward", 0.3, 5)
#panggil fungsi move_straight_time dari lib RobotControl dan memberi parameter string maju, 0,3, 5
robotcontrol.turn("clockwise", 0.3, 7)
#panggil fungsi belok dengan parameter arah putar jam dan 0,3, 7
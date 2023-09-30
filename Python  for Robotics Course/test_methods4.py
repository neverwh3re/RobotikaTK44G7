#Muhammad Ismail Ibadurrahman_1103204239

from robot_control_class import RobotControl
#Refer Fungsi RobotControl dari librarynya
robotcontrol = RobotControl(robot_name="summit")
#Deklarasi variabel robotcontrol, refer fungsi robotcontrol dari lib RobotControl dan memberi nama robotnya summit
robotcontrol.turn("counter-clockwise", 0.3, 4)
#memberi perintah pada robot dari fungsi yang ada didalam library robotcontrol untuk belok dan dgn parameter tertulis
robotcontrol.move_straight_time("forward", 0.3, 6)
#memberi perintah pada robot dari fungsi yang ada didalam library robotcontrol untuk maju dan dgn parameter tertulis
robotcontrol.turn("counter-clockwise", 0.3, 4)
#memberi perintah pada robot dari fungsi yang ada didalam library robotcontrol untuk belok dan dgn parameter tertulis
robotcontrol.move_straight_time("forward", 0.3, 7)
#memberi perintah pada robot dari fungsi yang ada didalam library robotcontrol untuk maju dan dgn parameter tertulis
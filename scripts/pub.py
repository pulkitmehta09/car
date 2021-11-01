#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import Float64

def talker():
    pub_right = rospy.Publisher('/car/fr_steer_joint_effort_controller/command', Float64, queue_size=10) # Add your topic here between ''. Eg '/my_robot/steering_controller/command'
    pub_left = rospy.Publisher('/car/fl_steer_joint_effort_controller/command', Float64, queue_size=10)
    pub_move = rospy.Publisher('/car/rear_axle_joint_velocity_controller/command', Float64, queue_size=10) # Add your topic for move here '' Eg '/my_robot/longitudinal_controller/command'
    rospy.init_node('pub', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    control_speed = 2
    control_turn = 5
    while not rospy.is_shutdown():
        hello_str = "Circular motion %s" % rospy.get_time()
        rospy.loginfo(hello_str)
        pub_move.publish(control_speed)
        pub_left.publish(control_turn)
        pub_right.publish(control_turn)        
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass


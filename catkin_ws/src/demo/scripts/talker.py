#!/usr/bin/env python
# license removed for brevity
import rospy
from geometry_msgs.msg import Twist

def reset(vel_msg):
    vel_msg.linear.x = 0
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0

def move():
    # Starts a new node
    rospy.init_node('turtle', anonymous=True)
    velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()

    move_speed = 0.01
    turn_speed = 0.01
    move_amount = 0.01
    turn_amount = 0.01

    #Since we are moving just in x-axis
    reset(vel_msg)

    while not rospy.is_shutdown():

        #Receiveing the user's input
        print("Let's move your robot")
        str_in = raw_input("Input a direction (wasd):")

        for dir in str_in:
            reset(vel_msg)
            t0 = rospy.Time.now().to_sec()
            speed = 0
            #Setting the current time for distance calculus
            current_distance = 0
            current_angle = 0

            if dir == "w" or dir == "s":
                if dir == "w": vel_msg.linear.x = move_speed; speed = move_speed
                if dir == "s": vel_msg.linear.x = -move_speed; speed = -move_speed

                #Loop to move the turtle in an specified distance
                while current_distance < move_amount:
                    #Publish the velocity
                    velocity_publisher.publish(vel_msg)
                    #Takes actual time to velocity calculus
                    t1=rospy.Time.now().to_sec()
                    #Calculates distancePoseStamped
                    current_distance = abs(speed)*(t1-t0)
                #After the loop, stops the robot
                vel_msg.linear.x = 0
                #Force the robot to stop
                velocity_publisher.publish(vel_msg)

            elif dir == "a" or dir == "d":
                if dir == "a": vel_msg.angular.z = turn_speed; speed = turn_speed
                if dir == "d": vel_msg.angular.z = -turn_speed; speed = -turn_speed

                #Loop to turn the turtle
                while current_angle < turn_amount:
                    #Publish the velocity
                    velocity_publisher.publish(vel_msg)
                    #Takes actual time to velocity calculus
                    t1=rospy.Time.now().to_sec()
                    #Calculates distancePoseStamped
                    current_angle = abs(speed)*(t1-t0)
                #After the loop, stops the robot
                vel_msg.angular.z = 0
                #Force the robot to stop
                velocity_publisher.publish(vel_msg)

if __name__ == '__main__':
    try:
        #Testing our function
        move()
    except rospy.ROSInterruptException: pass


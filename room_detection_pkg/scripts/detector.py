#!/usr/bin/env python3

import rospy
from darknet_ros_msgs.msg import BoundingBoxes
from std_msgs.msg import String
from coordination_msgs.msg import InitialCoordination

class RoomDetectionHandler:
    global room_dictionary
    global room_initial_coordinates
    room_dictionary = {"diningtable":"room1", "person":"room2", "sofa":"room3", "microwave":"room4","suitcase":"room5","hydrant":"room6"}
    room_initial_coordinates = {
        'room1': {'posx' : 10.0, 'posy' : 20.0, 'orix': 5.0, 'oriy': 6.0 , 'oriz': 15.0, 'oriw': 8.0},
        'room2': {'posx' : 1.0, 'posy' : 21.0, 'orix': 6.0, 'oriy': 8.0 , 'oriz': 14.0, 'oriw': 4.0},
        'room3': {'posx' : 5.0, 'posy' : 22.0, 'orix': 7.0, 'oriy': 5.0 , 'oriz': 13.0, 'oriw': 0.0},
        'room4': {'posx' : 8.0, 'posy' : 23.0, 'orix': 8.0, 'oriy': 4.0 , 'oriz': 18.0, 'oriw': 1.0},
        'room5': {'posx' : 7.0, 'posy' : 24.0, 'orix': 9.0, 'oriy': 3.0 , 'oriz': 19.0, 'oriw': 7.0},
        'room6': {'posx' : 9.0, 'posy' : 25.0, 'orix': 10.0, 'oriy': 2.0 , 'oriz': 19.0, 'oriw': 3.0}
    }
    def __init__(self):
        self.boundingBoxSubscriber = rospy.Subscriber("darknet_ros/bounding_boxes", BoundingBoxes, self.bounding_box_callback)
        self.objectNamePublisher = rospy.Publisher("detected_room", String, queue_size=10)
        self.roomCoordinationPublisher = rospy.Publisher("detected_initial_coordinates", InitialCoordination, queue_size=10)

    def bounding_box_callback(self, msg):
        for bbox in msg.bounding_boxes:
            class_label = bbox.Class
            class_label_string = str(class_label)
            self.objectNamePublisher.publish("Detected room for map and odometry values: {}".format(room_dictionary[class_label_string]))
            roomCoordinationMsg = InitialCoordination()
            roomCoordinationMsg.posy = room_initial_coordinates[room_dictionary[class_label_string]]['posy']
            roomCoordinationMsg.orix = room_initial_coordinates[room_dictionary[class_label_string]]['orix']
            roomCoordinationMsg.posx = room_initial_coordinates[room_dictionary[class_label_string]]['posx']
            roomCoordinationMsg.oriy = room_initial_coordinates[room_dictionary[class_label_string]]['oriy']
            roomCoordinationMsg.oriz = room_initial_coordinates[room_dictionary[class_label_string]]['oriz']
            roomCoordinationMsg.oriw = room_initial_coordinates[room_dictionary[class_label_string]]['oriw']
            self.roomCoordinationPublisher.publish(roomCoordinationMsg)
            


if __name__ == '__main__':
    try:
        rospy.init_node('room_detector_publisher_node', anonymous=True)
        room_detection_handler = RoomDetectionHandler()
        rospy.spin()

    except rospy.ROSInterruptException:
        pass
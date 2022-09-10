'''
Class for handling the webcam

author: @DanielNowak98
'''

import cv2

class Webcam:
    def __init__(self):
        self.device_id = self.find_working_webcam()
        self.cap = self.get_webcam_feed()

    def find_working_webcam(self):
        """
        Finds the first working webcam.
        """
        for device_id in range(10):
            cap = cv2.VideoCapture(device_id)
            if cap.isOpened():
                cap.release()
                return device_id
        return -1

    def get_webcam_feed(self):
        """
        Returns the webcam feed.
        """
        cap = cv2.VideoCapture(self.device_id)
        return cap
    
    def show_webcam_feed(self, window_name='webcam'):
        """
        Shows the webcam feed in a window.
        """
        cv2.namedWindow(window_name)
        while True:
            ret, frame = self.cap.read()
            cv2.imshow(window_name, frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        self.cap.release()
        cv2.destroyAllWindows()
    
    def get_frame(self):
        """
        Returns the current frame.
        """
        frame = self.cap.read()
        return frame


    

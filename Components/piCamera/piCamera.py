import picamera
from time import sleep

#new camera object
camera = picamera.PiCamera()

#Start a video feed
#camera.start_preview()

#tak a picture
#camera.capture('image1.jpg')
#sleep(5)
#camera.capture('image2.jpg')


#Record a video
camera.start_recording('video.h264')
sleep(5)
camera.stop_recording()

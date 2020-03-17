from picamera import PiCamera
from time import sleep
import subprocess

#Specify load and save paths.
film_name = 'film.h264'
save_name = 'scan'

#Capture video.
cam = PiCamera()
cam.start_preview()
cam.start_recording(film_name)
sleep(3)
cam.stop_recording()
cam.stop_preview()

#Convert to mp4 format.
command = "MP4Box -add {} {}.mp4".format(film_name, save_name)
try:
    output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
except subprocess.CalledProcessError as e:
    print('FAIL:\ncmd:{}\noutput:{}'.format(e.cmd, e.output))

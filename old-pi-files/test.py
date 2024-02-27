import subprocess

#vlc -f --play-and-exit /path/video.avi

result = subprocess.run(["export", "DISPLAY=:0","cvlc", "-f","--play-and-exit","TSN_test3.mp4"])
 #DISPLAY=:0 cvlc -f --play-and-exit TSN_test3.mp4
#sudo -u localreachbeta  cvlc --qt-fullscreen-screennumber=1 --alsa-audio-device hw:1,0 TSN_test3.mp4

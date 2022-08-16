import time, threading, os, pyautogui

def openFirefox():
	os.system('firefox https://www.youtube.com/feed/subscriptions')
#def openVlc():
	#os.system('vlc -Z /home/l/Music/"Work Playlist"/work-playlist.m3u')
def openRhythmbox():
	os.system('rhythmbox-client --no-present /home/l/Music/"Work Playlist"/work-playlist.m3u --set-volume=20 --play')
def manageRhythmbox():
	pyautogui.keyDown('ctrl')
	pyautogui.press('p')
	pyautogui.keyUp('ctrl')
	pyautogui.keyDown('ctrl')
	pyautogui.press('q')
	pyautogui.keyUp('ctrl')
def enableIptables():
	os.system('sudo iptables-restore <  /home/l/Security/Iptables/iptables-desktop-lenovo')

threading.Thread(target=openFirefox).start()
threading.Thread(target=openRhythmbox).start()
threading.Thread(target=enableIptables).start()

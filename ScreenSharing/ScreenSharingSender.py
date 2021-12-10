from vidstream import ScreenShareClient
import threading

sender = ScreenShareClient(r'192.168.10.1',9999)
sender.start_stream()

t = threading.Thread(target=sender.start_stream)
t.start()

while input("") != 'STOP':
    continue

sender.stop_stream()
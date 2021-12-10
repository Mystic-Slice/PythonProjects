from vidstream import StreamingServer
import threading

receiver = StreamingServer(r'192.168.10.1',9999)

t = threading.Thread(target=receiver.start_server)
t.start()

while input("") != 'STOP':
    continue

receiver.stop_server()
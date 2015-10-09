import socket
import time
import os

ip_port = ('',2727)

soc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
soc.bind(ip_port)
print 'Waiting for connection'
soc.listen(1)
dat,inf = soc.accept()
print 'Connected to: '+str(inf)
print ' '

def send_list():
    def fileList():
        def getF():
            fileL = os.walk(os.getcwd())
            for x in fileL:
                yield x
        f = getF()
        fff = f.next()[2]
        if '01_SEND.py' in fff:
            fff.remove('01_SEND.py')
        if '00_GET.py' in fff:
            fff.remove('00_GET.py')
        return fff
    def list_to_text(my_list):
        y = ''
        for x in my_list:
            y = y+'*'+str(x)
        return y
    #Convert to text
    file_list = fileList()
    return list_to_text(file_list)
file_list = send_list()
if file_list == '':
    print 'Nothing to send'
    file_list = 'NOTHINg_To_SeNd'
dat.sendall(file_list)
#print 'File list sent'
print ' '
##########################################
while True: # Inner loop
    data = dat.recv(1024)
    cmd = data[:data.find('\n')]

    if cmd == 'get':
        x, file_name, x = data.split('\n', 2)
        dat.sendall('ok')
        with open(file_name, 'rb') as f:
            data = f.read()
        dat.sendall('%16d' % len(data))
        dat.sendall(data)
        print 'Sent: '+str(file_name)
        print ' '
        os.remove(file_name)
        dat.recv(2)

    elif cmd == 'end':
        print 'Done'
        #print 'Closing connection'
        dat.close()
        soc.close()
        break
    else:
        print 'ERROR: Problem with connection'
        dat.close()
        soc.close()
        break




print 'Connection closed'
print ' '
zzz = raw_input('Press ENTER to close window')

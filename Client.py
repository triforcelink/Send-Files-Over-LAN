import socket
import time
import hashlib

#Who do you want to connect to?

ip = '192.168.1.6'

ip_port = (ip,2727)

soc = socket.socket()
try:
    soc.connect(ip_port)
    con = True
except:
    print 'Could not connect'
    con = False

def get_list():
    print 'Connected to: '+str(ip_port)
    print ' '
    file_list = soc.recv(1024)
    file_list = file_list.split('*')
    if file_list == 'NOTHINg_To_SeNd':
        #print 'shame'
        print 'Nothing to receive'
        print ' '
        return False
    elif len(file_list) <= 1:
        #print 'List appears to be too short'
        print 'Nothing to receive'
        print ' '
        return False
    elif file_list == '':
        print 'Nothing to receive'
        print ' '
        return False
    elif file_list[0] == '':
        return file_list[1:]
    else:
        print 'Problem..'
        return False

def get_file(file_name):
    """Required: socket,time. var examples:
    file_name = 'f1.mp4'
    """
    tries = 0
    def get_it(file_name=file_name):
        try:
            cmd = 'get\n%s\n' % (file_name)
            soc.sendall(cmd)
            r = soc.recv(2)
            size = int(soc.recv(16))
            #print str(file_name)+': '+str(size)+' bytes'
            recvd = 0
            fObj = open(file_name,'wb')
            m = hashlib.md5()#hash
            while size > recvd:
                data = soc.recv(1024)
                fObj.write(data)
                m.update(data)#hash
                if not data:
                    break
                recvd += len(data)
            soc.sendall('ok')
            fObj.close()
        except:
            time.sleep(1)
            return False
        #Check if all the data was received
        if recvd == size:
            #print 'file: '+str(file_name)+' has been saved!'
            #return True
            return m.hexdigest()#hash
        else:
            return False
        
    while True:
        tries = tries + 1
        m = get_it(file_name)
        if m:
            print 'Success: '+str(file_name)+' '+str(m)
            print ' '
            break
        elif tries > 2:
            print 'Failed: '+str(file_name)
            print ' '
            break
        else:
            print 'Problem with '+str(file_name)+' Trying again...'
            print ' '


if con:
    fileeeee_list = get_list()
    if fileeeee_list:
        for x in fileeeee_list:
            get_file(x)
    cmd = 'end\n'
    soc.sendall('end\n')
    print 'Done'
    soc.close()
    print 'Connection closed'
print ' '
zzz = raw_input('Press ENTER to close window')


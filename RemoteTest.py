import paramiko
import sys

class sampleParamiko:
    ssh = ""
    def __init__(self, host_ip, uname, passwd):
        try:
            self.ssh = paramiko.SSHClient()
            self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.ssh.connect(host_ip, username=uname, password=passwd)
            #print "In init function"
        except (paramiko.BadHostKeyException, paramiko.AuthenticationException,     paramiko.SSHException) as e:
            print(str(e))
            sys.exit(-1)

    def ececuteCmd(self,cmd):
        try:
            channel = self.ssh.invoke_shell()
            timeout = 60 # timeout is in seconds
            channel.settimeout(timeout)
            newline        = '\r'
            line_buffer    = ''
            channel_buffer = ''
            channel.send(cmd + ' ; exit ' + newline)
            while True:
                channel_buffer = channel.recv(1).decode('UTF-8')
                if len(channel_buffer) == 0:
                    break 
                channel_buffer  = channel_buffer.replace('\r', '')
                if channel_buffer != '\n':
                    line_buffer += channel_buffer
                else:
                    print(line_buffer)
                    line_buffer   = ''
        except paramiko.SSHException as e:
            print(str(e))
            sys.exit(-1)
host_ip = "70.42.161.157"
uname = "root"
password = "Password123"
cmd = str(input("Enter the command to execute in the host machine: "))
conn_obj = sampleParamiko(host_ip, uname, password)
conn_obj.ececuteCmd(cmd)
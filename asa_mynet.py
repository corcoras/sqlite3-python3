import os
from netmiko import ConnectHandler, SCPConn, FileTransfer
class my_netmiko:
    def __init__(self, ip, username, password, cmdlist):
    #def __init__(self, ip, username, password, cmdlist):
        self.ip = ip
        self.username = username
        self.password = password
        #self.myfile = myfile
        self.cmdlist = cmdlist
    def main(self):
        ssh_conn = ConnectHandler(
            device_type='cisco_asa',
            ip = self.ip,
            username = self.username,
            password = self.password
        )
        static = os.chdir('C:\\Users\corcoras\\Desktop\\FY14 INSTALLS\\PythonMotors\\netmiko_django\\netmiko_django\\static')
        myfile = os.listdir(static)
        for f in myfile:
            s_file = f
            d_file = f
            scp_conn = SCPConn(ssh_conn)
            scp_conn.scp_transfer_file(s_file, d_file)
        config_commands = self.cmdlist
        output = ssh_conn.send_config_set(config_commands)
        print(output)
        return output
        scp_conn.close()


#myfile = ['hello.txt', 'hello.1.txt', 'hello.2.txt', 'hello.3.txt']
#cmd = [ 'exit',
#        'sho ip inter brief',
 #       'show ver',
 #       'show flash:' ]
#x = my_netmiko('172.16.77.199', 'liam', 'Fender7797', myfile, cmd)
#x.main()



#myfile = ['hello.txt', 'hello.1.txt', 'hello.2.txt', 'hello.3.txt']
cmd = [ 'sho ip',
       'show ver',
       'show flash:' ]
x = my_netmiko('205.190.196.218', 'corcoras', 'F3nd3r1209', cmd)
z = x.main()
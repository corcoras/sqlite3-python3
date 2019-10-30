import os
from netmiko import ConnectHandler, SCPConn
#set this up if connecting to outside interface
#ip access-list extended INTERNET_IN
 #bla bla
 #permit tcp any any eq 22
 #permit tcp any eq 22 any
class my_netmiko:
    def __init__(self, ip, username, password, cmdlist):
        self.ip = ip
        self.username = username
        self.password = password
        #self.myfile = myfile
        self.cmdlist = cmdlist
    def main(self):
        ssh_conn = ConnectHandler(
            device_type='cisco_ios',
            ip = self.ip,
            username = self.username,
            password = self.password
        )
        static = os.chdir('C:\\Users\\corcoras\\netmiko_django\\hold')
        print(static)
        myfile = os.listdir(static)
        print(myfile)
        for f in myfile:
            if f == 'desktop.ini':
                pass
            else:
                print(f)
                s_file = f
                d_file = f
                scp_conn = SCPConn(ssh_conn)
                scp_conn.scp_transfer_file(s_file, d_file)
        config_commands = self.cmdlist
        output = ssh_conn.send_config_set(config_commands)
        print(output)
        return output
        scp_conn.close()



cmd = [ 'exit',
       'show flash:' ]
x = my_netmiko('205.190.196.221', 'corcoras', 'F3nd3r1209',  cmd)
x.main()



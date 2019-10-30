>>>
>>> net = c.listip()
>>> len(net)
62
>>>
>>>
>>>
>>> net
['204.125.25.193', '204.125.25.194', '204.1
204.125.25.204', '204.125.25.205', '204.125
4.125.25.215', '204.125.25.216', '204.125.2
125.25.226', '204.125.25.227', '204.125.25.
5.25.237', '204.125.25.238', '204.125.25.23
25.248', '204.125.25.249', '204.125.25.250'
>>>

>>>
>>> newlist = []
>>> count = 0
>>> while count < len(net):
...     newlist.append('')
...     count += 1
...
>>> len(newlist)
62

 newdict = dict(zip(net, newlist)
... )
>>> print(newdict)
{'204.125.25.193': '', '204.125.25.194': '', '204.1
204.125.25.202': '', '204.125.25.203': '', '204.125
4.125.25.211': '', '204.125.25.212': '', '204.125.2
125.25.220': '', '204.125.25.221': '', '204.125.25.
5.25.229': '', '204.125.25.230': '', '204.125.25.23
25.238': '', '204.125.25.239': '', '204.125.25.240'
.247': '', '204.125.25.248': '', '204.125.25.249':
>>>

-------------------------
Device ID: s7-71064423.nis.cdk.com
Entry address(es): 
  IP address: 205.190.182.116
Platform: cisco WS-C2960X-24PD-L,  Capabilities: Switch IGMP 
Interface: GigabitEthernet3/0/45,  Port ID (outgoing port): GigabitEthernet1/0/25
Holdtime : 155 sec

Version :
Cisco IOS Software, C2960X Software (C2960X-UNIVERSALK9-M), Version 15.0(2a)EX5, RELEASE SOFTWARE (fc3)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2015 by Cisco Systems, Inc.
Compiled Mon 16-Feb-15 08:16 by prod_rel_team

advertisement version: 2
Protocol Hello:  OUI=0x00000C, Protocol ID=0x0112; payload len=27, value=00000000FFFFFFFF010221FF000000000000F07816F44980FF0000
VTP Management Domain: ''
Native VLAN: 1
Duplex: full
Power Available TLV:

    Power request id: 0, Power management id: 1, Power available: 0, Power management level: -1
Management address(es): 
  IP address: 205.190.182.116

-------------------------



devices = {'Device ID': ''}
lines = data.split('\n')
for i in lines:
    if 'Device ID' in i:
        strdevice = i.split(':')
        print(strdevice[1:])
        devices['Device ID'] = i.split(':')[1:]




import sqlite3

conn = sqlite3.connect('myipnetwork.db') 
c = conn.cursor()
c.execute('''CREATE TABLE NETWORK
             ([generated_id] INTEGER PRIMARY KEY,
             [cmf] text,
             [name] text,
             [device_id] text,
             [ip_address] text,
             [platform] text,
             [local_interface] text,
             [remote_interface] text)
              ''')
          
sqlite_insert_query = """INSERT INTO `NETWORK`
                          ( 
                        'cmf',
                        'name',
                        'device_id',
                        'ip_address',
                        'platform',
                        'local_interface',
                        'remote_interface'     
                             ) 
                           VALUES 
                          (
                        '29012901',
                        'sullivan pontiac',
                        's1.sullivan-pont.langley',
                        '204.125.25.193',
                        'Cisco 3560',
                        'G0/0/10',
                        'G/0/0/23')  
                          """

c.execute(sqlite_insert_query)          
conn.commit()

INSERT INTO table (column1,column2 ,..)
VALUES( value1,    value2 ,...);
#!/usr/bin/python

from subprocess import call, check_call, check_output
from mininet.net import Mininet
from mininet.node import Node, OVSKernelSwitch, Host, RemoteController, UserSwitch, Controller
from mininet.link import Link, Intf, TCLink, TCULink
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from functools import partial
import sys, time
flush=sys.stdout.flush
import os, string

class cd:
    """Context manager for changing the current working directory"""
    def __init__(self, newPath):
        self.newPath = os.path.expanduser(newPath)

    def __enter__(self):
        self.savedPath = os.getcwd()
        os.chdir(self.newPath)

    def __exit__(self, etype, value, traceback):
        os.chdir(self.savedPath)


def WifiNet(n, m, IP, linkconfig, req, cap, mod,ts):
    print(IP)
    #link=partial(TCLink,delay='2ms',bw=10)
    #net.addController('c0',controller=Controller,link=link)
    net = Mininet(link=TCLink, controller= None, autoSetMacs = True)
    #net = Mininet(switch=OVSKernelSwitch)

    """ Node names """
    hosts = []
    switches = []
    links = []
    hosts.append('dest')
    sw_name=[]
    for i in range(1,16):
        sw_name.append('0'+hex(i)[-1])
    for i in range(16,60):
        sw_name.append(hex(i)[-2:])
    for i in range(1, n+1):
        hosts.append('ship'+str(i))
    for i in range(1, n+m+2):
        switches.append('s'+str(i))
    #hosts = ['h1', 'h2']
    #switches = ['s1', 's2', 's3', 's4', 's5', 's6', 's7']
    """ Links between APs """
    for i in range(1, n+1):
        for j in range(linkconfig[i-1]):
            links.append([hosts[i], switches[i-1]])
        for j in range(n, n+m):
            links.append([switches[i-1], switches[j]])
        #links.append([switches[i-1],switches[i-1+n]])
    for i in range(n, m+n):
        links.append([switches[-1], switches[i]])
    links.append([hosts[0], switches[-1]])
    print(links)



    nodes = {}

    """ Initialize Ships """
    for host in hosts:
        node = net.addHost(host)
        nodes[host] = node

    """ Initialize SATCOMs """
    for switch in switches:
        node = net.addSwitch(switch)
        nodes[switch] = node

    """ Add links """
    for link in links:
        name1, name2 = link[0], link[1]
        node1, node2 = nodes[name1], nodes[name2]
        print(name1,name2)
        #net.addLink(node1, node2)
    
    #bind ships with the switches
    net.addLink(nodes[switches[0]],nodes[hosts[1]], delay = '100ms')
    net.addLink(nodes[switches[0]],nodes[hosts[1]], delay = '100ms')
    net.addLink(nodes[switches[1]],nodes[hosts[2]], delay = '100ms')
    net.addLink(nodes[switches[1]],nodes[hosts[2]], delay = '100ms')    
    net.addLink(nodes[switches[2]],nodes[hosts[3]], delay = '100ms')
    net.addLink(nodes[switches[3]],nodes[hosts[4]], delay = '100ms')
    net.addLink(nodes[switches[3]],nodes[hosts[4]], delay = '100ms')    
    net.addLink(nodes[switches[4]],nodes[hosts[5]], delay = '100ms')
    net.addLink(nodes[switches[4]],nodes[hosts[5]], delay = '100ms')    
    
    net.addLink(nodes[switches[8]],nodes[hosts[0]],delay = '100ms')

    net.addLink(nodes[switches[5]],nodes[switches[8]], bw = cap[0], delay = '100ms')
    net.addLink(nodes[switches[6]],nodes[switches[8]], bw = cap[1], delay = '100ms')
    net.addLink(nodes[switches[7]],nodes[switches[8]], bw = cap[2], delay = '100ms')


    #Bug: if you want to use queues, you cannot set bws and delays of the following links because they all use linux-htb
    net.addLink(nodes[switches[0]],nodes[switches[5]])    #ship1 is connected to SAT1,3
    net.addLink(nodes[switches[0]],nodes[switches[7]])

    net.addLink(nodes[switches[1]],nodes[switches[5]])    #ship2 is connected to SAT1,2
    net.addLink(nodes[switches[1]],nodes[switches[6]])

    net.addLink(nodes[switches[2]],nodes[switches[6]])    #ship3 is connected to SAT2
    
    net.addLink(nodes[switches[3]],nodes[switches[5]])    #ship4 is connected to SAT1,2
    net.addLink(nodes[switches[3]],nodes[switches[6]])

    net.addLink(nodes[switches[4]],nodes[switches[5]])    #ship5 is connected to SAT1,3
    net.addLink(nodes[switches[4]],nodes[switches[7]])




    #generate MPTCP host configuration files
    for i in range(1,n+1):
        name=hosts[i]
        file=open(name+".sh","w")
        file.write("#!/bin/bash\n\n")
        for j in range(linkconfig[i-1]):
            intf=name+"-eth"+str(j)
            ipaddr="10.0."+str(i)+"."+str(j)
            file.write("ifconfig "+intf+" "+ipaddr+" netmask 255.255.255.255\n\n")
        for j in range(linkconfig[i-1]):
            ipaddr="10.0."+str(i)+"."+str(j)
            file.write("ip rule add from "+ipaddr+" table "+str(j+1)+"\n\n")
        for j in range(linkconfig[i-1]):
            ipaddr="10.0."+str(i)+"."+str(j)+"/32"
            intf=name+"-eth"+str(j)
            file.write("ip route add "+ipaddr+" dev "+intf+" scope link table "+str(j+1)+"\n\n")
        for j in range(linkconfig[i-1]):
            ipaddr="10.0."+str(i)+"."+str(j)
            intf=name+"-eth"+str(j)
            file.write("ip route add default via "+ipaddr+" dev "+intf+" table "+str(j+1)+"\n\n")
        file.write("ip route add default scope global nexthop via 10.0."+str(i)+".0 dev "+name+"-eth0")
        file.close()
        call(["sudo", "chmod", "777", name+".sh"])
                

    """ Start the simulation """
    info('*** Starting network ***\n')
    net.start()
    
    #set all ships 
    for i in range(1,n+1):
        src=nodes[hosts[i]]
        info("--configing routing table of "+hosts[i])
        src.cmdPrint('./'+hosts[i]+'.sh')
    
	
    info('*** start test ***\n')

    time.sleep(3)


    info('*** set queues ***\n')
    call(["sudo", "bash","MPTCPQueueConfig.sh"])
    
    time.sleep(3)
    info('*** set flow tables ***\n')
    call(["sudo", "bash","MPTCPFlowTableConfig.sh"])    
    

    dst=nodes[hosts[0]]
    dst.cmdPrint('iperf -s -i 1 >testiperf.txt &')
    dst.cmdPrint('sudo wireshark &')
    time.sleep(10)

    for i in range(1,n+1):
        src=nodes[hosts[i]]
        info("testing",src.name,"<->",dst.name,'\n')
        src.cmdPrint('ping -c 2 10.0.0.1 &')        
        time.sleep(0.2)
        src.cmdPrint('iperf -c 10.0.0.1 -t 60 -i 2 &')
        time.sleep(0.2)
    
    time.sleep(5)


    CLI(net)

    net.stop()
    info( '*** net.stop()\n' )

if __name__ == '__main__':
    setLogLevel( 'info' )
    WifiNet(5,3,"127.0.0.1",[2,2,1,2,2], [1.0,1.0,0.8,0.6,0.6],[3.0, 2.0, 1.5], [1.0]*5,30)
    #WifiNet(30,3,"127.0.0.1",[2.0]*30,[30,20,30],120)

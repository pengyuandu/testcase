#!/bin/bash


sudo ovs-ofctl add-flow s1 in_port=1,actions=set_queue:1,output:2
sudo ovs-ofctl add-flow s1 in_port=2,actions=normal
sudo ovs-ofctl add-flow s1 priority=100,actions=normal 


sudo ovs-ofctl add-flow s2 in_port=1,actions=set_queue:2,output:2
sudo ovs-ofctl add-flow s2 in_port=2,actions=normal
sudo ovs-ofctl add-flow s2 priority=100,actions=normal


sudo ovs-ofctl add-flow s3 in_port=1,actions=set_queue:3,output:2
sudo ovs-ofctl add-flow s3 in_port=2,actions=normal
sudo ovs-ofctl add-flow s3 priority=100,actions=normal


sudo ovs-ofctl add-flow s4 in_port=1,actions=set_queue:4,output:3
sudo ovs-ofctl add-flow s4 in_port=3,actions=normal
sudo ovs-ofctl add-flow s4 priority=100,actions=normal

sudo ovs-ofctl add-flow s5 in_port=1,actions=set_queue:5,output:3
sudo ovs-ofctl add-flow s5 in_port=3,actions=normal
sudo ovs-ofctl add-flow s5 priority=100,actions=normal


sudo ovs-ofctl add-flow s6 in_port=2,actions=output:1
sudo ovs-ofctl add-flow s6 in_port=3,actions=output:1
sudo ovs-ofctl add-flow s6 in_port=4,actions=output:1
sudo ovs-ofctl add-flow s6 in_port=5,actions=output:1
sudo ovs-ofctl add-flow s6 in_port=1,actions=normal
sudo ovs-ofctl add-flow s6 priority=100,actions=normal

sudo ovs-ofctl add-flow s7 in_port=2,actions=output:1
sudo ovs-ofctl add-flow s7 in_port=3,actions=output:1
sudo ovs-ofctl add-flow s7 in_port=4,actions=output:1
sudo ovs-ofctl add-flow s7 in_port=1,actions=normal
sudo ovs-ofctl add-flow s7 priority=100,actions=normal



sudo ovs-ofctl add-flow s8 in_port=2,actions=output:1
sudo ovs-ofctl add-flow s8 in_port=3,actions=output:1
sudo ovs-ofctl add-flow s8 in_port=1,actions=normal
sudo ovs-ofctl add-flow s8 priority=100,actions=normal


sudo ovs-ofctl add-flow s9 in_port=2,actions=output:1
sudo ovs-ofctl add-flow s9 in_port=3,actions=output:1
sudo ovs-ofctl add-flow s9 in_port=4,actions=output:1
sudo ovs-ofctl add-flow s9 in_port=1,actions=output:normal
sudo ovs-ofctl add-flow s8 priority=100,actions=normal

#!/bin/bash

sudo ovs-vsctl -- set Port s1-eth2 qos=@newqos -- --id=@newqos create QoS type=linux-htb other-config:max-rate=100000000 queues:1=@q1 -- --id=@q1 create Queue other-config:min-rate=1000000 other-config:max-rate=1000000
sudo ovs-ofctl -O Openflow13 queue-stats s1


sudo ovs-vsctl -- set Port s2-eth2 qos=@newqos -- --id=@newqos create QoS type=linux-htb other-config:max-rate=100000000 queues:2=@q2 -- --id=@q2 create Queue other-config:min-rate=1000000 other-config:max-rate=1000000
sudo ovs-ofctl -O Openflow13 queue-stats s2


sudo ovs-vsctl -- set Port s3-eth2 qos=@newqos -- --id=@newqos create QoS type=linux-htb other-config:max-rate=100000000 queues:3=@q3 -- --id=@q3 create Queue other-config:min-rate=800000 other-config:max-rate=800000
sudo ovs-ofctl -O Openflow13 queue-stats s3


sudo ovs-vsctl -- set Port s4-eth3 qos=@newqos -- --id=@newqos create QoS type=linux-htb other-config:max-rate=100000000 queues:4=@q4 -- --id=@q4 create Queue other-config:min-rate=600000 other-config:max-rate=600000
sudo ovs-ofctl -O Openflow13 queue-stats s4



sudo ovs-vsctl -- set Port s5-eth3 qos=@newqos -- --id=@newqos create QoS type=linux-htb other-config:max-rate=100000000 queues:5=@q5 -- --id=@q5 create Queue other-config:min-rate=600000 other-config:max-rate=600000
sudo ovs-ofctl -O Openflow13 queue-stats s5

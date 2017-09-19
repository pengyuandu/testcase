#!/bin/bash

sudo ovs-vsctl -- set Port s1-eth3 qos=@newqos -- --id=@newqos create QoS type=linux-htb other-config:max-rate=100000000 queues:1=@q1 -- --id=@q1 create Queue other-config:min-rate=535000 other-config:max-rate=535000

sudo ovs-vsctl -- set Port s1-eth4 qos=@newqos -- --id=@newqos create QoS type=linux-htb other-config:max-rate=100000000 queues:2=@q2 -- --id=@q2 create Queue other-config:min-rate=465000 other-config:max-rate=465000

sudo ovs-ofctl -O Openflow13 queue-stats s1


sudo ovs-vsctl -- set Port s2-eth3 qos=@newqos -- --id=@newqos create QoS type=linux-htb other-config:max-rate=100000000 queues:3=@q3 -- --id=@q3 create Queue other-config:min-rate=672000 other-config:max-rate=672000

sudo ovs-vsctl -- set Port s2-eth4 qos=@newqos -- --id=@newqos create QoS type=linux-htb other-config:max-rate=100000000 queues:4=@q4 -- --id=@q4 create Queue other-config:min-rate=328000 other-config:max-rate=328000

sudo ovs-ofctl -O Openflow13 queue-stats s2


sudo ovs-vsctl -- set Port s3-eth2 qos=@newqos -- --id=@newqos create QoS type=linux-htb other-config:max-rate=100000000 queues:5=@q5 -- --id=@q5 create Queue other-config:min-rate=800000 other-config:max-rate=800000
sudo ovs-ofctl -O Openflow13 queue-stats s3


sudo ovs-vsctl -- set Port s4-eth3 qos=@newqos -- --id=@newqos create QoS type=linux-htb other-config:max-rate=100000000 queues:6=@q6 -- --id=@q6 create Queue other-config:min-rate=403000 other-config:max-rate=403000

sudo ovs-vsctl -- set Port s4-eth4 qos=@newqos -- --id=@newqos create QoS type=linux-htb other-config:max-rate=100000000 queues:7=@q7 -- --id=@q7 create Queue other-config:min-rate=197000 other-config:max-rate=197000

sudo ovs-ofctl -O Openflow13 queue-stats s4


sudo ovs-vsctl -- set Port s5-eth3 qos=@newqos -- --id=@newqos create QoS type=linux-htb other-config:max-rate=100000000 queues:8=@q8 -- --id=@q8 create Queue other-config:min-rate=321000 other-config:max-rate=321000

sudo ovs-vsctl -- set Port s5-eth4 qos=@newqos -- --id=@newqos create QoS type=linux-htb other-config:max-rate=100000000 queues:9=@q9 -- --id=@q9 create Queue other-config:min-rate=279000 other-config:max-rate=279000

sudo ovs-ofctl -O Openflow13 queue-stats s5

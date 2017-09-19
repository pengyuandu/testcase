#!/bin/bash

ifconfig ship3-eth0 10.0.3.0 netmask 255.255.255.255

ip rule add from 10.0.3.0 table 1

ip route add 10.0.3.0/32 dev ship3-eth0 scope link table 1

ip route add default via 10.0.3.0 dev ship3-eth0 table 1

ip route add default scope global nexthop via 10.0.3.0 dev ship3-eth0
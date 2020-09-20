Title: Networking Pt 2
Date: 2020-09-19
Tags: learning, pts

# Routing
A router is a networking device that forwards data packets between computer networks. A router os connected to two or more data lines from different IP networks. When a data packet comes in one of the lines, the router reads the network address information in the packet header to determine the destination. Then, based on routing table, it directs the packet to the next network.
Routing table contains information about the topology of the network immediately around it.
The table can also contain an entry with the **default address** `0.0.0.0`. This entry is used when the router receives a packet whose destination is an *unknown network*.

## Routing table example (router)

```
Kernel IP routing table
Destination     Gateway         Genmask         Flags   MSS Window  irtt Iface
87.169.144.1    0.0.0.0         255.255.255.255 UH        0 0          0 eth0
192.168.1.0     0.0.0.0         255.255.255.0   U         0 0          0 br0
87.169.144.0    0.0.0.0         255.255.252.0   U         0 0          0 eth0
127.0.0.0       0.0.0.0         255.0.0.0       U         0 0          0 lo
0.0.0.0         87.169.144.1    0.0.0.0         UG        0 0          0 eth0
```
The kernel reads routing table from the top down. The first column is the destination. The second column tells how to reach that destination.
The default gateway is always shown with the destination `0.0.0.0`. The IP address in the gateway column is that of the outbound gateway router. The netmask for the default gateway means that any packet not addressed to the local network or another outbound router by additional entries in the routing table are to be sent to the default gateway regardless of the network class.

# Networking Layer 2
Every host on a network has both an IP and a MAC address. When server A wants to send a packet to server B:

1. server A creates a packet:
    * the destination IP address of server B in the IP header of the datagram.
    * the destination MAC address of the router in the link layer header of the frame.
    * the source IP address of the server A.
    * the source MAC address of the server A.
1. router takes a packet and forwards it to server B (the destination MAC address is the MAC address of the **next hop**):
    * the destination MAC address is rewritten to server B
    * the source MAC address is of router.
    * **Only MAC address is changed. IP address stays the same (both source and destination)**. This is global information and remains the same along the packet trip.

## MAC address
MAC address is a unique identifier assigned to a network interface controller (NIC). It is assigned by device manufacturer: typically includes a manufacturer's organizationally unique identifier. MAC address is 48 bit (6 bytes) long and is expressed in hexadecimal form: `AA:BB:CC:DD:EE:FF`.

The IEEE has built in special address to allow more than one NIC to be addressed at one time. It's called broadcast address: `FF:FF:FF:FF:FF:FF`. Frame with this address is delivered to all devices in the local network.

## Network segmentation
Switches do not segment networks. Only routers do so. Usually, every interface of a router is connected to different network. This is the reason, why routers **do not forward broadcast packets**, like switches.

## Packet forwarding
To forward a packet:

* the switch reads the destination MAC address of the frame.
* it performs a look-up in the CAM table.
* it forwads the packet to the corresponding interface.
* if there is no entry with the MAC address, the switch will forward the frame to all its interfaces.

## Address Resolution Protocol (ARP)
The ARP is a communication protocol used for discovering the link layer address, such as a MAC address, associated with a given internet layer address, typically an IPv4 address.

### Example of workflow
Two computers are connected to the same local network. Computer A wants to send packet to Computer B. Through DNS, it determines Computer B **IP address** `192.168.0.2`.
To send message, Computer A also requires MAC address.

1. Computer A retrieves cached information from ARP table for `192.168.0.2`
    * if the cache didn't produce a result for IP address, Computer A sends broadcast ARP request message `FF:FF:FF:FF:FF:FF`, requesting an answer for `192.168.0.2`.

2. Based on retrieved information, Computer A sends packet with MAC adress and IP address.

ARP table has time-to-live (TTL) for every entry. When it expires, or on power off, host discards entries.

# Additional resources
* [Router](https://en.wikipedia.org/wiki/Router_(computing))
* [IP routing](https://en.wikipedia.org/wiki/IP_routing)
* [netstat command](https://tldp.org/LDP/nag2/x-087-2-iface.netstat.html)
* [Introduction to Linux network routing](https://opensource.com/business/16/8/introduction-linux-network-routing)
* [MAC address](https://en.wikipedia.org/wiki/Mac_address)
* [ARP](https://en.wikipedia.org/wiki/Address_Resolution_Protocol)

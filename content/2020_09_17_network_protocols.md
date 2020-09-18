Title: Networking
Date: 2020-09-17
Tags: learning, pts

# Protocols

## What is packet

Every packet in every protocol has `Header` (control information) and `Payload` (user data) structure. The header has a protocol-specific structure: this ensures that the receiving host can correctly interpret the payload and handle the communication. The payload is the actual information. It could be something like part of an email message or the content of a file during a download.

[IPv4 protocol header](https://en.wikipedia.org/wiki/IPv4_packet#Header) is at least 160 bits (20 bytes) long, and it includes 14 fields, of which 13 are required. Last field, called `options` is optional.
![IPv4 packet - Wikipedia](https://upload.wikimedia.org/wikipedia/commons/7/71/IPv4_Packet_-en.svg)
Source: Wikipedia, author [MichelBakni](https://commons.wikimedia.org/w/index.php?title=User:MichelBakni&action=edit&redlink=1)

Using the information in the header, the nodes involved in the communication can understand and use IP packets.

## Protocol layers
Most of the time, when people talk about layers, they think about OSI model. OSI model promoted the idea of a consistent model of protocol layers, defining interoperability between network devices and software.
Based on that we can think about seven layers ([more here](https://docs.microsoft.com/en-us/windows-hardware/drivers/network/windows-network-architecture-and-the-osi-model)).  What we need to know is, that each protocol has `header` and `payload`. It goes from top to bottom. Every next layer is encapsulating the layer before in the form of payload.

## Encapsulation
If we look from 10.000 foot perspective, we can see only data packet. However, if we look at this closer, it's starting showing some interesting properties.
Every layer contains paylod in a form of `header+payload` from previous layer. It means, that at the lowest level, we're looking at
```
(header + (header + (header + (header + payload))))
```
This kind of behavior happens to every packet sent by host. On the other side of pipeline, receiving host, needs to unpack all the information, with regards to correct layers.

# Internet Protocol (IP)

## IP Address

### IPv4 Address
IPv4 address consists of 4 bytes (octets). A dot delimits every octet in the address. Each byte (`2^8`) can represent value **0** to **255**.
```
 172.22.128.47
```

#### Special use IPv4 addresses
RFC5735 describes IPv4 addresses, which cannot be assigned to host, due to its special use case.
Common addresses, that are in use:
```
127.0.0.0/8    <-- host loopback address.
169.254.0.0/16 <-- communication between hosts, without DHCP server cannot be found.
192.168.0.0/16 <-- private networks.
```

### Network classes
Internet addresses are allocated by the InterNIC organization. The most common classes are A, B and C. D and E exist, but are not used by end users.
Each of classes has different default subnet mask.

* Class A: uses 255.0.0.0 (CIDR /8) and have `0-127` as first octet,
* Class B: uses 255.255.0.0 (CIDR /16) and have `128-191` as first octet,
* Class C: uses 255.255.255.0 (CIDR /24) and have `192-223` as first octet.
* Class D: range `224-239` as first octet, used for multicasting
* Class E: range `240-255` as first octet, not available for general use, reserved for research purposes.

### CIDR
Subnet with all zeros is reserved for the referring to the network itself, while last address, all ones is used as broadcast address for the network. It means, that from network, two addresses are unavailable. In the world of CIDR, `/31` and `/32`, would be unusable, due to above requirement. That's why `RFC3021` created an exception. Network `/31` is usable for point-to-point links, while `/32` (single-host network) must be accessed by explicit routing rules, as there is no room in such a network for a gateway.

### IPv6
RFC3513 (obsolete now) and RFC4291 describes IPv6 addressing architecture. This version allows to address 2^128 devices (approximately 3.4\*10^38). It's been introduced in December 1995, but still majority of Internet relies on IPv4.
IPv6 is divided into two parts (each 64 bits): network identifier and interface identifier. Furthermore, the first 64 bits ends with a dedicated 16-bits space that can be used only for specifying a subnet.

# Additional resources

* [IPv4 protocol header](https://en.wikipedia.org/wiki/IPv4_packet#Header)
* [Network architecture](https://docs.microsoft.com/en-us/windows-hardware/drivers/network/windows-network-architecture-and-the-osi-model)
* [OSI model](https://en.wikipedia.org/wiki/OSI_model)
* [RFC5735](https://tools.ietf.org/html/rfc5735)
* [subnet masks](https://support.microsoft.com/en-us/help/164015/understanding-tcp-ip-addressing-and-subnetting-basics).
* [RFC1878 - Variable Length Subnet Table For IPv4](https://tools.ietf.org/html/rfc1878)
* [CIDR - Wikipedia](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing#IPv4_CIDR_blocks)
* [RFC3021 - Using 31-bit Prefixes on IPv4 Point-to_-Point links](https://tools.ietf.org/html/rfc3021)
* [RFC4291 - Internet Protocol Version 6 (IPv6) Addressing Architecture](https://tools.ietf.org/html/rfc4291)

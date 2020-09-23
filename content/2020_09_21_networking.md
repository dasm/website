Title: Networking Pt 3: TCP and UDP
Date: 2020-09-21
Tags: learning, pts, network

# TCP & UDP

There are two common transport protocols used on the Internet: `TCP` (Transmission Control Protocol) and `UDP` (User Datagram Protocol).
TCP is the most used transport protocol on the Internet. The vast majority of applications use it, and the IP protocol suite is often called **TCP/IP**.
UDP is much simpler. It doesn't guarantee packet delivery and it is conectionless. Thanks to those features, it is much faster than TCP, it provides better throughput. It is often used by multimedia applications that can tolerate packet loss but are througput intensive. It is often used in VoIP and video streaming applications where you can tolerate a little glitch in the audio or video.

TCP | UDP
----|-----
Connection oriented protocol | Connectionless
Rearranges data packets in the order specified | No inherent order as all packets are independent of each other.
Slower speed than UDP | UDP is faster, because error recovery is not attepmted. It is "best effort" protocol
Data is read as byte stream, no distinguishing information is sent to signal message boundaries | Packets are sent individually and are checked for integrity only when they arrive. Packets have definite boundaries, meaning a read operation at the receiver socket will yield an entire message as it was originally sent.

## Ports
Ports are used to identify a single network process on a machine. When some process is establishing connection to external internet resource (browser -> website), there is port open, associated with browser. Information about the port is later sent as part of header in TCP or UDP packet. In the case of aforementioned connection, `source port` would be the same, that was created for browser. `Destination port` then is associeated with website (usually `80` or `443`).
This is the way how process know where information needs to be addressed.

## TCP handshake
In the case of UDP, which is connectionless, there is no handshake. However, for TCP, before any kind of transmission can happen, there needs to be established connection.
It is done in so called three-way handshake.
The header fields involved in the handshake are: sequence number, acknowledgement numbers, SYN and ACK flags

1. The client sends a TCP packet to the server with the `SYN` flag enabled and a random `sequence number`.
1. The server replies by sending a packet with both the `SYN` and `ACK` flags. `Sequence number` is again chosen as random, but `ACK` is `seq number + 1`.
1. The client completes the synchronization by sending an `ACK` packet. The `ACK` is `seq number + 1` and `sequence number` is `ACK + 1` from the second step.

```
Host 1 | flags | Host 2
-------|-------|--------
-----> |SYN    |
    Seq: 328, ACK: 0

       |SYN/ACK| <------
    Seq: 412, ACK: 329

------>|ACK    |
    Seq: 330, ACK: 413

```

# Additional resources
* [TCP vs UDP](https://www.diffen.com/difference/TCP_vs_UDP)
* [Port numbers on a computer](https://www.lifewire.com/port-numbers-on-computer-networks-817939)

Title: Networking Pt 4
Date: 2020-09-23
Tags: learning, pts, network

# Firewall

Firewalls are specialized software modules running on a computer or a dedicated network device. They serve to filter packets coming in and out of a network. They can work on different layers of the OSI model.

## Packet filtering

The most basic feature of a firewall is packet filtering. Administrator can create rules which will filter packets according to certain characteristics like:

* source IP address
* destination IP address
* protocol
* source port
* destination port

Common actions, that can be applied:

* allow: allow the packet to pass
* drop: drops the packet without any diagnostic message to the packet source host
* deny: similar to drop, but notify the source host

Inspecting the header of a packet does not give you any information on the content. Even if only port `80` or `443` is allowed, attacker can exploit them, to access deeper levels of network.

## Application level firewalls

Application level firewall works by checking all 7 layers of the OSI model. They provide more comprehensive protection because they inspect the actual content of a packet, not just headers.

## Intrusion Detection System (IDS)
IDS inspects the application payload trying to detect any potential attack. It checks for attack vectors like ping sweeps, port scans, SQL injections, buffer overflows etc.
IDS, similar to antivirus, detects risky traffic by means of signatures. The vendor provides frequent signature updates as soon as new attack vectors are found. Without the right signatures an IDS cannot detect and report an intrusion.
There is also risk of **false positives** when legic traffic is marked as malicious.

`IDS != firewall`
IDS is another layer of protection, which can be used in conjunction with firewall.

## Intrusion Prevention System (IPS)
It is similar to IDS, however it can drop malicious request when the threat has risk classification above predefined threshold.

# Domain Name System (DNS)
The DNS converts human-readable names to IP addresses.
DNS structure can be broken down into:

* top level domain (TLD)
* domain part
* subdomain part (if applicable)
* host part

Name resolution is performed by resolvers. Resolvers are servers that contact the TLD server and follow the hierarchy of the DNS name to resolve the name of a host:

1. resolver contacts one of the **root name servers**, these server contain information about the TLD (this information is hardcoded by system administrator);
1. next, it asks the TLD name server (from previous step), what's the name of the server which can give information about the **domain** the resolver is looking for;
1. if there are one or more subdomains, previous step is repeated for every subdomain;
1. resolver asks for the name resolution of the **host** part;
1. the resolver sends the IP address back to the client.

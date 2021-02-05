Title: Introduction to the Cloud
Date: 2021-02-05
Tags: learning, virtualization, cloud


This post is an attempt to gather common terms, and provide links for more reading (mainly to wikipedia) about virtualization et al.

# Intro
Virtualization term has been coined in 1960s to describe virtual machine. Right now, virtualization can also describe other areas like: software, memory, storage, data, network and hardware.
However, in the common understanding, virtualization means hardware virtualization. It refers to the creation of virtual machine htat acts like a real computer with an operating system.

# Hardware virtualization
[Hardware Virtualization][1] can be divided into two main types:

* [full virtualization][2] - completely simulates the actual hardware, guest system can run unmodified.
* [paravirtualization][3] - uses software interface which is similar, but not identical to the underlying hardware.

## Full virtualization
Virtual machine simulates hardware to allow an unmodified guest OS to be run in isolation.

* Software-assisted - completely relies on binary translation to virtualize the execution of sensitive, non-virtualizable instruction sets. It emulates the hardware using the software instruction sets. Due to binary translation, it is often criticized for performance issue: Eg. VirtualBox, VMware workstation, Virtual PC
* Hardware-assisted - it eliminates the binary translation and it directly interrupts with hardware using the virtualization technology which has been integrated on processors. Guest OS's instructions might allow a virtual context execute privileged instructions directly on the processor, even thought it is virtualized. Eg. VMware ESXi, KVM, Hyper-V, Xen.

## Paravirtualization
It requires the guest operating system to be explicitly ported for the para-API, conventional OS distribution that is not paravirtualization-aware cannot be run on top of a paravirtualizing VVM.

# Hypervisor
[Hypervisor][4] (virtual machine monitor, VMM) is computer software, firmare or hardware that runs virtual machines. A computer on which a hypervisor runs one or more virtual machines is called a _host machine_, and each virtual machine is called a _guest machine_.
There are two types of hypervisors:

* Type-1, native or bare-metal hypervisors
* Type-2 or hosted hypervisors

## Type-1 (bare-metal)
Type-1 hypervisor is very basic OS on top of which there can be run virtual machines. The physical machine the hypervisor is running on serves virtualization purpose only. It is mainly found in enterprise environments.
Due to its simplicity, it doesn't offer many functionalities.
Examples:

* VMware ESX/ESXi
* KVM (it oftentimes can be categorized as type-2 hypervisor)
* Oracle VM

## Type-2 (hosted)
This type of hypervisor runs on a conventional OS as an another program.
Examples:

* VirtualBox
* VMware Workstation
* Windows Virtual PC
* Parallels Desktop

[1]: https://en.wikipedia.org/wiki/Hardware_virtualization
[2]: https://en.wikipedia.org/wiki/Full_virtualization
[3]: https://en.wikipedia.org/wiki/Paravirtualization
[4]: https://en.wikipedia.org/wiki/Hypervisor

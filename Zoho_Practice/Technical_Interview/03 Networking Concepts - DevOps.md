# Phase 1: The Physical Server Era

[Networking Interview questions for Devops (2026)](https://medium.com/@shindeshubhangi463/50-must-prepare-networking-interview-questions-for-devops-engineers-2025-guide-2b7e7d56e8f1)

## IP Address

An **IP address** is a unique numerical label assigned to every device connected to a network that uses the Internet Protocol for communication. It serves two primary functions: host or network interface identification, and location addressing.

- **IPv4** addresses are 32-bit numbers usually displayed in dot-decimal notation (e.g., `192.168.1.50`).
  
- **IPv6** addresses are 128-bit numbers displayed in hexadecimal (e.g., `2001:db8::ff00:42:8329`) to accommodate the exploding number of global devices. Addresses are further divided into **Public IPs** (globally routable on the internet) and **Private IPs** (used only within local networks).

**Practical Example**,
When your laptop joins the office Wi-Fi, the local network dynamically assigns it a private IP address of `10.0.1.45`. When you try to access the public internet, your office router translates that private address to the company's single public IP address, `203.0.113.82`, so external servers know where to send back the web traffic.
## Network
A **network** is a collection of interconnected computing devices (hosts) that can communicate and share resources with one another. Networks can be small and localized, like a **LAN (Local Area Network)** inside a single building, or massive and distributed, like a **WAN (Wide Area Network)** or the global internet itself. Communication is governed by standardized protocols (like TCP/IP) that dictate how data is packaged, sent, and received.

**Practical Example**, 
An enterprise sets up a corporate office network. All employee laptops, local staging servers, and office printers are connected to a Local Area Network (LAN) using Ethernet cables and Wi-Fi, allowing them to share files and access internal tools within the `192.168.1.0/24` IP range.
## Host
A **host** is any network-connected computer or device that initiates, processes, or terminates data sessions. Every host is assigned an IP address. Hosts include end-user devices (laptops, smartphones, IoT devices) as well as infrastructure assets (servers, network-attached storage). Essentially, if a device has a network stack running on it and can participate actively as an endpoint in communication, it is a host.

**Practical Example**
An engineer's MacBook Pro acting as a client machine, or a bare-metal Dell blade running Linux in an on-premise datacenter, are both **hosts** on the corporate network. The MacBook initiates a request, and the Linux blade processes it.
## Router
A **router** is a specialized network device that forwards data packets between different computer networks. Operating primarily at Layer 3 (Network Layer) of the OSI model, a router inspects the destination IP address of an incoming packet and uses its internal **routing table** to determine the most efficient path (the "next hop") to get that packet closer to its destination. It connects your local network to external networks, such as your Internet Service Provider (ISP).

**Practical Example**
You are on your office laptop (`192.168.1.50`) and try to visit an external website. Your local **default gateway** (the local router at `192.168.1.1`) realizes that the target website is outside the local office network. It encapsulates the data and passes it off to the upstream ISP router, which continues moving it across the internet backbone.
## Servers
A **server** is a specific type of high-performance host that provides functionality, data, or resources to other devices (called "clients") over a network. Servers run specialized operating systems (like Linux or Windows Server) and continuous background processes (daemons) designed to listen for and fulfill incoming requests, such as serving webpages, managing databases, or handling file transfers.

**Practical Example**,
An organization deploys an Ubuntu Linux instance to serve as their internal Git repository. This **server** sits at a fixed IP address (`10.0.2.10`), constantly running a service that waits for developers to push or pull source code changes from their local machines.

## Transmission Control Protocol (TCP)
TCP stands for **Transmission Control Protocol**. It is the foundational communication standard that dictates how devices exchange data reliably across the internet. By breaking messages into packets, verifying their delivery, and ensuring they arrive in the correct order, it acts as a digital courier.

**Practical Example**,
When a DevOps engineer runs a deployment script that connects to a remote production server via SSH (`ssh admin@10.0.4.20:22`), their local machine initiates a TCP connection. The laptop sends a `SYN` packet to port 22. The server responds with a `SYN-ACK`. The laptop replies with an `ACK`, opening a secure pipe. As commands are typed, TCP packages and tracks the keystrokes. If a packet drops due to momentary Wi-Fi interference, the laptop's TCP stack notices the missing acknowledgement and silently re-transmits those specific bytes.
## Domain Name System (DNS)
The **Domain Name System (DNS)** is the phonebook of the internet. Computers communicate strictly via numerical IP addresses, but humans prefer human-readable names. DNS is a hierarchical, distributed database that translates easy-to-remember domain names (like `internal.company.com`) into the numerical IP addresses (`10.0.2.10`) required to route network traffic.

**Practical Example**,
Instead of forcing engineers to memorize the IP address `192.168.42.11` to access their internal project management dashboard, the DevOps team creates a DNS **A record** mapping `jira.corporate.local` to that exact IP. When an engineer types the domain into their browser, a DNS query runs in milliseconds behind the scenes to fetch the IP.
## Network Interface
A **Network Interface** is the software or hardware boundary between a host device and the physical network medium. It can be a physical component like a **Network Interface Card (NIC)** for wired Ethernet connections, or a virtual/wireless component. In Linux operating systems, these interfaces are exposed as names like `eth0` (first physical Ethernet interface), `wlan0` (first wireless interface), or `lo` (loopback interface).

**Practical Example**,
A dual-homed database server needs to connect to two networks simultaneously for security isolation. It uses its physical Ethernet port mapping to interface `eth0` to communicate with the internal application tier, while utilizing a separate virtual interface `eth1` to back up data to an isolated storage area network (SAN).
### eho0
### Wlan0
### Io
## Ports
A **port** is a logical construct at the transport layer (Layer 4) used to identify a specific process or application running on a host. While an IP address gets a packet to the correct device, a port number ensures the packet goes to the correct application running on that device. Ports range from `0` to `65535`. Standardized services use **Well-Known Ports** (e.g., Port `80` for HTTP, Port `443` for HTTPS, Port `22` for SSH).

**Practical Example**,
A single server with the IP address `10.0.5.5` is running two separate services simultaneously: a secure web server and an encrypted file transfer server. When a client connects to `10.0.5.5:443`, the operating system routes the traffic directly to the web server application process (**NGINX**). When a client connects to `10.0.5.5:22`, the operating system routes that traffic to the secure shell daemon (**SSHD**).

## Putting It All Together: The Lifecycle of a Request

To see how this mental map operates end-to-end, let's track a request from an employee's machine to an internal tool:

1. **The Intent:** An employee on their laptop (**Host**) wants to check their benefits on `payroll.corporate.local`.
   
2. **DNS Resolution:** The laptop doesn't know where that is. It queries the corporate switchboard (**DNS**), which responds: _"`payroll.corporate.local` is located at `10.0.10.25`."_
   
3. **Addressing & Packaging:** The laptop prepares data packets, marking the destination address as `10.0.10.25` and the target desk as Port `443` (HTTPS). The data exits the laptop through its wireless antenna mapping (**Network Interface `wlan0`**).
   
4. **Routing:** The packets travel through the air to the office building's mailroom (**Router**). The router reads the destination `10.0.10.25`, determines it belongs in the secure server room network, and routes it through the appropriate internal network cables (**Network**).
   
5. **Delivery:** The packet arrives at the target machine (**Server**) via its physical network card interface (**`eth0`**).
   
6. **Processing:** The server's operating system reads the packet, sees it is directed to **Port `443`**, and hands it off to the waiting Web Service daemon, which compiles the payroll data and sends a response back down the exact same chain.
# Phase 2: Virtual Machines & Hypervisors
## Virtual Machine
A **Virtual Machine (VM)** is an isolated software emulation of a physical computer that runs its own distinct guest operating system (e.g., Linux Ubuntu, Windows Server). A VM includes its own virtualized hardware stack—including a **vCPU**, **vRAM**, virtual disks, and **vNICs (Virtual Network Interface Cards)**. Because it is completely decoupled from the underlying hardware via the hypervisor, a VM can be snapshotted, backed up, migrated to completely different physical hardware while running, and destroyed in seconds without impacting other VMs on the same host.

**Practical Examples**,
Within our KVM hypervisor environment, we spin up a VM allocated with 4 vCPUs, 16GB of vRAM, and a 100GB virtual disk (`/dev/vda`). We install Ubuntu Server 24.04 onto it to act as a production database instance. To this database VM, it behaves exactly like a dedicated physical server, completely unaware that a Windows Server VM is running right next to it on the exact same physical silicon.
## Hypervisor
The hypervisor’s primary job is **resource emulation and isolation**: it abstracts the physical CPU, memory, storage, and network interfaces, dividing them into virtualized allocations. It tricks guest operating systems into believing they have exclusive access to real, physical hardware components while strictly preventing one virtual system from crashing or accessing the memory space of another.

**Practical Examples**,
An infrastructure engineer provisions a bare-metal Dell server with 128 physical CPU cores and 512GB of RAM running a Type 1 **KVM/Proxmox Hypervisor**. Through an infrastructure-as-code tool like Terraform, the engineer instructs the hypervisor to slice these resources up to host multiple distinct applications, ensuring compute limits are rigidly enforced so an application memory leak won't destabilize the whole machine.
## Network Address Translation
**Network Address Translation (NAT)** is a networking method used to map an entire private IP address space into a single public IP address (or a smaller pool of public IPs). In virtualization, a **NAT Gateway** or virtual NAT switch allows VMs residing on isolated internal networks (e.g., using RFC 1918 private ranges like `10.0.0.0/8` or `192.168.0.0/16`) to initiate outbound connections to the external internet to download patches or pull dependencies.

**Practical Examples**,
Your database VM is assigned a private IP of `192.168.122.45` on a virtual isolated network. The VM needs to run `apt-get update` to pull a security patch from the internet. The packet hits the hypervisor's virtual **NAT switch**. The switch intercepts the packet, swaps the source IP `192.168.122.45` with the host's public IP `198.51.100.12`, assigns an ephemeral source port, and passes it to the web. When the patch repository responds, the NAT switch maps it back to private host `192.168.122.45`.
## Firewall
A **firewall** is a network security device or software layer that monitors and filters inbound and outbound network traffic based on an organization’s previously established security rules. In virtualized cloud environments, firewalls exist as **Stateful Packet Inspection (SPI)** utilities operating as **Security Groups** or network-level appliances.
# Phase 3: Cloud Networking
## Cloud 
- The "cloud" refers to computing resources (servers, storage, networking, databases, etc.) that run in remote data centers and are accessed over the internet.
- Instead of buying and managing your own server, you rent resources from cloud providers.
- In networking, **"the cloud"** refers to ==on-demand, remote servers and infrastructure accessed over the internet, rather than local servers or hard drives==. It replaces physical, on-premises networking hardware (like routers and firewalls) with virtual, software-based components managed by third-party providers.
## Virtual Private Cloud (VPC)
## Subnets
A **Subnet** (Sub-network) is a logical subdivision of an IP network inside a VPC. By slicing the master CIDR block into smaller chunks (e.g., `/24` ranges), you isolate different tiers of an application.

- **Public Subnets** are designed for internet-facing resources. They are linked to an **Internet Gateway (IGW)**, meaning resources inside have public IPs and can directly exchange packets with the outside world.
  
- **Private Subnets** are completely isolated from direct internet access. Resources placed here receive only internal private IPs, sealing them off from external scanning and inbound threats.
- A Section of your VPC's IP range in one availability zone use to organize resources
- Public subnets have internet access, private ones don't.
## Security Group
### Route Tables
Defines how network traffic moves in a VPC, directing packets from subnet to targets like gateways, NAT, or other subnets.
### NAT Gateway
A NAT Gateways lets private subnet resources access the internet for updates or APIs while blocking incoming internet connections.
# Phase 4: Docker Networking
## Microservice
## Containers
## Docker Networking
## Docker overlay networking
## Container Port Mapping
# Phase 5: Kubernetes Networking
## Kubernetes Pod
## Container Network Interface - CNI
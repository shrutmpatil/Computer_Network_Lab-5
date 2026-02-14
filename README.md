# Computer Networks Lab – 5  
## IPv4 Address Classification Program

### Objective
This program determines networking details for a given IPv4 address based on classful addressing.

### Functionality
For a user-provided IPv4 address, the program outputs:

1. Class of IP address (A, B, C, D, E)
2. Number of NetID bits
3. Number of HostID bits
4. Number of networks supported
5. Number of hosts per network
6. Start and end range of the IP class
7. Default subnet mask

### Implementation Details
- Language: Python
- Uses classful IPv4 addressing logic
- Calculates networks and hosts using power-of-2 formulas
- Handles invalid input cases

### How to Run

```bash
python CN_LAB-5.py
```

Then enter an IPv4 address when prompted.

### Example

```
Enter an IPv4 address: 192.168.1.1

Class of IP Address: C
Number of NetID bits: 24
Number of HostID bits: 8
Default Subnet Mask: 255.255.255.0
```

### Concepts Covered
- IPv4 Addressing
- Classful Addressing
- Subnet Mask
- Network and Host Calculations

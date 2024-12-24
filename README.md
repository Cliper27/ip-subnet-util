# IP Subnet Utility

A command-line tool for performing subnet-related operations, such as converting subnet masks, calculating usable IPs, and finding the appropriate subnet mask for a given number of IPs.

## Usage
Convert a long-form subnet mask (e.g., 255.255.255.0) to CIDR notation (e.g., /24):
```bash
ip-subnet-util long_to_cidr <VALUE>
```

Convert a CIDR mask (e.g., /24) to a long-form mask (e.g., 255.255.255.0):
```bash
ip-subnet-util cidr_to_long <VALUE>
```

Calculate the number of usable IPs for a given CIDR mask (e.g., /24):
```bash
ip-subnet-util get_n_ips <VALUE>
```

Find the smallest CIDR mask for a given number of total IPs:
```bash
ip-subnet-util total_ips_to_mask <VALUE>
```

For additional info:
```bash
ip-subnet-util -h
```
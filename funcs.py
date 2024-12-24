import math

def cidr_to_long_form(mask: int) -> str:
    """
    Convert a CIDR notation mask (e.g., 24) to long form (e.g., 255.255.255.0).

    Args:
    mask (int): The CIDR notation mask (e.g., 24).

    Returns:
    str: The subnet mask in long form (e.g., "255.255.255.0").
    """
    if not (0 <= mask <= 32):
        raise ValueError("CIDR mask must be between 0 and 32.")

    binary_mask = "1" * mask + "0" * (32 - mask)
    octets = [str(int(binary_mask[i:i + 8], 2)) for i in range(0, 32, 8)]
    return ".".join(octets)

def long_form_to_cidr(mask: str) -> int:
    """
    Convert a long-form subnet mask (e.g., 255.255.255.0) to CIDR notation (e.g., 24).

    Args:
    mask (str): The subnet mask in long form (e.g., "255.255.255.0").

    Returns:
    int: The CIDR notation (e.g., 24).
    """
    octets = mask.split(".")
    if len(octets) != 4:
        raise ValueError("Invalid subnet mask format. Must have four octets.")

    binary_mask = "".join(f"{int(octet):08b}" for octet in octets)
    if not binary_mask.startswith('1' * binary_mask.count('1')):
        raise ValueError("Invalid subnet mask. Must be contiguous 1s followed by 0s.")
    return binary_mask.count('1')


def total_ips_to_mask(total_ips: int) -> int:
    """
    Calculate the smallest CIDR mask that accommodates a given total number of IPs.

    Args:
    total_ips (int): The total number of IPs.

    Returns:
    int: The CIDR mask (e.g., 24 for /24).
    """
    if total_ips < 1 or total_ips > 2 ** 32:
        raise ValueError("Total IPs must be between 1 and 2^32.")

    host_bits = math.ceil(math.log2(total_ips))
    cidr_mask = 32 - host_bits
    return cidr_mask

def get_available_ips(mask: int) -> int:
    """
    Calculate the total number of available IPs for a given IP mask.

    Args:
    mask (int): The subnet mask (e.g., 24 for /24).

    Returns:
    int: The total number of usable IPs.
    """
    if not (0 <= mask <= 32):
        raise ValueError("Mask must be between 0 and 32.")

    host_bits = 32 - mask
    total_ips = 2 ** host_bits
    usable_ips = total_ips - 2 if host_bits > 1 else 0
    return usable_ips

import argparse

import funcs


def main() -> None:
    parser = argparse.ArgumentParser(
        description="IP Subnet Utility CLI: Perform various subnet-related operations.",
        formatter_class=argparse.RawTextHelpFormatter,
    )

    parser.add_argument(
        "operation",
        choices=["long_to_cidr", "cidr_to_long", "get_n_ips", "total_ips_to_mask"],
        help=(
            "Choose an operation:\n"
            "- long_to_cidr: Convert a long-form subnet mask (e.g., 255.255.255.0) to CIDR notation (e.g., /24).\n"
            "- cidr_to_long: Convert a CIDR mask (e.g., /24) to a long-form mask (e.g., 255.255.255.0).\n"
            "- get_n_ips: Calculate the number of usable IPs for a given CIDR mask (e.g., /24).\n"
            "- total_ips_to_mask: Find the smallest CIDR mask for a given number of total IPs."
        ),
    )

    parser.add_argument(
        "value",
        help=(
            "The input value required for the chosen operation:\n"
            "- For long_to_cidr, provide the long-form mask (e.g., 255.255.255.0).\n"
            "- For cidr_to_long, provide the CIDR mask (e.g., 24).\n"
            "- For get_n_ips, provide the CIDR mask (e.g., 24).\n"
            "- For total_ips_to_mask, provide the total number of IPs (e.g., 300)."
        ),
    )

    args = parser.parse_args()

    try:
        if args.operation == "long_to_cidr":
            cidr = funcs.long_form_to_cidr(args.value)
            print(f"CIDR notation for {args.value}: /{cidr}")

        elif args.operation == "cidr_to_long":
            try:
                mask = int(args.value)
                long_form = funcs.cidr_to_long_form(mask)
                print(f"Long-form mask for /{mask}: {long_form}")
            except ValueError:
                print("Invalid CIDR mask. Ensure it is a number between 0 and 32.")

        elif args.operation == "get_n_ips":
            try:
                mask = int(args.value)
                usable_ips = funcs.get_available_ips(mask)
                print(f"Total usable IPs for /{mask}: {usable_ips}")
            except ValueError:
                print("Invalid CIDR mask. Ensure it is a number between 0 and 32.")

        elif args.operation == "total_ips_to_mask":
            try:
                total_ips = int(args.value)
                cidr_mask = funcs.total_ips_to_mask(total_ips)
                print(f"Smallest CIDR mask for {total_ips} IPs: /{cidr_mask}")
            except ValueError as e:
                print(f"Error: {e}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == '__main__':
    main()
def get_ip_class(ip_address):
    first_octet = int(ip_address.split('.')[0])

    if 1 <= first_octet <= 127:
        return 'A'
    elif 128 <= first_octet <= 191:
        return 'B'
    elif 192 <= first_octet <= 223:
        return 'C'
    elif 224 <= first_octet <= 239:
        return 'D (Multicast)'
    elif 240 <= first_octet <= 255:
        return 'E (Reserved)'
    else:
        return 'Invalid IP address'


def convert_to_binary(ip_address):
    binary_parts = [format(int(part), '08b') for part in ip_address.split('.')]
    return '.'.join(binary_parts)


def calculate_subnet(ip_address, subnet_mask):
    subnet_parts = []
    ip_parts = ip_address.split('.')
    mask_parts = subnet_mask.split('.')

    for i in range(4):
        subnet_part = int(ip_parts[i]) & int(mask_parts[i])
        subnet_parts.append(str(subnet_part))    # part into parts

    return '.'.join(subnet_parts)


def display_subnet_generator(ip_address, subnet_mask):
    subnet = calculate_subnet(ip_address, subnet_mask)
    print(f"\nInitial IP Address: {ip_address}")
    print(f"Class: {get_ip_class(ip_address)}")
    print(f"Binary Representation: {convert_to_binary(ip_address)}")
    print(f"Subnet Mask: {subnet_mask}")
    print(f"Subnet Generator: {subnet}")


if __name__ == "__main__":
    # Example usage
    ip_address = input("Enter an IP address: ")
    subnet_mask = input("Enter the subnet mask: ")

    display_subnet_generator(ip_address, subnet_mask)

import socket

def get_host_info(input_value):
    try:
        # Try to interpret input as an IP address
        ip_address = socket.gethostbyname(input_value)
        host_name, _, _ = socket.gethostbyaddr(ip_address)  #The underscores (_) are used as placeholder variables for the alias list and IP address list
        return f"IP Address: {ip_address}, Hostname: {host_name}"

    except socket.herror:
        try:
            # Try to interpret input as a URL
            ip_address = socket.gethostbyname(input_value)
            host_name, _, _ = socket.gethostbyaddr(ip_address)
            return f"IP Address: {ip_address}, Hostname: {host_name}"

        except socket.herror:
            return "Invalid input. Please provide a valid IP address or URL."

# Get user input
user_input = input("Enter an IP address or URL: ")

# Perform DNS lookup and print the result
result = get_host_info(user_input)
print(result)

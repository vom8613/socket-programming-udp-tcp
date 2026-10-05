import socket

SERVER_IP = "192.168.196.215"
SERVER_PORT = 12000
BUFFER_SIZE = 2048
TIMEOUT_LIMIT = 3.0  # seconds

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # Requirement: Prevent indefinite client blocking if packet drops
    client_socket.settimeout(TIMEOUT_LIMIT)

    try:
        user_input = input("Enter an integer to evaluate: ").strip()
        if not user_input:
            print("[UDP Client] Input cannot be blank.")
            return

        # Transmit datagram to the server
        client_socket.sendto(user_input.encode("utf-8"), (SERVER_IP, SERVER_PORT))

        # Wait for reply
        data, server_address = client_socket.recvfrom(BUFFER_SIZE)
        print(f"[UDP Client] Reply from {server_address}: {data.decode('utf-8')}")

    except socket.timeout:
        print("[UDP Client] Error: Request timed out. Server unreachable or packet lost.")
    except socket.error as e:
        print(f"[UDP Client] Socket error: {e}")
    finally:
        client_socket.close()

if __name__ == "__main__":
    main()
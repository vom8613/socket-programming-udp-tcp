import socket

SERVER_HOST = "0.0.0.0"  # Listen on all network interfaces
SERVER_PORT = 12000
BUFFER_SIZE = 2048

def main():
    # AF_INET specifies IPv4; SOCK_DGRAM specifies UDP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((SERVER_HOST, SERVER_PORT))
    print(f"[UDP Server] Ready and listening on port {SERVER_PORT}...")

    try:
        while True:
            # recvfrom receives data and the (client_ip, client_port) tuple
            data, client_address = server_socket.recvfrom(BUFFER_SIZE)
            raw_msg = data.decode("utf-8").strip()
            print(f"[UDP Server] Received '{raw_msg}' from {client_address}")

            # Input validation & business logic (Even/Odd checker)
            try:
                num = int(raw_msg)
                result = "EVEN" if num % 2 == 0 else "ODD"
                response = f"SUCCESS: {num} is {result}"
            except ValueError:
                response = f"ERROR: '{raw_msg}' is not a valid integer."

            # Send response back to the client's ephemeral port
            server_socket.sendto(response.encode("utf-8"), client_address)

    except KeyboardInterrupt:
        print("\n[UDP Server] Shutting down...")
    finally:
        server_socket.close()

if __name__ == "__main__":
    main()
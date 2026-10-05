import socket

SERVER_HOST = "0.0.0.0"
SERVER_PORT = 12000
BUFFER_SIZE = 2048

def main():
    # AF_INET specifies IPv4; SOCK_STREAM specifies TCP
    welcoming_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Release the socket immediately after closing to avoid TIME_WAIT reuse errors
    welcoming_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    welcoming_socket.bind((SERVER_HOST, SERVER_PORT))
    welcoming_socket.listen(5)  # Backlog of 5 connections
    print(f"[TCP Server] Listening for connections on port {SERVER_PORT}...")

    try:
        while True:
            # accept() blocks until a client completes the 3-way handshake
            connection_socket, client_address = welcoming_socket.accept()
            print(f"[TCP Server] Connection established with {client_address}")

            try:
                data = connection_socket.recv(BUFFER_SIZE)
                if data:
                    raw_msg = data.decode("utf-8").strip()
                    print(f"[TCP Server] Received '{raw_msg}'")

                    try:
                        num = int(raw_msg)
                        result = "EVEN" if num % 2 == 0 else "ODD"
                        response = f"SUCCESS: {num} is {result}\n"
                    except ValueError:
                        response = f"ERROR: '{raw_msg}' is not an integer.\n"

                    connection_socket.sendall(response.encode("utf-8"))
            except ConnectionResetError:
                print(f"[TCP Server] Client {client_address} abruptly dropped.")
            finally:
                connection_socket.close()
                print(f"[TCP Server] Connection with {client_address} closed.")

    except KeyboardInterrupt:
        print("\n[TCP Server] Shutting down...")
    finally:
        welcoming_socket.close()

if __name__ == "__main__":
    main()
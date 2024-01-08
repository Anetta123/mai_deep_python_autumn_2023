"""Server implementation"""
import re
import json
import threading
import argparse
import socket
import queue
import requests
from bs4 import BeautifulSoup
from collections import Counter

HANDLED_URLS = 0


def get_words_from_url(url: str) -> list:
    """Function to take all the words from url"""
    try:
        response = requests.get(url, timeout=5)
        words = []
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            text = soup.get_text()
            words = re.findall(r'\b\w+\b', text)
        return words
    except:
        print("Connection refused")


def worker(client_socket_queue: queue.Queue, c: int) -> None:
    """Defining worker attitude"""
    while True:
        client_socket = client_socket_queue.get()
        handle_client(client_socket, c)


def handle_client(client_socket: socket.socket, c: int) -> None:
    """Function to handle each client"""
    buffer = ""
    while True:
        # Reading from client's socket
        data = client_socket.recv(1024).decode('utf-8')
        if not data:
            break

        buffer += data
        while "\n" in buffer:
            url, buffer = buffer.split("\n", 1)
            words = get_words_from_url(url)
            # Count words
            d = list(Counter(words).items())
            d.sort(reverse=True, key=lambda x: x[1])

            # Sending to client JSON
            json_dump = json.dumps(dict(d[0:c]), ensure_ascii=False)
            client_socket.sendall(json_dump.encode('utf-8'))

            global HANDLED_URLS
            HANDLED_URLS += 1
            print(f"Urls already have handled: {HANDLED_URLS}")
    client_socket.close()


def parse_flags() -> tuple:
    """Parsing flags from cmd"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--workers", "-w", help="Number of workers")
    parser.add_argument("--bests", "-k", help="Number of the most frequent words")
    try:
        args = parser.parse_args()
        return int(args.workers), int(args.bests)
    except argparse.ArgumentError as e:
        parser.print_help(sys.stderr)


def main() -> None:
    """Main function"""
    # Define host and port
    host = '127.0.0.1'
    port = 7777

    # Parse flags from cmd
    workers, count = parse_flags()

    # Create socket and bind it with host + port
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))

    # Listen
    server_socket.listen(64)

    # Create clients socket Queue
    client_socket_queue = queue.Queue()

    # Create threads
    threads = []
    for _ in range(workers):
        thread = threading.Thread(target=worker, args=(client_socket_queue, count))
        thread.start()
        threads.append(thread)

    try:
        print("Server is listening!")
        while True:
            client_socket, addr = server_socket.accept()
            client_socket_queue.put(client_socket)
    finally:
        server_socket.close()


if __name__ == "__main__":
    main()

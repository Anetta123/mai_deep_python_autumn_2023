"""Client implementation"""
import json
import threading
import socket
import argparse
import queue
import sys


def parse_flags() -> tuple:
    """Parsing flags from cmd"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--urls", "-u", help="File with urls")
    parser.add_argument("--threads", "-t", help="Number of threads")
    try:
        args = parser.parse_args()
        return args.urls, int(args.threads)
    except argparse.ArgumentError as e:
        parser.print_help(sys.stderr)



def action(client_socket: socket.socket, urls_queue: queue.Queue) -> None:
    """Action to do for every thread"""
    while True:
        url = urls_queue.get()
        client_socket.send(f"{url.strip()}\n".encode('utf-8'))
        response = client_socket.recv(1024)
        decoded_response = response.decode('utf-8')
        data_json = json.loads(decoded_response)
        print(f"{url}:  {data_json}")



def main() -> None:
    """Main function"""
    # Defining
    host = '127.0.0.1'
    port = 7777

    # Create urls_queue
    urls, threads_c = parse_flags()
    urls_queue = queue.Queue()

    # Create client socket and connect to server
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    # Create threads
    threads = []
    for _ in range(threads_c):
        thread = threading.Thread(target=action, args=(client_socket, urls_queue))
        thread.start()
        threads.append(thread)

    # Fill the queue with urls
    with open(urls, 'r') as file:
        for line in file:
            urls_queue.put(line)


if __name__ == '__main__':
    main()
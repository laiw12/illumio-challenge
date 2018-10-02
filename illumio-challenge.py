import ipaddress
import csv

class Firewall:

    def __init__(self, csv_path):
        self.__rules = []
        with open(csv_path, encoding='utf-8-sig') as csv_file:
            csvr = csv.reader(csv_file)
            for line in csvr:
                self.__rules.append(line)
        print(self.__rules)
                
    """
    Accept a packet into the firewall.

    Paramters: 
    direction (string): “inbound” or “outbound”
    protocol (string): exactly one of “tcp” or “udp”, all lowercase
    port (int): an integer in the range [1, 65535]
    ip_address (string): a single well-formed IPv4 address.

    Returns:
    boolean: Whether or not to accept packet
    """
    def accept_packet(self, direction, protocol, port, ip_address):
        pass

if __name__ == "__main__":
    fw = Firewall("/Users/jon/desktop/fw.csv")
    fw.accept_packet("", "", "", "")
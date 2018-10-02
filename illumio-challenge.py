import ipaddress
import csv
import unittest

class Firewall:

    def __init__(self, csv_path):
        self.__rules = []
        with open(csv_path, encoding='utf-8-sig') as csv_file:
            csvr = csv.reader(csv_file)
            for line in csvr:
                self.__rules.append(line)
                
                
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
    # Rule[0]: direction rule, Rule[1]: protocol rule, Rule[2]: port rule, Rule[3]: ip rule
        for rule in self.__rules:
            if not self.check_direction(rule[0], direction):
                continue
            elif not self.check_protocol(rule[1], protocol):
                continue
            elif not self.check_port(rule[2], port):
                continue
            elif not self.check_ip_address(rule[3], ip_address):
                continue
            return True
        return Fals
    
    #Checks for valid direction rules
    def check_direction(self, rule, direction):
        if direction == rule:
            return True
        else:
            return False

    #Checks for valid protocol rules
    def check_protocol(self, rule, protocol):
        if protocol == rule:
            return True
        else:
            return False
    
    #Checks for valid port rules
    def check_port(self, rule, port):
        str_port = str(port)
        if "-" in rule:
            port_range = rule.split("-")
            return port_range[0] <= str_port and str_port <= port_range[1]
        else:
            return str_port == rule
    
    #Checks for valid ip address rules 
    def check_ip_address(self, rule, ip_address):
        if "-" in rule:
            ip_range = rule.split("-")
            ip = ipaddress.ip_address(ip_address)
            ip_range1 = ipaddress.ip_address(ip_range[0])
            ip_range2 = ipaddress.ip_address(ip_range[1])
            return ip_range1 <= ip and ip <= ip_range2
        else:
            return ip_address == rule

class FirewallTest(unittest.TestCase):

    def test1(self):
        self.assertTrue(fw.accept_packet("inbound", "tcp", 80, "192.168.1.2"))

    def test2(self):
        self.assertTrue(fw.accept_packet("inbound", "udp", 53, "192.168.2.1"))
    
    def test3(self):
        self.assertTrue(fw.accept_packet("outbound", "tcp", 10234, "192.168.10.11"))
    
    def test4(self):
        self.assertFalse(fw.accept_packet("inbound", "tcp", 81, "192.168.1.2"))

    def test5(self):
        self.assertFalse(fw.accept_packet("inbound", "udp", 24, "52.12.48.92"))

if __name__ == "__main__":
    fw = Firewall("/Users/jon/desktop/fw.csv")
    unittest.main()
import scapy.all as scapy
import logging

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)


def main(ip):
    packet = 'ff:ff:ff:ff:ff:ff'
    try:
        arp_request = scapy.ARP(pdst=ip)
        broadcast = scapy.Ether(dst=packet)
        arp_request_broadcast = broadcast / arp_request
        answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
        clients_list = []
        for el in answered_list:
            clients_dict = {'ip': el[1].psrc, 'mac': el[1].hwsrc}
            clients_list.append(clients_dict)
        return clients_list
    except Exception as ex:
        print(ex)


def res(res_list):
    print('\n[IP]\t\t\t\t[MAC ADDRESS]\t\t\t\t[VENDOR NAME]')
    for clients in res_list:
        print(clients['ip'] + '      \t'
              + clients['mac'])


if __name__ == '__main__':
    scan_result = main('192.168.0.155/2')
    res(scan_result)

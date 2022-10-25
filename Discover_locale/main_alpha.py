import datetime
import scapy.all as scapy
import logging
import requests
import time

logging.getLogger('scapy.runtime').setLevel(logging.ERROR)


def main(ip):
    packet = 'ff:ff:ff:ff:ff:ff'
    main_bar = '\n[IP]\t\t\t\t[MAC ADDRESS]\t\t\t\t[VENDOR NAME]'
    date = datetime.datetime.now().strftime("%d-%m-%Y")
    try:
        # Отправка arp запросов на все указанные адреса
        arp_request = scapy.ARP(pdst=ip)
        broadcast = scapy.Ether(dst=packet)
        arp_request_broadcast = broadcast / arp_request
        answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
        print(main_bar)
        for el in answered_list:
            # Запись всего диапозона в словарь и перебор mac адресов
            clients_dict = {'ip': el[1].psrc, 'mac': el[1].hwsrc}
            mac_scanner = {el[1].hwsrc}
            time.sleep(0.75)
            for addr in mac_scanner:
                vendor = requests.get('http://api.macvendors.com/' + addr).text
                all_ip = clients_dict['ip'] + '      \t' + clients_dict['mac'] + '\t\t\t' + vendor
                with open(f'ip_output/ip_list({date}).txt', 'a') as f:
                    f.write(all_ip + '\n')
                    f.close()
                print(all_ip)
    except Exception as ex:
        print(ex)


if __name__ == '__main__':
    main(input('Set range: '))

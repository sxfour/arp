# arp
Scanning all locale network, with arp request using scapy, and find vendor names with macs using API
This modules we need to install with pip
!pip install scapy
![Снимок](https://user-images.githubusercontent.com/112577182/197688042-5c8565c6-c6fc-4ade-aebb-aca9dfacdf70.PNG)

This function sends arp requests to the entire range of addresses specified on the local network, and if someone responds, writes it to the print, as well as a text file with the entire arp scan report is created as a result of the scan, the api name vendor is also used (due to its scanning speed is significantly reduced, since the service is absolutely free)
This code works on python3, linux, windows (need install winpcap)
![изображение](https://user-images.githubusercontent.com/112577182/197688710-06860ca8-bcc0-4883-9328-aa7c3b966484.png)
Output:![изображение](https://user-images.githubusercontent.com/112577182/197688905-6b4c87be-15d2-4e1a-b375-06ee6b83f985.png)

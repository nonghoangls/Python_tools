#Scan port ở chế độ không đồng bộ.
#import thư viện nmap
import nmap

#hàm in thông tin về host và kết quả quét cổng
def callback_result(host, scan_result):
    print(host, scan_result)

#Hàm scan_ports được định nghĩa để thực hiện quét cổng trên một danh sách các địa chỉ IP (hoặc tên miền) và một danh sách các cổng.
def scan_ports(hosts, ports):
    #PortScannerAsync từ thư viện nmap để thực hiện quét cổng không đồng bộ.
    portScannerAsync = nmap.PortScannerAsync()
    #vòng lặp lồng nhau để lặp qua từng địa chỉ IP trong danh sách hosts và từng cổng trong danh sách ports.
    for host in hosts:
        for port in ports:
            #PortScannerAsync, truyền vào địa chỉ IP, cổng và một hàm callback (callback_result) để xử lý kết quả quét.
            portScannerAsync.scan(hosts=host, arguments=f"-p {port}", callback=callback_result)
#vòng lặp while để kiểm tra xem quá trình quét cổng vẫn đang tiếp tục hay không, bằng cách sử dụng phương thức still_scanning()
    # của đối tượng PortScannerAsync.
    #Trong mỗi vòng lặp của vòng while, chúng ta in ra thông báo "Scanning >>>" để biết rằng chương trình đang tiếp tục quét.

    while portScannerAsync.still_scanning():
        print("Scanning >>>")
        #wait(2) để chờ đợi 2 giây trước khi kiểm tra lại xem quét cổng đã hoàn tất chưa.
        portScannerAsync.wait(2)

#hàm chạy chiính với danh sách hosts và port

if __name__ == "__main__":
    hosts = ["scanme.nmap.org", "facebook.com"]  # Danh sách các địa chỉ IP hoặc tên miền bạn muốn quét
    ports = ["21", "22", "80", "443"]  # Danh sách các cổng bạn muốn quét
#gọi hàm scan_port với tham số truyền vào là các host và port ở trên
    scan_ports(hosts, ports)

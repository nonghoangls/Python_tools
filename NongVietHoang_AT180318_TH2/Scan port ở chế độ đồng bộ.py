#Scan port ở chế độ đồng bộ
import nmap

#tạo class NmapScanner đóng gói cac chức năng quét nmap
class NmapScanner:
    #Trong hàm khởi tạo __init__, một đối tượng PortScanner từ thư viện nmap được tạo ra và gắn vào thuộc tính portScanner của lớp.
    #self là một tham chiếu tới đối tượng hiện tại của lớp
       def __init__(self):
             self.portScanner = nmap.PortScanner()

       #Phương thức nmapScan được định nghĩa để thực hiện quét cổng cho một địa chỉ IP và một cổng cụ thể.
       #Đầu vào của phương thức này bao gồm địa chỉ IP và cổng
       def nmapScan(self, ip_address, port):
           self.portScanner.scan(ip_address, port)
           print("[+] Executing command: ", self.portScanner.command_line())
def main():
    #nhập địa chỉ ip và gán nó vào biến ip_address
    ip_address = input("IP scan: ")
    #1 danh sách các cổng để kiểm tra trong quá trình quét
    ports = ["80", "443", "8080", "21","23"]
    #vòng lap for với biến chạy port, gọi hàm nmapScan từ lớp NmapScanner với hai tham số: ip_address và port.
    for port in ports:
        NmapScanner().nmapScan(ip_address, port)

#hàm chạy chính với phương thức main()
if __name__ == "__main__":
    main()
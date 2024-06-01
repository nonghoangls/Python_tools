# Kiểm tra các port với địa chỉ host xác định (VD: dantri.com.vn)
# 42.113.206.26
#thu vien tương tác với công cụ quét Nmap.
import nmap
#Tạo một thể hiện của lớp PortScanner để thực hiện quét.
portScanner = nmap.PortScanner()
#Yêu cầu người dùng nhập tên máy chủ hoặc địa chỉ IP của máy chủ mục tiêu để quét.
host_scan = input("Host scan: ")
#cho ds các cổng trong biến portlist
#21:FTP, 22:SSH,23:Telnet, 25:SMTP, 80:HTTP, 443:HTTPS, 8080: cong máy chủ web phổ biến
portlist = "21,22,23,25,80,443,8080"
#Thực hiện quét cổng bằng cách sử dụng đối tượng portScanner đã tạo
#hosts = host_scan: là biên lưu máy chủ mục tiêu từ đầu vào của người dùng
#arguments = "-n -p" + portlist: Thiết lập các đối số quét:
           #-n: Vô hiệu hóa giải quyết DNS (nhanh hơn nhưng ít thông tin hơn).
           #-p: Chỉ định các cổng để quét bằng biến portlist.
portScanner.scan(hosts = host_scan, arguments = "-n -p" + portlist)
#In lệnh dòng lệnh chính xác được sử dụng cho quét (hữu ích để gỡ lỗi hoặc tham khảo).
print(portScanner.command_line())
#Tạo danh sách các bộ ba chứa tên máy chủ, trạng thái quét tổng thể của nó
#(ví dụ: "up" hoặc "down") và trạng thái dịch vụ (ví dụ: "open", "closed", "filtered").
#portScanner.all_hosts() Trả về danh sách tất cả các máy chủ đã quét.
hosts_list = [(x, portScanner[x]["status"]["state"]) for x in portScanner.all_hosts()]
#Lặp qua từng tên máy chủ và trạng thái tương ứng của nó.
for host, status in hosts_list:
    #In tên máy chủ, trạng thái quét tổng thể và trạng thái dịch vụ của nó.
    print(host,status)
# Lặp qua tất cả các giao thức được quét cho máy chủ cụ thể (host) từ đầu vào của người dùng
for protocol in portScanner[host].all_protocols():
    #In giao thức hiện tại (thường là "tcp")
    print("Protocol: %s" % protocol)
    #Lấy danh sách các cổng đã quét cho giao thức hiện tại.
    listport = portScanner[host]["tcp"].keys()
    #Lặp qua từng cổng đã quét
    for port in listport:
        #In số cổng, trạng thái (ví dụ: "mở", "đóng", "lọc") và lý do (nếu có) của nó.
        print("Port: %s Stute : %s" % (port,portScanner[host][protocol][port]["state"]))



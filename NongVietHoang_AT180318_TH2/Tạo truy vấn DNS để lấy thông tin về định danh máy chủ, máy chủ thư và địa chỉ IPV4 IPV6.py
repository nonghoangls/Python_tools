#Tạo truy vấn DNS để lấy thông tin về định danh máy chủ, máy chủ thư và địa chỉ IPV4/IPV6
#import thư viện dns để có thế su dụng chức năng truy vấn DNS
import dns.resolver

#danh sách tên miền truy vấn duoc gán cho biến hosts
hosts = ["google.com", "google", "yahoo.com", "yahoo.com"]

#vòng lặp for để duyet từng miền trong hosts và lưu vào biến host
for host in hosts:
    #in ra tên miền
    print("Hostname:", host)
    try:
        #truy vấn và lấy ra địa chỉ ipv4 từ tên miền
        ip = dns.resolver.resolve(host, "A")
        #vòng lặp for duyệt qua từng địa chỉ gán ở biến ip, lưu vào bien i
        #và in biến i là địa chỉ các ip của miền
        for i in ip:
            print("IP Address:", i)
    #bắt ngoại lệ các trường hợp nếu xảy ra lỗi
    #1: không tìm thấy địa chỉ từ miền
    #2:không tồn tại miền
    #3:thời gian truy vấn DNS quá hạn
    #4:lỗi xảy ra
    except dns.resolver.NoAnswer:
        print("No A record found for this domain.")
    except dns.resolver.NXDOMAIN:
        print("Non-existent domain.")
    except dns.resolver.Timeout:
        print("Timeout occurred during DNS query.")
    except Exception as e:
        print("An error occurred:", e)

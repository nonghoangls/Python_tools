#Tìm danh sách địa chỉ IP cho các máy chủ FTP đăng nhập ở chế độ Anonymous
# shodan cho phép tương tác với Shodan API
import  shodan
#Danh sách rỗng để lưu trữ địa chỉ IP của các máy chủ được tìm thấy
servers = []
#biến sodanApi sử dụng khóa API Shodan
shodanApi = shodan.Shodan("cdYPlZMAGfs38VOAYWu43N3dNCsE7AFr")
#Thực hiện tìm kiếm Shodan API với chuỗi truy vấn được cung cấp. Truy vấn tìm kiếm các máy chủ luu vào biến result
#cổng 21 đc dùng cho giao thức FTP
result = shodanApi.search("port: 21 Anonymous user logged in")
#In số lượng máy chủ được tìm thấy khớp với tiêu chí tìm kiếm(port 21 và người ẩn danh đăng nhập vào cổng này)
print("hosts number: " + str(len(result["matches"])))
#Xử lý từng máy chủ được tìm thấy trong kết quả tìm kiếm.
for result in result["matches"]:
    #Kiểm tra xem khóa "ip_str" có tồn tại trong từ điển kết quả hiện tại và có giá trị (địa chỉ IP) hay không.
    #Không phải tất cả kết quả đều có địa chỉ IP hợp lệ.
    if result["ip_str"] is not None:
        #Nếu địa chỉ IP hợp lệ, thêm nó vào danh sách servers.
        servers.append(result["ip_str"])
#Duyệt qua danh sách servers đã được thêm.print(server): In địa chỉ IP của từng máy chủ được tìm thấy từ tìm kiếm Shodan.
for server in servers:
    print(server)
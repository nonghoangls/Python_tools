#Lấy thông tin về một địa chỉ IP cụ thể, chẳng hạn như máy chủ DNS và vị trí địa lý...
#import thư vien requests và os
#request cho phép thực hiện các yêu cầu tới HTTP đến APIs
#Thư viện này được sử dụng để truy cập các biến môi trường.
import requests
import os
#tạo biến SHODAN_API_KEY và gán nó với API được lưu trữ trong biến môi trường của hệ thong(SHODAN_API_KEY)
SHODAN_API_KEY = os.environ['SHODAN_API_KEY']

#địa chỉ DNS của Google
ip = '8.8.8.8'

#Hàm này lấy một địa chỉ IP làm đầu vào và lấy thông tin về nó bằng cách sử dụng Shodan API
def ShodanInfo(ip):
    #khối try-except xử li ngoại le trong quá trình yêu cầu api
    try:
        #requests.get(...): Dòng này thực hiện yêu cầu GET đến điểm cuối API Shodan để lấy thông tin về máy chủ.
        #URL được định dạng bằng f-strings để bao gồm IP mục tiêu và khóa API của bạn.
        #f"https://api.shodan.io/shodan/host/{ip}?key=${SHODAN_API_KEY}":
        #Chuỗi này xây dựng URL yêu cầu API với IP được chỉ định và khóa API của bạn được lưu trữ trong biến SHODAN_API_KEY.
        #json(): Phương thức này chuyển đổi phản hồi JSON từ API thành một từ điển Python để dễ dàng truy cập dữ liệu hơn.
        result = requests.get(f"https://api.shodan.io/shodan/host/{ip}?key=${SHODAN_API_KEY}").json()
    except Exception as exception:
        #trường hợp ngoại lệ, khối này sẽ bắt nó và gán một từ điển với khóa "error" cho biến result.
        result = {"error":"Information not available"}
    #Hàm trả về từ điển chứa phản hồi API Shodan (nếu thành công) hoặc thông báo lỗi (nếu có ngoại lệ).
    return result
#gọi hàm ShodanInfo với biến ip ở đây đc truyền vào là 8.8.8.8
print(ShodanInfo(ip))
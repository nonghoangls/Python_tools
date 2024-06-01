#Tìm kiếm các địa chỉ dễ bị tổn thương trong máy chủ với fuzzing
#thư viện requests cho phép thuc hiện yêu cầu HTTP đến trang web
import requests
#tạo 1 danh sách login trống de luu trữ các ip tiem nang
logins = []
#đọc tệp với đường dẫn ở dưới
with open("E:/PycharmProjects/NongVietHoang_AT180318_TH2/Logins.txt", "r") as filehandle:
    ##Nó duyệt qua từng dòng trong tệp
    for line in filehandle:
        #xóa ký tự dòng mới (\n) ở cuối
        login = line[:-1]
        #thêm dòng (thông tin đăng nhập tiềm năng) vào danh sách logins
        logins.append(login)
#lưu web mục tiêu
domain = 'http://testphp.vulnweb.com'
#Mã duyệt qua từng thông tin đăng nhập trong danh sách logins.
for login in logins:
    print("Checking... " + domain + login)
    #gửi một yêu cầu HTTP GET đến URL đó bằng requests.get.
    #kiểm tra mã trạng thái phản hồi
    response = requests.get(domain+login)
    #Nếu mã trạng thái là 200 (OK), nó cho biết rằng máy chủ đã phản hồi với một trang thành công,
    #cho thấy một nguồn tài nguyên đăng nhập tiềm năng đã được tìm thấy.
    if response.status_code == 200:
        print("Login resource detected: " + login)

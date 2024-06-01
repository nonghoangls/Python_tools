#Tìm lỗi SQL injection đối với một trang web sử dụng dự án Fuzzing

#import thư viện

import requests

# Đường dẫn của trang web cần kiểm tra
url = "http://testphp.vulnweb.com/listproducts.php?cat="

# Đọc các chuỗi từ tệp errors.txt của FuzzDB
with open("E:/PycharmProjects/NongVietHoang_AT180318_TH2/MySQL.txt", "r") as file:
    error_strings = file.readlines()

# Lặp qua từng chuỗi lỗi và gửi yêu cầu HTTP để kiểm tra lỗ hổng SQL injection
for error_string in error_strings:
    # Loại bỏ dấu xuống dòng và khoảng trắng từ chuỗi
    error_string = error_string.strip()
    # Tạo URL với tham số bị tấn công bằng cách chèn chuỗi lỗi
    payload_url = f"{url}?id={error_string}"
    # Gửi yêu cầu HTTP và kiểm tra phản hồi
    response = requests.get(payload_url)
    # Kiểm tra nếu có dấu hiệu của lỗ hổng SQL injection trong phản hồi
    if "error" in response.text:
        print(f"Vulnerable to SQL injection: {payload_url}")

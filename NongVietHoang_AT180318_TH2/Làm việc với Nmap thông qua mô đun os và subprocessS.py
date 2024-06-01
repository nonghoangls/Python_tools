#Làm việc với Nmap thông qua mô đun os và subprocessS
#import thư viện os, cho phép tương tác với hệ điều hành.
import os
#khai báo biến nmap_command và gán cho nó giá trị là một chuỗi
#nmap: Tên chương trình quét mạng nmap
#-sT: Cờ này yêu cầu nmap thực hiện quét TCP SYN. Loại quét này nhanh hơn quét kết nối TCP đầy đủ nhưng cung cấp ít thông tin hơn.
#157.240.199.35 địa chỉ mục tiêu muốn quét
nmap_command = 'nmap -sT 157.240.199.35'
#os.system để thực thi lệnh được lưu trữ trong biến nmap_command.
#Hàm này sẽ thực thi lệnh nmap.
os.system(nmap_command)
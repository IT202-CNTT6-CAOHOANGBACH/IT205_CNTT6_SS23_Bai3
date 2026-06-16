""" 
1.
    rikkei_aviation/
│
├── core/
│   ├── __init__.py          # Đánh dấu core là một package
│   ├── logistics.py         # Chức năng 1: Thống kê hậu cần
│   └── manager.py           # Chức năng 2: Tiếp nhận chuyến bay mới
│
├── utils/
│   ├── __init__.py          # Đánh dấu utils là một package
│   ├── time_helper.py       # Chức năng 3: Tính toán ETA
│   └── file_helper.py       # Chức năng 4: Khởi tạo thư mục log
│
├── main.py                  # Điều hướng Menu chính (Luồng thực thi)

2.
Cú pháp from math import * có tác hại:
    - Ô nhiễm không gian tên (Namespace Pollution)
    - Mất tính tường minh
    - Giảm hiệu năng
Giải pháp tối ưu: sử dụng import math
"""


# Import các hàm nghiệp vụ từ các Package/Module riêng biệt
from Session23.IT205_CNTT6_SS23_Bai3.core.logistics import display_flights_and_logistics
from Session23.IT205_CNTT6_SS23_Bai3.core.manager import add_new_flight
from Session23.IT205_CNTT6_SS23_Bai3.utils.time_helper import calculate_eta
from Session23.IT205_CNTT6_SS23_Bai3.utils.file_helper import initialize_log_directory

def main():
    # Dữ liệu khởi tạo ban đầu của hệ thống
    flights = [
        {"flight_id": "RA001", "passengers": 154, "depart_time": "2026-06-15 08:00:00", "duration_min": 120},
        {"flight_id": "RA002", "passengers": 85,  "depart_time": "2026-06-15 13:30:00", "duration_min": 45}
    ]

    while True:
        print("\n===== HỆ THỐNG ĐIỀU HÀNH BAY RIKKEI AVIATION =====")
        print("1. Hiển thị lịch trình và Thống kê hậu cần")
        print("2. Tiếp nhận chuyến bay mới")
        print("3. Tính thời gian hạ cánh dự kiến (ETA)")
        print("4. Khởi tạo thư mục lưu trữ log hệ thống")
        print("5. Thoát chương trình")
        print("==================================================")
        
        # Bẫy 4 — Nhập lỗi Menu (Nhập chữ, ký tự lạ hoặc nằm ngoài khoảng 1-5)
        choice = input("Nhập lựa chọn của bạn: ")

        match choice:
            case "1":
                display_flights_and_logistics(flights)
            case "2":
                add_new_flight(flights)
            case "3":
                calculate_eta(flights)
            case "4":
                initialize_log_directory()
            case "5":
                print("\nCảm ơn kỹ sư đã sử dụng hệ thống!")
                break
            case _:
                print(">> Lỗi: Lựa chọn không hợp lệ! Vui lòng nhập lại một số từ 1 đến 5.")

if __name__ == "__main__":
    main()
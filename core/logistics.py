import math

def display_flights_and_logistics(flight_list):
    """Chức năng 1: Hiển thị lịch trình và Thống kê hậu cần"""
    print("\n----- DANH SÁCH CHUYẾN BAY & HẬU CẦN -----")
    if not flight_list:
        print("Hiện chưa có chuyến bay nào trong hệ thống.")
        return
        
    for index, flight in enumerate(flight_list, start=1):
        # Tính số thùng nước khoáng dự phòng (10 khách/thùng, làm tròn lên)
        passengers = flight["passengers"]
        water_boxes = math.ceil(passengers / 10)
        
        print(f"{index}. Mã: {flight['flight_id']} | "
              f"Khởi hành: {flight['depart_time']} | "
              f"Số khách: {passengers:<3} | "
              f"Dự phòng: {water_boxes} thùng nước.")
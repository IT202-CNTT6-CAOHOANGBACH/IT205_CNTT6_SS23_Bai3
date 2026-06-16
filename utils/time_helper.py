from datetime import datetime, timedelta

def calculate_eta(flight_list):
    """Chức năng 3: Tính toán thời gian hạ cánh dự kiến (ETA)"""
    print("\n----- TÍNH TOÁN THỜI GIAN HẠ CÁNH (ETA) -----")
    search_id = input("Nhập mã chuyến bay cần tính: ").strip().upper()
    
    # Tìm kiếm chuyến bay trong danh sách
    target_flight = None
    for flight in flight_list:
        if flight["flight_id"] == search_id:
            target_flight = flight
            break
            
    if not target_flight:
        print(f">> Không tìm thấy chuyến bay có mã {search_id}!")
        return

    # Xử lý tính toán thời gian với datetime và timedelta
    depart_time_str = target_flight["depart_time"]
    duration_min = target_flight["duration_min"]
    
    # Ép chuỗi sang kiểu datetime
    depart_datetime = datetime.strptime(depart_time_str, "%Y-%m-%d %H:%M:%S")
    # Cộng thêm số phút bay
    eta_datetime = depart_datetime + timedelta(minutes=duration_min)
    
    # Định dạng lại đầu ra thành chuỗi chuẩn để hiển thị
    eta_str = eta_datetime.strftime("%Y-%m-%d %H:%M:%S")
    
    print(f"-> Chuyến bay {search_id} cất cánh lúc: {depart_time_str}")
    print(f"-> Thời gian hạ cánh dự kiến (ETA): {eta_str}")
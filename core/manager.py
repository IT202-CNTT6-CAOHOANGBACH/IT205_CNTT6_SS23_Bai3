from datetime import datetime

def check_duplicate_id(flight_id, flight_list):
    """Helper Function: Kiểm tra trùng mã chuyến bay (Chuẩn hóa chữ hoa, xóa khoảng trắng)"""
    clean_id = flight_id.strip().upper()
    for flight in flight_list:
        if flight["flight_id"] == clean_id:
            return True
    return False

def add_new_flight(flight_list):
    """Chức năng 2: Tiếp nhận chuyến bay mới (Có bẫy lỗi định dạng và trùng lặp)"""
    print("\n----- TIẾP NHẬN CHUYẾN BAY MỚI -----")
    
    # 1. Nhập và kiểm tra mã chuyến bay (Bẫy 1)
    flight_id = input("Nhập mã chuyến bay: ").strip().upper()
    if not flight_id:
        print(">> Lỗi: Mã chuyến bay không được để trống!")
        return
        
    if check_duplicate_id(flight_id, flight_list):
        print(f">> Lỗi: Mã chuyến bay {flight_id} đã tồn tại trên hệ thống!")
        return

    # 2. Nhập số lượng hành khách
    try:
        passengers = int(input("Nhập số lượng hành khách: "))
        if passengers < 0:
            print(">> Lỗi: Số lượng hành khách không được âm!")
            return
    except ValueError:
        print(">> Lỗi: Số lượng hành khách phải là một số nguyên!")
        return

    # 3. Nhập thời gian khởi hành (Bẫy 2)
    depart_time_str = input("Nhập thời gian cất cánh (YYYY-MM-DD HH:MM:SS): ").strip()
    try:
        # Kiểm tra thử xem có đúng định dạng không
        datetime.strptime(depart_time_str, "%Y-%m-%d %H:%M:%S")
    except ValueError:
        print(">> Sai định dạng thời gian! Vui lòng nhập đúng chuẩn YYYY-MM-DD HH:MM:SS")
        return

    # 4. Nhập thời gian bay
    try:
        duration_min = int(input("Nhập số phút bay: "))
        if duration_min <= 0:
            print(">> Lỗi: Số phút bay phải lớn hơn 0!")
            return
    except ValueError:
        print(">> Lỗi: Số phút bay phải là một số nguyên!")
        return

    # Thêm mới vào danh sách gốc nếu tất cả các bước trên hợp lệ
    new_flight = {
        "flight_id": flight_id,
        "passengers": passengers,
        "depart_time": depart_time_str,
        "duration_min": duration_min
    }
    flight_list.append(new_flight)
    print(f">> Thêm chuyến bay {flight_id} thành công!")
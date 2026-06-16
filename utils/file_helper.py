import os

def initialize_log_directory():
    """Chức năng 4: Khởi tạo thư mục log hệ thống (Bẫy 3)"""
    print("\n----- KHỞI TẠO THƯ MỤC HỆ THỐNG -----")
    folder_name = "aviation_logs"
    
    # Kiểm tra thư mục tồn tại trước khi tạo để tránh FileExistsError
    if not os.path.exists(folder_name):
        print(f"[SYSTEM] Thư mục '{folder_name}' chưa tồn tại. Đang tiến hành khởi tạo...")
        try:
            os.mkdir(folder_name)
            print("[SYSTEM] Tạo thư mục thành công!")
        except Exception as e:
            print(f"[SYSTEM] Có lỗi xảy ra khi tạo thư mục: {e}")
    else:
        print("[SYSTEM] Thư mục đã tồn tại, bỏ qua bước khởi tạo.")
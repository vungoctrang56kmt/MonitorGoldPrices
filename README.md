#author name: Vũ Ngọc Trang
#class: K56KMT.01
#student code: K205480106035
---Đề tài: Xây dựng website theo dõi giá vàng----

1. Đầu tiên em sẽ tạo csdl gồm 2 bảng: Tabel và Stored Procedures.
- Tạo bảng có tên (GoldPrice): Lưu thông tin về giá vàng, bao gồm ID(PK), ngày, giá vàng.
- Tạo bảng Stored Procedures (SP_) có tên: SP_GetTopGoldPrices: Lấy thông tin của giá mấy loại giá vàng cao nhất hoặc ít nhất

2. Về Module đọc dữ liệu: Em sử dụng Python và FastAPI để tạo một API để lấy dữ liệu từ trang web chuyên về giá vàng.
- Sử dụng Web Scraping hoặc lấy dữ liệu qua API của các trang web chuyên về giá vàng.
- Dữ liệu bao gồm thông tin về giá vàng và ngày.

3. Node-RED:
- Xây dựng một chu trình trong Node-RED để tự động gọi API Python để lấy dữ liệu. Sau đó, xử lý dữ liệu và ghi dữ liệu vào cơ sở dữ liệu.
  
4. Web:
- Sử dụng các công nghệ như HTML, CSS, JavaScript để tạo giao diện web.
- Xây dựng một ứng dụng web để hiển thị dữ liệu từ cơ sở dữ liệu.
- Hiển thị danh sách giá vàng và ngày hoặc biểu đồ các giá vàng cao nhất.


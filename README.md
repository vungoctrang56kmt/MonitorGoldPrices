#author name: Vũ Ngọc Trang
#class: K56KMT.01
#student code: K205480106035
---Đề tài: Xây dựng website theo dõi giá vàng----

1. Cơ sở dữ liệu:

- Bảng: GoldPrice: Lưu thông tin về giá vàng, bao gồm ID (PK), thời gian, giá vàng.
- Stored Procedures (SP_): SP_GetLatestGoldPrices: (Lấy thông tin về giá vàng mới nhất) và SP_SaveGoldPrice: (Lưu giá vàng mới vào cơ sở dữ liệu).
- Dữ liệu bao gồm thông tin về thời gian và giá vàng.
  
2. Mô tả nguồn dữ liệu:
- Sử dụng Web Scraping hoặc lấy dữ liệu qua API của các trang web chuyên về giá vàng.
- Dữ liệu bao gồm thông tin về giá vàng và thời gian cập nhật.

3. Node-RED:
- Xây dựng một chu trình trong Node-RED để tự động gọi Stored Procedure SP_SaveGoldPrice để lưu giá vàng vào cơ sở dữ liệu.
- Node-RED sẽ gọi API Python (hoặc một dịch vụ khác) để lấy dữ liệu giá vàng và thời gian cập nhật, sau đó gửi dữ liệu này sang SP_SaveGoldPrice để lưu trữ.
  
4. Web:
- Xây dựng một ứng dụng web để hiển thị dữ liệu từ cơ sở dữ liệu.
- Hiển thị danh sách giá vàng và thời gian cập nhật hoặc biểu đồ các giá vàng theo thời gian.
- Sử dụng các công nghệ như HTML, CSS, JavaScript để tạo giao diện web.

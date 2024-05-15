#author name: Vũ Ngọc Trang
#class: K56KMT.01
#student code: K205480106035
---Đề tài: Xây dựng website theo dõi giá vàng----
- Giống như bài của thầy đã hướng dẫn. em sẽ làm về bài project riêng của mình về đề Tài Theo Dõi Giá Vàng
  tóm tắt:  em tạo code py fastAPI để lấy dữ liệu giá vàng bên ngoài -> dùng node-red để lưu về bảng db mà mình đã tạo-> sau đó tạo Sp_db để lấy dữ liệu ra-> Sau khi gọi api thì sử dụng http request lấy thông tin và đưa vào endpoint -> Cuối cùng dùng js để lấy dữ liệu và vẽ biểu đồ.
- Dưới đây là dự định và các bước thực hiện.
1. Thu thập Dữ liệu: Sử dụng Node-RED để kết nối với một nguồn dữ liệu về giá vàng, như API từ trang web tài chính hoặc các dịch vụ cung cấp dữ liệu tài chính. Thiết lập luồng làm việc trong Node-RED để lấy dữ liệu giá vàng theo định kỳ (ví dụ: mỗi giờ) từ nguồn dữ liệu và lưu vào cơ sở dữ liệu SQL.
2. Lưu trữ Dữ liệu: Sử dụng cơ sở dữ liệu SQL (ví dụ: MySQL, PostgreSQL) để lưu trữ dữ liệu giá vàng. Tạo bảng để lưu trữ thông tin như thời gian, giá vàng, và các thuộc tính khác.
3. Tạo API: Sử dụng FastAPI để tạo các endpoint API để truy xuất dữ liệu giá vàng từ cơ sở dữ liệu SQL. Thiết kế các endpoint để trả về dữ liệu giá vàng theo thời gian, loại vàng, và các yếu tố khác mà người dùng yêu cầu.
4. Giao diện Web: Tạo một giao diện web để hiển thị thông tin giá vàng từ API mà bạn đã tạo. Bạn có thể sử dụng HTML, CSS và JavaScript để xây dựng giao diện người dùng. Sử dụng AJAX hoặc Fetch API để gọi các endpoint API và hiển thị dữ liệu giá vàng lên giao diện web.
5. Biểu đồ: Sử dụng thư viện JavaScript như Chart.js hoặc D3.js để tạo các biểu đồ biểu diễn xu hướng giá vàng theo thời gian. Tích hợp các biểu đồ này vào giao diện web để người dùng có thể dễ dàng theo dõi và phân tích xu hướng giá vàng.

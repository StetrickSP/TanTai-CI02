# Câu 1: Trong lập trình, biến toàn cục (global variable) và biến cục bộ (local variable) có sự khác biệt quan trọng về phạm vi và cách sử dụng:
# + Biến toàn cục được khai báo bên ngoài tất cả các hàm và có phạm vi toàn cục, nghĩa là nó có thể được truy cập và thay đổi từ bất kỳ đâu trong chương trình.
# + Biến cục bộ được khai báo bên trong một hàm và chỉ có thể được truy cập và thay đổi trong phạm vi của hàm đó.

# Câu 2: Viết một đoạn mã Python để kiểm tra một số có phải là số nguyên tố hay không.
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
print(is_prime(-5)) 

# Câu 3: 
# Trong mô hình Client-Server, khi trình duyệt tải một trang web từ máy chủ, quá trình diễn ra như sau:
# 1. Trình duyệt (client) gửi một yêu cầu HTTP (HTTP request) đến máy chủ (server) thông qua địa chỉ URL của trang web.
# 2. Máy chủ nhận yêu cầu và xử lý nó. 
# 3. Sau khi xử lý xong, máy chủ gửi lại một phản hồi HTTP (HTTP response) chứa mã HTML của trang web về cho trình duyệt. 
# 4. Trình duyệt nhận phản hồi và hiển thị nội dung trang web cho người dùng. Trình duyệt có thể tiếp tục gửi các yêu cầu bổ sung để tải các tài nguyên khác như hình ảnh, CSS, và JavaScript.

# Câu 4: 
# HTML (HyperText Markup Language) là ngôn ngữ đánh dấu được sử dụng để tạo cấu trúc và nội dung cho trang web. Có thể nói là sườn của một trang web.
# CSS (Cascading Style Sheets) là ngôn ngữ dùng để mô tả cách trình bày và định dạng của các phần tử HTML trên trang web. Là thứ trang trí cho sườn của trang web.
# JavaScript là ngôn ngữ lập trình được sử dụng để tạo ra các tương tác động và các tính năng phức tạp trên trang web. Là thứ lập trình các cơ quan chức năng cho trang web, giúp no hoạt động.

# Câu 5: Cho đoạn mã HTML sau, hãy bổ sung CSS để làm cho đoạn văn có màu đỏ và in đậm:
# <p class="highlight" color="red" font-weight="bold">Chào mừng bạn đến với bài kiểm tra!</p>

# Câu 7: Hai loại phép nối (join) được sử dụng để kết hợp các hàng từ hai bảng dựa trên một điều kiện:
# INNER JOIN chỉ trả về các hàng có sự tương ứng trong cả hai bảng.
# LEFT JOIN trả về tất cả các hàng từ bảng bên trái, và các hàng tương ứng từ bảng bên phải. Nếu không có sự tương ứng, các cột từ bảng bên phải sẽ chứa giá trị NULL.

# Câu 8: 
# SQL (Structured Query Language) là ngôn ngữ truy vấn có cấu trúc được sử dụng để quản lý và thao tác cơ sở dữ liệu quan hệ.

# Truy vấn SQL để lấy tất cả khách hàng có tổng chi tiêu trên 10 triệu từ bảng orders:
#SELECT customer_id
#FROM orders
#GROUP BY customer_id
#HAVING SUM(total_amount) > 10000000;

# Câu 9: 
# Thư viện Pandas trong Python được sử dụng để thao tác và phân tích dữ liệu. Nó cung cấp các cấu trúc dữ liệu và hàm thao tác mạnh mẽ để làm việc với dữ liệu có nhãn hoặc dữ liệu bảng.

# Đọc file CSV vào DataFrame:
# import pandas as pd
# df = pd.read_csv('path_to_your_file.csv')

# Hiển thị 5 dòng đầu tiên của DataFrame:
# print(df.head())

# Câu 10: 
# Supervised Learning (Học có giám sát) và Unsupervised Learning (Học không giám sát) là hai phương pháp chính trong Machine Learning:

# Supervised Learning:
# - Dữ liệu huấn luyện bao gồm các cặp đầu vào-đầu ra (input-output pairs), trong đó đầu ra là nhãn (label) hoặc giá trị mục tiêu (target value).
# - Mục tiêu là học một hàm ánh xạ từ đầu vào đến đầu ra dựa trên các cặp dữ liệu huấn luyện.
# - Các thuật toán phổ biến: Linear Regression, Logistic Regression, Support Vector Machines, Neural Networks, Decision Trees, Random Forests.
# - Ứng dụng: Dự đoán giá nhà, phân loại email spam, nhận dạng hình ảnh, dự đoán bệnh tật.

# Unsupervised Learning:
# - Dữ liệu huấn luyện chỉ bao gồm đầu vào (input data) mà không có nhãn hoặc giá trị mục tiêu.
# - Mục tiêu là tìm ra cấu trúc ẩn hoặc mẫu (patterns) trong dữ liệu.
# - Các thuật toán phổ biến: K-means Clustering, Hierarchical Clustering, Principal Component Analysis (PCA), Anomaly Detection.
# - Ứng dụng: Phân cụm khách hàng, giảm chiều dữ liệu, phát hiện bất thường, phân tích thị trường.

# Tóm lại, sự khác biệt chính giữa Supervised Learning và Unsupervised Learning là ở việc có hay không có nhãn trong dữ liệu huấn luyện và mục tiêu của quá trình học.

# Câu 11: Quy trình chuẩn bị dữ liệu trước khi phân tích trong một dự án Data Analysis bao gồm các bước sau:

# I. Thu thập dữ liệu: Thu thập dữ liệu từ các nguồn khác nhau như cơ sở dữ liệu, file CSV, API, web scraping, v.v.
# II. Khám phá dữ liệu: Sử dụng các phương pháp thống kê và trực quan hóa để hiểu cấu trúc, phân phối và các đặc điểm chính của dữ liệu.
# III. Làm sạch dữ liệu: Xử lý các giá trị thiếu, loại bỏ các giá trị ngoại lệ, sửa chữa các lỗi trong dữ liệu, và chuẩn hóa dữ liệu.
# IV. Biến đổi dữ liệu: Chuyển đổi dữ liệu về định dạng phù hợp cho phân tích, bao gồm việc mã hóa các biến phân loại, tạo các biến mới, và chuẩn hóa hoặc chuẩn hóa dữ liệu.
# V. Tích hợp dữ liệu: Kết hợp dữ liệu từ các nguồn khác nhau để tạo ra một tập dữ liệu thống nhất.
# VI. Giảm chiều dữ liệu: Sử dụng các kỹ thuật như PCA để giảm số lượng biến đầu vào, giúp tăng hiệu quả và độ chính xác của mô hình phân tích.
# VII. Chia tách dữ liệu: Chia dữ liệu thành các tập huấn luyện và kiểm tra để đánh giá hiệu suất của mô hình phân tích.
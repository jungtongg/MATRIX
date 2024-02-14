'''Lê Ngọc Hà 20216922'''

class Matrix:
    
    # 1. Hàm khởi tạo lớp matrix
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[0] * cols for _ in range(rows)]

    
    # 2. Hàm hiển thị ma trận dưới dạng chuỗi
    def __str__(self):
        output = "\n"
        for row in self.data:
            for element in row:
                output += f'{format(round(element, 9), "> 15")}'
            output += '\n'
        return output
       

    # 3. Nhập ma trận từ bàn phím
    def input_from_user(self):

        # Xử lý lỗi trong việc nhập số hàng và số cột
        while True:
            try:
                if (self.rows <= 0) or (self.cols <= 0):
                    print("Số hàng và số cột phải là số nguyên dương. Vui lòng nhập lại.")
                    return None
                else:
                    break
            except ValueError:
                print("Giá trị không hợp lệ: các giá trị phải là số nguyên. Vui lòng nhập lại.")
        
        # Nhập giá trị cho ma trận từ người dùng
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                while True:
                    try:
                        value = float(input(f"Nhập giá trị [{i + 1}][{j + 1}]: "))
                        break
                    except ValueError:
                        print("Giá trị không hợp lệ: các giá trị phải là số nguyên hoặc số thực. Vui lòng nhập lại.")
                row.append(value)
            self.data[i] = row


    # 4. Nhập ma trận từ tệp tin
    def input_from_file(self, filename):
        try:
            with open(filename) as f:
                count = 0

                for line in f:
                    if count == 0:
                        # Đọc dòng đầu tiên của tệp để lấy số hàng và số cột
                        size = line.strip().split()
                        if (len(size) != 2) or not (size[0].isdigit()) or not (size[1].isdigit()):
                            raise ValueError("Dòng đầu tiên của file chỉ chứa hai giá trị nguyên dương (số hàng, số cột) và cách nhau bởi khoảng trắng.")
                        self.rows = int(size[0])
                        self.cols = int(size[1])
                        self.data = [[0] * self.cols for _ in range(self.rows)]
                    else:
                        # Đọc dữ liệu của ma trận từ các dòng tiếp theo trong tệp
                        values = line.strip().split()
                        if (len(values) != self.cols):
                            raise ValueError("Số lượng giá trị không tương ứng với số cột của ma trận.")
                        try:
                            row = [float(value) for value in values]
                        except ValueError:
                            raise ValueError("Không thể chuyển đổi giá trị sang số thực.")
                        self.data[count - 1] = row
                    count += 1

            if count - 1 != self.rows:
                raise ValueError("Số lượng dòng dữ liệu trong file không tương ứng với số hàng của ma trận.")                     
        except FileNotFoundError:
            raise FileNotFoundError("Tệp tin không tồn tại, vui lòng kiểm tra lại.")

    
    # 5. Hàm xuất kết quả ra file
    def output_to_file(self, output_filename, output):
        with open(output_filename, "a", encoding="utf-8") as f:
            lines = output.split('\n')
            for line in lines:
                f.write(line + '\n')
        print("Kết quả đã được lưu vào file:", output_filename)


    # 6. Hàm tính tổng hai ma trận
    def addition(self, other):
        if (self.rows != other.rows) or (self.cols != other.cols):
            raise ValueError("Hai ma trận không có kích thước giống nhau.")
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[i][j] = self.data[i][j] + other.data[i][j]
        return result


    # 7. Hàm tính hiệu hai ma trận
    def subtraction(self, other):
        if (self.rows != other.rows) or (self.cols != other.cols):
            raise ValueError("Hai ma trận không có kích thước giống nhau.")
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[i][j] = self.data[i][j] - other.data[i][j]
        return result


    # 8. Hàm tính tích hai ma trận
    def multiply(self, other):
        if self.cols != other.rows:
            raise ValueError("Số cột của ma trận A không bằng số hàng của ma trận B.")
        result = Matrix(self.rows, other.cols)
        for i in range(self.rows):
            for j in range(other.cols):
                total = 0
                for k in range(self.cols):
                    total += self.data[i][k] * other.data[k][j]
                result.data[i][j] = total
        return result


    # 9. Hàm tính tích ma trận với một số
    def multiply_by_number(self, number: float):
        if not isinstance(number, float):
            raise ValueError("Số nhập vào không hợp lệ. Vui lòng nhập một số nguyên hoặc số thực.")
        for i in range(self.rows):
            for j in range(self.cols):
                self.data[i][j] *= number
        return self

 
    # 10. Phương pháp Gauss
    def gauss(self):
        if (self.rows == 0) or (self.cols == 0) or (len(self.data) != self.rows) or (any(len(row) != self.cols for row in self.data)):
            raise ValueError("Kích thước ma trận không tương thích với dữ liệu.")
        
        m = self.rows
        n = self.cols
        rank = min(m, n)
        A = self.data
        eps = 1e-15

        # Tìm phần tử có giá trị tuyệt đối lớn nhất
        for i in range(rank):
            max_row = i
            for j in range(i + 1, m):
                if abs(A[j][i]) > abs(A[max_row][i]):
                    max_row = j
            # Kiểm tra phần tử đường chéo chính
            if abs(A[i][i]) < eps:
                for k in range(i + 1, m):
                    # Kiểm tra phần tử dưới đường chéo chính
                    if abs(A[k][i]) > eps:
                        A[i], A[k] = A[k], A[i]
                        break
                    else:
                        rank -= 1
                        continue

            # Chuẩn hóa các hàng
            for j in range(i + 1, m):
                factor = A[j][i] / A[i][i]
                for k in range(i + 1, n):
                    A[j][k] -= factor * A[i][k]

        return rank


    # 11. Hàm tính định thức ma trận
    def calculate_determinant(self):
        if self.rows != self.cols:
            raise ValueError("Ma trận không phải ma trận vuông")
        if (self.rows == 0) or (self.cols == 0):
            return "Ma trận rỗng"
        n = self.rows
        det = 1
        rank = self.gauss()
        if rank < n:
            return "Định thức bằng 0" 
        for i in range(rank):
            det *= self.data[i][i]
        return det
  

    # 12. Hàm tính hạng ma trận
    def calculate_rank(self):
        if (self.rows == 0) or (self.cols == 0):
            return 0
        return self.gauss()


    # 13. Hàm tính ma trận nghịch đảo
    @staticmethod
    def from_list(data: list):
        m = Matrix(len(data), len(data[0]))
        m.data = data
        return m
    
    # Tìm ma trận nghịch đảo bằng phương pháp Gauss Jordan
    def calculate_inverse(self):
        if self.rows != self.cols:
            raise ValueError("Ma trận không phải ma trận vuông")

        # Tạo ma trận đơn vị
        identity = [[0 for j in range(self.cols)] for i in range(self.rows)]
        for i in range(self.rows):
            identity[i][i] = 1

        A = self.data
        B = identity
        n = self.rows
        
        # Kiểm tra phần tử đường chéo chính
        for i in range(n):
            if A[i][i] == 0:
                for k in range(i + 1, n):
                    if A[k][i] != 0:
                        A[i], A[k] = A[k], A[i]
                        B[i], B[k] = B[k], B[i]
                        break
                else:
                    raise ValueError("Ma trận không thể nghịch đảo")

            # Chuẩn hóa hàng i để phần tử đường chéo chính bằng 1
            pivot = A[i][i]
            for j in range(n):
                A[i][j] /= pivot
                B[i][j] /= pivot

            # Đưa các phần tử dưới đường chéo chính về 0
            for k in range(n):
                if k == i:
                    continue
                factor = A[k][i]
                for j in range(n):
                    A[k][j] -= factor * A[i][j]
                    B[k][j] -= factor * B[i][j]

        return Matrix.from_list(B)


    # 14. Hàm tính ma trận chuyển vị
    def calculate_transpose(self):
        result = Matrix(self.cols, self.rows)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[j][i] = self.data[i][j]
        return result

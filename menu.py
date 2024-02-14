'''Lê Ngọc Hà 20216922'''

from matrix import Matrix
import copy

# Nhập ma trận A 
filename_a = input("Nhập tên tệp tin (filename.txt) cho ma trận A hoặc nhấn Enter để nhập từ bàn phím: ")
if filename_a:
    matrix_a = Matrix(1, 1)
    matrix_a.input_from_file(filename_a)
else:
    rows = int(input("Nhập số hàng của ma trận A: "))
    cols = int(input("Nhập số cột của ma trận A: "))
    matrix_a = Matrix(rows, cols)
    matrix_a.input_from_user()
print("Ma trận A là:")
print(matrix_a)

output_filename = "output.txt"
matrix_a.output_to_file(output_filename, f"Ma trận A là:\n {str(matrix_a)}")

while True:
    print("Menu: ")
    print("1. Cộng hai ma trận")
    print("2. Hiệu hai ma trận")
    print("3. Nhân hai ma trận")
    print("4. Nhân một số với ma trận")
    print("5. Tính định thức của ma trận")
    print("6. Tính hạng của ma trận")
    print("7. Tính ma trận nghịch đảo")
    print("8. Tính ma trận chuyển vị")
    print("9. Thoát khỏi chương trình")
    choice = input("\n" + "Vui lòng chọn: ")

    if choice in ['1', '2', '3']:

        # Nhập ma trận B
        filename_b = input("Nhập tên tệp tin (filename.txt) cho ma trận B hoặc nhấn Enter để nhập từ bàn phím: ")
        if filename_b:
            matrix_b = Matrix(1, 1)
            matrix_b.input_from_file(filename_b)
        else:
            rows = int(input("Nhập số hàng của ma trận B: "))
            cols = int(input("Nhập số cột của ma trận B: "))
            matrix_b = Matrix(rows, cols)
            matrix_b.input_from_user()
        print("Ma trận B là: ")
        print(matrix_b)
        matrix_b.output_to_file(output_filename, f"Ma trận B là:\n {str(matrix_b)}")

        #Tạo bản sao của ma trận A
        matrix_a_copy = copy.deepcopy(matrix_a)

        if choice == '1':
            matrix_sum = matrix_a_copy.addition(matrix_b)
            print("Tổng hai ma trận là: ")
            print(matrix_sum)
            matrix_sum.output_to_file(output_filename, f"Tổng hai ma trận là:\n {str(matrix_sum)}")

        elif choice == '2':
            matrix_sub = matrix_a_copy.subtraction(matrix_b)
            print("Hiệu hai ma trận là: ")
            print(matrix_sub)
            matrix_sub.output_to_file(output_filename, f"Hiệu hai ma trận là: \n {matrix_sub}")

        else:
            matrix_mul = matrix_a_copy.multiply(matrix_b)
            print("Tích hai ma trận là: ")
            print(matrix_mul)
            matrix_mul.output_to_file(output_filename, f"Tích hai ma trận là: \n {matrix_mul}")

    elif choice == '4':
        matrix_a_copy = copy.deepcopy(matrix_a)
        number = float(input("Nhập số muốn nhân với ma trận: "))
        mul_by_number = matrix_a_copy.multiply_by_number(number)
        print("Tích của ma trận với một số là: ")
        print(mul_by_number)
        mul_by_number.output_to_file(output_filename, f"Tích của ma trận với một số là: \n {mul_by_number}")

    elif choice == '5':
        matrix_a_copy = copy.deepcopy(matrix_a)
        det = matrix_a_copy.calculate_determinant()
        print("Định thức của ma trận đã nhập là: ")
        print(det)
        matrix_a_copy.output_to_file(output_filename, f"Định thức của ma trận đã nhập là: {det} \n")

    elif choice == '6':
        matrix_a_copy = copy.deepcopy(matrix_a)
        rank = matrix_a_copy.calculate_rank()
        print("Hạng của ma trận đã nhập là: ")
        print(rank)
        matrix_a_copy.output_to_file(output_filename, f"Hạng của ma trận đã nhập là: {rank} \n" )

    elif choice == '7':
        matrix_a_copy = copy.deepcopy(matrix_a)
        inverse = matrix_a_copy.calculate_inverse()
        print("Ma trận nghịch đảo của ma trận đã nhập là: ")
        print(inverse)
        if inverse is not None:   
            inverse.output_to_file(output_filename, f"Ma trận nghịch đảo của ma trận đã nhập là: \n {inverse}")
        else:
            print("Ma trận không thể nghịch đảo.")
        
    elif choice == '8':
        matrix_a_copy = copy.deepcopy(matrix_a)
        transpose = matrix_a_copy.calculate_transpose()
        print("Ma trận chuyển vị của ma trận đã nhập là: ")
        print(transpose)
        transpose.output_to_file(output_filename, f"Ma trận chuyển vị của ma trận đã nhập là: \n {transpose}")

    elif choice == '9':
        print("Bạn đã thoát khỏi chương trình.")
        break

    else:
        print("Lựa chọn không hợp lệ, vui lòng chọn lại.")
        print()
        continue
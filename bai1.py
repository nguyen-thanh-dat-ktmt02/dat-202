import tkinter as tk
import numpy as np

def create_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            entry = tk.Entry(matrix_frame, width=5)
            entry.grid(row=i, column=j, padx=5, pady=5)
            row.append(entry)
        matrix.append(row)
    return matrix

def submit_dimensions():
    global matrix_entries
    matrix_entries = None  # Đặt giá trị ban đầu cho biến global
    try:
        rows = int(rows_entry.get())
        cols = int(cols_entry.get())

        # Xóa ma trận hiện tại nếu có
        if matrix_entries:
            for row in matrix_entries:
                for entry in row:
                    entry.destroy()

        # Tạo ma trận mới dựa trên số dòng và số cột
        matrix_entries = create_matrix(rows, cols)

        # Hiển thị ma trận
        submit_button.grid(row=rows+1, column=0, columnspan=cols)
    except ValueError:
        # Xử lý ngoại lệ nếu người dùng nhập không phải là số
        pass

def get_matrix_values():
    values = []
    for row in matrix_entries:
        row_values = []
        for entry in row:
            row_values.append(float(entry.get()))
        values.append(row_values)
    return values

def solve(coefficients, constants):
    try:
        # Chuyển đổi ma trận hệ số thành ma trận đường chéo
        augmented_matrix = np.column_stack((coefficients, constants))
        row_echelon_form, pivot_columns = rref(augmented_matrix)

        # Kiểm tra số lượng hàng có giá trị khác không
        non_zero_rows = np.where(row_echelon_form[:, :-1].any(axis=1))[0]
        if len(non_zero_rows) < len(pivot_columns):
            return "Hệ phương trình có vô số nghiệm"

        # Trích xuất ma trận hệ số sau khi chuyển về dạng rút gọn
        reduced_coefficients = row_echelon_form[:, :-1]

        # Giải hệ phương trình
        solutions = np.zeros(reduced_coefficients.shape[1])
        for i, pivot_column in enumerate(pivot_columns):
            solutions[pivot_column] = row_echelon_form[i, -1]

        return solutions
    except Exception as e:
        return str(e)
def rref(matrix):
    num_rows, num_cols = matrix.shape
    pivot_columns = []
    lead = 0

    for r in range(num_rows):
        if lead >= num_cols:
            break

        i = r
        while matrix[i, lead] == 0:
            i += 1
            if i == num_rows:
                i = r
                lead += 1
                if num_cols == lead:
                    break

        # Swap i-th and r-th rows
        matrix[[i, r]] = matrix[[r, i]]

        # Scale to make the pivot 1
        pivot = matrix[r, lead]
        if pivot != 0:
            matrix[r] = matrix[r] / pivot

        # Eliminate other rows
        for i in range(num_rows):
            if i != r:
                factor = matrix[i, lead]
                matrix[i] = matrix[i] - factor * matrix[r]

        pivot_columns.append(lead)
        lead += 1

    return matrix, pivot_columns
def solve_linear_equations():
    coefficients = get_matrix_values()
    constants = get_matrix_values()[0]
    solutions = solve(coefficients, constants)
    result_label.config(text=solutions)

# Tạo cửa sổ tkinter
window = tk.Tk()
window.title("Linear Equation Solver")

# Khởi tạo biến số dòng và số cột
rows_entry = tk.Entry(window)
cols_entry = tk.Entry(window)
matrix_entries = None

# Tạo widget Entry và Label cho số dòng và số cột
rows_label = tk.Label(window, text="Số dòng:")
cols_label = tk.Label(window, text="Số cột:")
rows_label.grid(row=0, column=0, padx=10, pady=10)
rows_entry.grid(row=0, column=1, padx=10, pady=10)
cols_label.grid(row=1, column=0, padx=10, pady=10)
cols_entry.grid(row=1, column=1, padx=10, pady=10)

# Tạo nút nhấn để xác nhận số dòng và số cột
submit_button = tk.Button(window, text="Xác nhận", command=submit_dimensions)
submit_button.grid(row=2, column=0, columnspan=2, pady=10)

# Frame chứa ma trận
matrix_frame = tk.Frame(window)
matrix_frame.grid(row=3, column=0, columnspan=2)

# Nút nhấn để giải hệ phương trình
solve_button = tk.Button(window, text="Giải hệ phương trình", command=solve_linear_equations)
solve_button.grid(row=4, column=0, columnspan=2, pady=10)

# Label để hiển thị kết quả
result_label = tk.Label(window, text="")
result_label.grid(row=5, column=0, columnspan=2, pady=10)

# Mở cửa sổ
window.mainloop()

# Bài 1
def permutations(nums):
    """
    Tìm tất cả hoán vị của nums
    """
    result = []

    def backtrack(path, remaining):
        # Base case: Đã chọn đủ n số
        if len(path) == len(nums):
            result.append(path.copy()) # QUAN TRỌNG: phải copy!
            return  # SỬA Ở ĐÂY: Thụt lề vào TRONG lệnh if

        # Thử từng số còn lại
        # SỬA Ở ĐÂY: Toàn bộ vòng lặp này phải thụt lề vào TRONG hàm backtrack
        for i in range(len(remaining)):
            # CHOOSE: Chọn remaining[i]
            path.append(remaining[i])

            # EXPLORE: Đệ quy với các số còn lại (bỏ số vừa chọn)
            new_remaining = remaining[:i] + remaining[i+1:]
            backtrack(path, new_remaining)

            # UNCHOOSE: Quay lui
            path.pop()

    # Gọi hàm đệ quy lần đầu tiên
    backtrack([], nums)
    return result

# Test
print("=== Test Permutations ===")
result1 = permutations([1, 2, 3])
print(f"Hoán vị của [1,2,3]: {result1}")
print(f"Số hoán vị: {len(result1)}") # Kỳ vọng: 6 (= 3!)

result2 = permutations([1, 2])
print(f"\nHoán vị của [1,2]: {result2}")
print(f"Số hoán vị: {len(result2)}") # Kỳ vọng: 2 (= 2!)


def combinations(nums, k):
    """
    Tìm tất cả tổ hợp k phần tử từ nums
    """
    result = []

    def backtrack(start, path):
        # Base case: Đã chọn đủ k phần tử
        if len(path) == k:
            result.append(path.copy())
            return

        # Thử các số từ vị trí start trở đi
        for i in range(start, len(nums)):
            # CHOOSE
            path.append(nums[i])
            
            # EXPLORE: Chỉ xét các số sau i (i+1)
            backtrack(i + 1, path)

            # UNCHOOSE: Quay lui
            path.pop()

    # Khởi chạy thuật toán với vị trí bắt đầu là 0 và danh sách rỗng
    backtrack(0, [])
    return result

# Test
print("\n=== Test Combinations ===")
result1 = combinations([1, 2, 3, 4], 2)
print(f"Tổ hợp 2 từ [1,2,3,4]: {result1}")
print(f"Số tổ hợp: {len(result1)}") # Kỳ vọng: 6 (C(4,2) = 6)

result2 = combinations([1, 2, 3], 2)
print(f"\nTổ hợp 2 từ [1,2,3]: {result2}")
print(f"Số tổ hợp: {len(result2)}") # Kỳ vọng: 3 (C(3,2) = 3)


def subsets(nums):
    """
    Tìm tất cả tập con của nums
    """
    result = []

    def backtrack(start, path):
        # Lưu tất cả tập con (không có điều kiện dừng cụ thể)
        result.append(path.copy())

        # Thử thêm các phần tử từ start
        for i in range(start, len(nums)):
            # CHOOSE
            path.append(nums[i])

            # EXPLORE
            backtrack(i + 1, path)

            # UNCHOOSE
            path.pop()

    backtrack(0, [])
    return result

# Test
print("\n=== Test Subsets ===")
result1 = subsets([1, 2, 3])
print(f"Tập con của [1,2,3]: {result1}")
print(f"Số tập con: {len(result1)}") # Kỳ vọng: 8 (= 2^3)

result2 = subsets([1, 2])
print(f"\nTập con của [1,2]: {result2}")
print(f"Số tập con: {len(result2)}") # Kỳ vọng: 4 (= 2^2)



def binary_strings(n):
    """
    Tìm tất cả chuỗi nhị phân độ dài n
    """
    result = []

    def backtrack(path):
        # Base case: Đủ n ký tự
        if len(path) == n:
            result.append(''.join(path))
            return  # CHÚ Ý: Lệnh return phải thụt vào trong lệnh if

        # Thử cả '0' và '1'
        for choice in ['0', '1']:
            # CHOOSE
            path.append(choice)

            # EXPLORE
            backtrack(path)

            # UNCHOOSE
            path.pop()

    backtrack([])
    return result

# Test
print("\n=== Test Binary Strings ===")
result1 = binary_strings(3)
print(f"Chuỗi nhị phân độ dài 3: {result1}")
print(f"Số chuỗi: {len(result1)}") # Kỳ vọng: 8 (= 2^3)

result2 = binary_strings(2)
print(f"\nChuỗi nhị phân độ dài 2: {result2}")
print(f"Số chuỗi: {len(result2)}") # Kỳ vọng: 4 (= 2^2)










# Bài 2

def is_safe(board, row, col, n):
    """
    Kiểm tra đặt quân hậu ở (row, col) có hợp lệ không
    board: list lưu cột của quân hậu ở mỗi hàng
    """
    # Kiểm tra tất cả các hàng trước đó
    for prev_row in range(row):
        prev_col = board[prev_row]
        # Kiểm tra cùng cột
        if prev_col == col:
            return False
        # Kiểm tra đường chéo
        if abs(prev_row - row) == abs(prev_col - col):
            return False
    return True

def print_board(solution, n):
    """
    In bàn cờ N×N với quân hậu
    """
    for row in range(n):
        line = ""
        for col in range(n):
            if solution[row] == col:
                line += "Q "
            else:
                line += ". "
        print(line)
    print()

def solve_n_queens(n):
    """
    Hàm chính giải bài toán N-Queens
    """
    board = [-1] * n
    
    def backtrack(row):
        if row == n:
            print_board(board, n)
            return

        for col in range(n):
            if is_safe(board, row, col, n):
                board[row] = col
                backtrack(row + 1)
                board[row] = -1 # Reset

    backtrack(0)

# Test với bàn cờ 4x4
print("=== Bàn cờ 4x4 ===")
solve_n_queens(4)

class Counter:
    """Class để đếm số lần gọi hàm"""
    def __init__(self):
        self.total_calls = 0
        self.solutions = 0

    def report(self):
        print(f"Tổng số lần gọi: {self.total_calls}")
        print(f"Số giải pháp tìm được: {self.solutions}")

def is_valid(board):
    """Kiểm tra xem cấu hình bàn cờ hiện tại có hợp lệ không"""
    n = len(board)
    for i in range(n):
        for j in range(i + 1, n):
            # Kiểm tra cùng cột hoặc cùng đường chéo
            if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                return False
    return True

def solve_n_queens_no_pruning(n):
    """
    N-Queens KHÔNG có pruning (kiểm tra sau)
    """
    counter = Counter()
    result = []
    board = []

    def backtrack(row):
        counter.total_calls += 1

        # Base case: Đã đặt đủ n quân hậu
        if row == n:
            if is_valid(board):
                result.append(board.copy())
                counter.solutions += 1
            return

        # Thử tất cả cột (0 đến n-1)
        for col in range(n):
            board.append(col)
            backtrack(row + 1)
            board.pop()

    backtrack(0)
    counter.report()
    return result

# Test với bàn cờ 4x4
print("=== Kết quả 4x4 (No Pruning) ===")
solve_n_queens_no_pruning(4)


def solve_n_queens_with_pruning(n):
    """
    N-Queens CÓ pruning (kiểm tra trước)
    """
    counter = Counter()
    result = []
    board = []

    def backtrack(row):
        counter.total_calls += 1

        # Base case
        if row == n:
            result.append(board.copy())
            counter.solutions += 1
            return

        # Thử từng cột
        for col in range(n):
            # PRUNING: Kiểm tra is_safe TRƯỚC khi đệ quy
            if is_safe(board, row, col, n):
                # CHOOSE
                board.append(col)

                # EXPLORE
                backtrack(row + 1)

                # UNCHOOSE
                board.pop()

    backtrack(0)
    counter.report()
    return result

# Test thử với 4x4
print("\n=== Kết quả 4x4 (Có Pruning) ===")
solve_n_queens_with_pruning(4)

import time

def compare_n_queens(n):
    print(f"\n{'='*50}")
    print(f"So sánh N-Queens với N={n}")
    print(f"{'='*50}")

    # 1. Test không có pruning
    print("\n[1] KHÔNG có pruning:")
    start = time.time()
    result1 = solve_n_queens_no_pruning(n)
    time1 = time.time() - start
    print(f"Thời gian chạy: {time1:.6f} giây")

    # 2. Test có pruning
    print("\n[2] CÓ pruning:")
    start = time.time()
    result2 = solve_n_queens_with_pruning(n)
    time2 = time.time() - start
    print(f"Thời gian chạy: {time2:.6f} giây")
    
    # 3. In kết quả so sánh
    if time2 > 0:
        print(f"\nTốc độ nhanh hơn: {time1/time2:.2f} lần")
    else:
        print("\nPruning quá nhanh, thời gian đo được gần bằng 0!")

    # In một giải pháp mẫu
    if len(result2) > 0:
        print(f"\nMột giải pháp mẫu cho {n}-Queens:")
        print_board(result2[0], n)

# Chạy thử
compare_n_queens(4)
compare_n_queens(6)










# Bài 3
import time
class Counter:
    """Class để đếm số lần gọi hàm đệ quy"""
    def __init__(self):
        self.calls = 0
def subset_sum_basic(nums, target, counter):
    """Subset Sum cơ bản (chỉ để so sánh)"""
    result = [] 
    def backtrack(start, path, current_sum):
        counter.calls += 1
        
        if current_sum == target:
            result.append(path.copy())
            return
            
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path, current_sum + nums[i])
            path.pop()
    backtrack(0, [], 0)
    return result
def subset_sum_pruned(nums, target, counter):
    """Subset Sum áp dụng 4 kỹ thuật tối ưu"""
    result = []
    nums.sort() 
    suffix_sums = [0] * len(nums)
    curr_sum = 0
    for i in range(len(nums) - 1, -1, -1):
        curr_sum += nums[i]
        suffix_sums[i] = curr_sum
    def backtrack(start, path, current_sum):
        counter.calls += 1
        if current_sum == target:
            result.append(path.copy())
            return
        if current_sum > target:
            return 
        for i in range(start, len(nums)):
 
            if i > start and nums[i] == nums[i-1]:
                continue
            if current_sum + nums[i] > target:
                break
            remaining_sum = suffix_sums[i] 
            if current_sum + remaining_sum < target:
                break 
            path.append(nums[i])
            backtrack(i + 1, path, current_sum + nums[i])
            path.pop()
    backtrack(0, [], 0)
    return result
def compare_subset_sum(nums, target):
    print(f"{'='*50}")
    print(f"SO SÁNH SUBSET SUM (Target = {target}, N = {len(nums)})")
    print(f"{'='*50}")
    counter_basic = Counter()
    start_time = time.time()
    res_basic = subset_sum_basic(nums, target, counter_basic)
    time_basic = time.time() - start_time
    counter_pruned = Counter()
    start_time = time.time()
    res_pruned = subset_sum_pruned(nums.copy(), target, counter_pruned)
    time_pruned = time.time() - start_time
    nhanh_cat_tia = counter_basic.calls - counter_pruned.calls
    ty_le_cat = (nhanh_cat_tia / counter_basic.calls) * 100 if counter_basic.calls > 0 else 0
    toc_do_tang = time_basic / time_pruned if time_pruned > 0 else float('inf')
    print("[1] BẢN CƠ BẢN (KHÔNG PRUNING):")
    print(f" - Tổng số lần gọi hàm: {counter_basic.calls:,}")
    print(f" - Thời gian chạy     : {time_basic:.6f} giây")
    print(f" - Số nghiệm tìm được : {len(res_basic):,}")
    print("\n[2] BẢN TỐI ƯU (CÓ 4 PRUNING):")
    print(f" - Tổng số lần gọi hàm: {counter_pruned.calls:,}")
    print(f" - Thời gian chạy     : {time_pruned:.6f} giây")
    print(f" - Số nghiệm tìm được : {len(res_pruned):,}")
    print("\n[3] BÁO CÁO HIỆU NĂNG:")
    print(f" - Số nhánh đã cắt tỉa: {nhanh_cat_tia:,}")
    print(f" - Tỷ lệ cắt (%)      : {ty_le_cat:.2f}%")
    print(f" - Tốc độ tăng (lần)  : {toc_do_tang:.2f}x nhanh hơn")
if __name__ == "__main__":
    test_nums = list(range(1, 20)) # [1, 2, ..., 19]
    test_target = 50
    compare_subset_sum(test_nums, test_target)
# Bài 1
#Hàm 1 – Tính tổng từ 1 đến n
def sum_to_n(n):
#Tính tổng 1 + 2 + ... + n bằng đệ quy
# Base case: n = 0 hoặc n = 1
    if n == 0:
        return 0
    if n == 1:
        return 1
# Recursive case: n + sum(1..n-1)
    return n + sum_to_n(n - 1)
print(sum_to_n(5)) 
print(sum_to_n(10)) 
# Độ phức tạp: O(n)
# Giải thích: Hàm gọi đệ quy n lần, mỗi lần thực hiện 1 phép cộng

#Hàm 2 – Tính n mũ k (power)
def power(n, k):
#Tính n^k bằng đệ quy
# Base case 1: mũ 0
    if k == 0:
        return 1

    # Base case 2: cơ số 0
    if n == 0:
        return 0

    # Recursive case: n × n^(k-1)
    return n * power(n, k - 1)
print(power(2, 5))
print(power(3, 4)) 
print(power(5, 0)) 
# Độ phức tạp: O(k)
# Giải thích: Hàm gọi đệ quy k lần

#Hàm 3 – Đảo chuỗi (reverse string)
def reverse_string(s):
#Đảo ngược chuỗi bằng đệ quy
# Base case: chuỗi rỗng hoặc 1 ký tự
    if len(s) <= 1:
        return s
    # Recursive case: đảo phần còn lại + ký tự đầu
    return reverse_string(s[1:]) + s[0]
print(reverse_string("hello")) # Kết quả: "olleh"
print(reverse_string("python")) # Kết quả: "nohtyp"
print(reverse_string("a")) # Kết quả: "a"
print(reverse_string("")) # Kết quả: ""
# Độ phức tạp: O(n)
# Giải thích: n lần gọi đệ quy với n = len(s)

#Hàm 4 – Kiểm tra palindrome (đọc xuôi ngược như nhau)
def is_palindrome(s):
#Kiểm tra chuỗi có phải palindrome bằng đệ quy
# Base case: chuỗi rỗng hoặc 1 ký tự
    if len(s) <= 1:
        return True
    # So sánh ký tự đầu và cuối
    if s[0] != s[-1]:
        return False
# Recursive case: kiểm tra phần giữa
    return is_palindrome(s[1:-1])
print(is_palindrome("racecar")) # True
print(is_palindrome("madam")) # True
print(is_palindrome("hello")) # False
print(is_palindrome("a")) # True
print(is_palindrome("")) # True
# Độ phức tạp: O(n)
# Giải thích: Tối đa n/2 lần so sánh, vẫn là O(n)








# Bài 2
def fibonacci_naive(n):
    """
    Fibonacci đệ quy đơn giản - CHẬM
    F(n) = F(n-1) + F(n-2)
    F(0) = 0, F(1) = 1
    """
    if n <= 1:
        return n
    return fibonacci_naive(n - 1) + fibonacci_naive(n - 2)

# Test
print("Fibonacci naive:")
print(fibonacci_naive(10)) # 55
print(fibonacci_naive(20)) # 6765 (chậm rồi)
# print(fibonacci_naive(35)) # Rất chậm! Mất vài giây
# Độ phức tạp: O(2^n) - rất chậm

def fibonacci_memo(n, memo=None):
    """
    Fibonacci với memoization - NHANH
    """
    # Khởi tạo memo nếu chưa có
    if memo is None:
        memo = {}
    # TODO: Kiểm tra n đã có trong memo chưa
    # Nếu có → trả về ngay memo[n]
    if n in memo:
        return memo[n]
    # TODO: Base case
    # Nếu n <= 1 → lưu vào memo và trả về
    if n <= 1:
        memo[n] = n
        return n
    # TODO: Recursive case
    # Tính fibonacci_memo(n-1) + fibonacci_memo(n-2)
    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]
# TODO: Recursive case
# Tính fibonacci_memo(n-1) + fibonacci_memo(n-2)
# Lưu kết quả vào memo[n]
# Trả về memo[n]

def fibonacci_memo(n, memo=None):
    if memo is None:
        memo = {}

    # Kiểm tra memo
    if n in memo:
        return memo[n]

    # Base case
    if n <= 1:
        memo[n] = n
    return memo[n]

# Recursive case: sinh viên tự viết
# memo[n] = ...
# return memo[n]

import time

# Test với n = 35
print("\n--- So sánh hiệu suất ---")

start = time.time()
result1 = fibonacci_naive(30) # Chỉ test n=30 vì 35 quá chậm
time1 = time.time() - start
print(f"Naive F(30) = {result1}, thời gian: {time1:.4f}s")

start = time.time()
result2 = fibonacci_memo(100) # Có thể test với 100!
time2 = time.time() - start
print(f"Memo F(100) = {result2}, thời gian: {time2:.6f}s")










# Bài 3
import time
import random

def merge_sort(arr):
    """
    Sắp xếp mảng bằng Merge Sort
    Độ phức tạp: O(n log n)
    """
# Base case: mảng 0 hoặc 1 phần tử
    if len(arr) <= 1:
        return arr

    # TODO: Divide - chia đôi mảng
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

# TODO: Conquer - đệ quy sắp xếp 2 nửa

    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)
    # TODO: Combine - trộn 2 nửa đã sắp xếp
    return merge(left_sorted, right_sorted)

def merge(left, right):
    """
    Trộn 2 mảng đã sắp xếp thành 1 mảng sắp xếp
    """
    result = []
    i = j = 0
# TODO: So sánh và chọn phần tử nhỏ hơn
# while i < len(left) and j < len(right):
# if left[i] <= right[j]:
# ...
# else:
# ...

# TODO: Thêm các phần tử còn lại
# result.extend(...)

    return result

# Test
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = merge_sort(arr)

print(f"Mảng sau khi sắp xếp: {sorted_arr}")
# Kết quả: [11, 12, 22, 25, 34, 64, 90]


# Tạo mảng ngẫu nhiên
arr_small = [random.randint(1, 1000) for _ in range(100)]
arr_large = [random.randint(1, 10000) for _ in range(5000)]

# Đo thời gian với mảng nhỏ
start = time.time()
sorted_small = merge_sort(arr_small.copy()) # hoặc quick_sort
time_small = time.time() - start
print(f"Thời gian sắp xếp 100 phần tử: {time_small:.6f}s")

# Đo thời gian với mảng lớn
start = time.time()
sorted_large = merge_sort(arr_large.copy())
time_large = time.time() - start
print(f"Thời gian sắp xếp 5000 phần tử: {time_large:.6f}s")

start = time.time()
sorted_builtin = sorted(arr_large)
time_builtin = time.time() - start
print(f"Thời gian Python sorted(): {time_builtin:.6f}s")
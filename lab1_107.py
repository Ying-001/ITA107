# Bài 1
def snippet_1(n):
    total = 0 
    for i in range(n): 
        total = total + 1
    return total
# Độ phức tạp: O(n)
# Giải thích: vòng for chạy n lần, mỗi lần chỉ có 1 phép gán/cộng.

def snippet_2(n):
    count = 0
    for i in range(n):
        for j in range(n):
            count += 1
    return count
# Độ phức tạp: O(n^2)
# Giải thích: có 2 vòng for lồng nhau, mỗi vòng chạy n lần → tổng n * n = n^2 bước.


def snippet_3(n):
    steps = 0
    while n > 0:
        n = n // 2
        steps += 1
    return steps
# Độ phức tạp: O(log n)
# Giải thích: mỗi vòng while chia n cho 2, nên số vòng ≈ số lần chia đôi n về 1 là log2(n).

def constant_work():
    x = 1
    y = 2
    z = x + y
    return z
def snippet_4(n):
    for i in range(n):
        constant_work()
# Độ phức tạp: O(n)
# Giải thích: vòng for chạy n lần, mỗi lần gọi hàm O(1), nên tổng thời gian tỉ lệ tuyến tính với n.









# Bài 2
def snippet_5(n):
    total = 0
    for i in range(n):
        for j in range(i):
            total += 1
    return total
# Độ phức tạp: O(n^2)
# Giải thích: vòng j chạy n lần , Khi i = 1 → chạy 1 lần, i = 2 → 2 lần, ..., i = n-1 → n-1 lần. Tổng số lần lặp là 0 + 1 + 2 + ... + (n-1) = n(n-1)/2.

def snippet_6(n):
    k = 1
    total = 0
    while k < n:
        for i in range(n):
            total += 1
            k = k * 2
    return total
# Độ phức tạp:O(n log n)
# Giải thích: vòng for bên trong chạy n lần , mỗi lần nhân k với 2 → số lần lặp của while

def snippet_7(arr):
    count = 0
    for x in arr:
        if x in arr: 
            count += 1
    return count
# Độ phức tạp:O(n^2)
# Giải thích:Vòng for chạy n lần , mỗi lần, phép x in arr phải duyệt cả list

def snippet_8(arr):
    s = set(arr)
    count = 0
    for x in arr:
        if x in s:
            count += 1
    return count
# Độ phức tạp:O(n)
# Giải thích: số phần tử = n → O(n) vòng for chạy n lần, mỗi lần x in s là O(1) trung bình, tổng thời gian: O(n) + n × O(1).







# Bài 3
def two_sum_quadratic(arr, target):
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == target:
                return (i, j)
    return None
# Độ phức tạp: O(n^2) 
# Giải thích: Thuật toán sử dụng 2 vòng lặp lồng nhau 

def two_sum_linear(arr, target):
    seen = {}
    for i in range(len(arr)):
        complement = target - arr[i]
        if complement in seen:
            return (seen[complement], i)
        seen[arr[i]] = i
    return None
# Độ phức tạp: O(n)
# Giải thích: Chỉ sử dụng một vòng lặp duy nhất chạy n lần.

import time
import random
arr = list(range(10000))
random.shuffle(arr)
target = arr[100] + arr[500]
start = time.time()
two_sum_quadratic(arr, target)
print(f"Thời gian O(n^2): {time.time() - start:.4f} giây")
start = time.time()
two_sum_linear(arr, target)
print(f"Thời gian O(n): {time.time() - start:.4f} giây")
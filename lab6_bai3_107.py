print("===== Kruskal dùng DSU Basic =====")

# =========================
# DSU Basic
# =========================
def make_set(vertices):
    return {v: v for v in vertices}

def find(parent, v):
    while parent[v] != v:
        v = parent[v]
    return v

def union(parent, a, b):
    root_a = find(parent, a)
    root_b = find(parent, b)

    if root_a != root_b:
        parent[root_b] = root_a


# =========================
# Kruskal Basic
# =========================
def kruskal_mst_basic(vertices, edges):
    edges_sorted = sorted(edges, key=lambda e: e[0])

    parent = make_set(vertices)

    mst = []
    total_weight = 0

    print("Cạnh sau khi sort:")
    for e in edges_sorted:
        print(e)

    print("\nDuyệt các cạnh:")

    for w, u, v in edges_sorted:
        root_u = find(parent, u)
        root_v = find(parent, v)

        print(
            f"Xét cạnh {u}-{v} (w={w}), "
            f"root_u={root_u}, root_v={root_v}"
        )

        if root_u != root_v:
            print(" -> CHỌN")
            mst.append((u, v, w))
            total_weight += w
            union(parent, u, v)
        else:
            print(" -> BỎ (tạo chu trình)")

        if len(mst) == len(vertices) - 1:
            break

    return mst, total_weight


print("\n===== Kruskal dùng DSU Optimized =====")

# =========================
# DSU Optimized
# =========================
def make_set_optimized(vertices):
    parent = {}
    size = {}

    for v in vertices:
        parent[v] = v
        size[v] = 1

    return parent, size


def find_optimized(parent, v):
    if parent[v] != v:
        parent[v] = find_optimized(parent, parent[v])  # Path Compression
    return parent[v]


def union_optimized(parent, size, a, b):
    root_a = find_optimized(parent, a)
    root_b = find_optimized(parent, b)

    if root_a == root_b:
        return

    # Union by Size
    if size[root_a] < size[root_b]:
        root_a, root_b = root_b, root_a

    parent[root_b] = root_a
    size[root_a] += size[root_b]


# =========================
# Kruskal Optimized
# =========================
def kruskal_mst_optimized(vertices, edges):
    edges_sorted = sorted(edges, key=lambda e: e[0])

    parent, size = make_set_optimized(vertices)

    mst = []
    total_weight = 0

    for w, u, v in edges_sorted:
        root_u = find_optimized(parent, u)
        root_v = find_optimized(parent, v)

        if root_u != root_v:
            mst.append((u, v, w))
            total_weight += w
            union_optimized(parent, size, u, v)

        if len(mst) == len(vertices) - 1:
            break

    return mst, total_weight


# =========================
# Test
# =========================
def test_kruskal():
    vertices = ['A', 'B', 'C', 'D', 'E']

    edges = [
        (1, 'A', 'B'),
        (4, 'A', 'C'),
        (3, 'B', 'C'),
        (2, 'B', 'D'),
        (2, 'D', 'E'),
        (5, 'C', 'E')
    ]

    print("\n=== Kruskal Basic ===")
    mst1, total1 = kruskal_mst_basic(vertices, edges)

    print("\nMST Basic:")
    for u, v, w in mst1:
        print(f"{u}-{v} (w={w})")

    print("Tổng trọng số:", total1)

    print("\n=== Kruskal Optimized ===")
    mst2, total2 = kruskal_mst_optimized(vertices, edges)

    print("\nMST Optimized:")
    for u, v, w in mst2:
        print(f"{u}-{v} (w={w})")

    print("Tổng trọng số:", total2)


if __name__ == "__main__":
    test_kruskal()
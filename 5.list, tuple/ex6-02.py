# korea, 365, 400 값 출력
a = [100, 3.14, "korea", [1, 2, 3, 365], (100, 200, 300, 400, 500)]

print(a[2], a[3][3], a[4][3])

# 역인덱스
# 정방향 순서는 0, 1, 2,...
# 역인덱스는 오른쪽에서 왼쪽으로 ...,-3, -2, -1
a = [100, 200, 300, 400, 500]
print(a[::-1])

# 인덱스와 값 출력
a = [1, 2, 3, 4, 5, [1, 2, 3], (4, 5, 6)]
index = 0
for x in a:
    print(index, "=", x, end="\t")
    index += 1
so_phan_tu = int(input("Nhập số phần tử có trong mảng: "))
list = []
for i in range(so_phan_tu):
    data_input = int(input(f"Phần tử thứ {i + 1} là:"))
    list.append(data_input)
print("Mảng sau khi sắp xếp là:", sorted(list))
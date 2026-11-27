# Tạo danh sách chứa các số thỏa mãn điều kiện
ket_qua = []

for i in range(2000, 3201):
    if (i % 7 == 0) and (i % 5 != 0):
        ket_qua.append(str(i))

# In các số tìm được trên một dòng, ngăn cách bởi dấu phẩy
print(",".join(ket_qua))
def XoaPhanTu(dictionary, key):
    if key in dictionary:
        del dictionary[key]
        return True
    else:
        return False
my_dict = {'a' : 1, 'b' : 3, 'c' : 5}
print("Moi nhap key: ")
Key = input()
KQ = XoaPhanTu(my_dict, Key)
if KQ:
    print("Phan tu da duoc xoa", my_dict)
else:
    print("Khong tim thay phan tu do")
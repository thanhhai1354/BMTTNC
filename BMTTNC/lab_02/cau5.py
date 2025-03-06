def count(List):
    count_dict = {}
    for item in List:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    return count_dict

inputList = input("Nhap danh sach: ")
wordList = inputList.split()
XuatHien = count(wordList)
print("So lan xuat hien cua cac phan tu: ", XuatHien)
        
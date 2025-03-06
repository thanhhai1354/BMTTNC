def daonguoc(List):
    return List[:: -1]
inputList = input("Nhap danh sach: ")
nums = list(map(int, inputList.split(',')))
listdaonguoc = daonguoc(nums)
print("Ket qua: ", listdaonguoc)
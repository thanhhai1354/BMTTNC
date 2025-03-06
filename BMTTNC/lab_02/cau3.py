def Tuple(List):
    return tuple(List)

inputList = input("Nhap danh sach: ")
nums = list(map(int, inputList.split(',')))

MyTuple = Tuple(nums)
print("List: ", nums)
print("Tuple: ", MyTuple)
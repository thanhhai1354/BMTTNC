def tongchan(List):
    sum = 0
    for num in List:
        if num % 2 == 0:
            sum += num
    return sum
inputList = input("Nhap so: ")
nums = list(map(int, inputList.split(',')))
tong = tongchan(nums)
print("Tong cac so chan trong list: ", tong)
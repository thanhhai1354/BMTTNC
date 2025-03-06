def Find(tuple_dta):
    first = tuple_dta[0]
    last = tuple_dta[-1]
    return first, last
inputList = eval(input("Nhap tuple: "))
first, last = Find(inputList)

print("Ptu dau tien: ", first)
print("Ptu cuoi cung: ", last)
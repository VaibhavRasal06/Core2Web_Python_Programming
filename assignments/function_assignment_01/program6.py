def parent():
    def myIndex(listData, searchEle):
        if searchEle in listData:
            return listData.index(searchEle)
        else:
            return -1

    def myPalindrome(Num):
        return str(Num) == str(Num)[::-1]

    choice = int(input("Enter your choice (1 for myIndex, 2 for myPalindrome): "))

    if choice == 1:
        listData = [1, 2, 3, 4, 5, 6]
        searchEle = int(input("Enter the element to search: "))
        result = myIndex(listData, searchEle)
        print(result)
    elif choice == 2:
        Num = int(input("Enter a number: "))
        result = myPalindrome(Num)
        print(result)
    else:
        print("Invalid input")

parent()

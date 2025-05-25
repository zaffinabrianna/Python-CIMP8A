# List Program
# Brianna Zaffina
# 11/20/2023

MY_NAME = "Brianna Zaffina"

def main():
    print("List Program -", MY_NAME)
    print()

    list = []
    total = 0

    for i in range(0, 10):
       num = (int(input("Enter an Integer: ")))
       total = total + num
       list.insert(i, num)

    print()
    print("This is the list of integers entered:", list)

    smallestNum = min(list)
    highestNum = max(list)

    print("This is the lowest integer:", smallestNum)
    print("This is the highest integer:", highestNum)
    print("This is the total of all the integers:", total)

    avg = total / 10

    print("This is the average of all the integers:", avg)
    list.sort()
    print("This is the integers list sorted in ascending sequence:", list)
    list.reverse()
    print("This is the integers list sorted in descending sequence:", list)

main()
       

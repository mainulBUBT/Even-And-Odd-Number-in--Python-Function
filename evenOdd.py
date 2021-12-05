def evenOdd(number):
    if number%2 == 0:
        print(number," is Even")
    else:
        print(number," is Odd")


givenNumber = int(input("Enter a Number to check even or odd: "))
evenOdd(givenNumber)
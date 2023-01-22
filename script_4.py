def int_input():
    count = 1
    sum = 0
    i = True
    while i:
        try:
            for x in range(5):
                if count != 6:
                    print("enter number #", count)
                    temp_int = int(input())
                    sum += temp_int
                    count += 1
                else:
                    return sum

        except ValueError:
            print("that is not a number")
            count = 1
            sum = 0
            i = True
            

print(int_input())


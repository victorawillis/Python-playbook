# allow user to repeatedly perform calculation
option = 'y'
while (option == 'y'):
    
    # get filename
    print("Enter the name of the file")

    while (True):
        filename = input()
        try:
            file = open(filename)


        except IOError:
            print("Error: file could not be opened. Enter a valid filename:")
            continue

        else:
            break

    # perform duties to file
    num_list = file.readlines()
    num_list = list(map(int, num_list))
    length = len(num_list)
    file.close()

    # sum
    number_sum = 0
    for i in range(len(num_list)):
        number_sum += num_list[i]

    # count
    count = len(num_list)

    # average
    average = number_sum / length

    # maxium
    maximum = max(num_list)

    # minimum
    minimum = min(num_list)

    # range
    number_range = maximum - minimum

    # display results
    print("File name:", filename)
    print("Sum:", number_sum)
    print("Count:", count)
    print("Average:", average)
    print("Maximum:", maximum)
    print("Minimum:", minimum)
    print("Range:", number_range)

    print("Would you like to evaluate another file?")
    option = input()

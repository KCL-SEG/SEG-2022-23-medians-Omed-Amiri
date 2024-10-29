def median(*args):
    count = 0
    numbers = list(args)
    numbers.sort()
    for value in numbers:
        count += 1
    if count%2==1:
        return numbers[count//2]
    elif count%2==0:
        no1 = count//2
        no2 = count//2 - 1
        average = (numbers[no1] + numbers[no2])/2
        return average 

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
print(f'the median of these numbers is {median(*numbers)}')

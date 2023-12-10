
def calculate_statistics(numbers):
    count = len(numbers)
    total = sum(numbers)
    mean = total/count if count > 0 else 0
    sorted_numbers = sorted(numbers)
    if count % 2 == 0:
        median = (sorted_numbers[count // 2 - 1] + sorted_numbers [count // 2 - 1]) / 2
    else:
        median = sorted_numbers[count // 2 ]
    minimum = min(numbers) if count > 0 else 0
    maximum = max(numbers) if count > 0 else 0
    print ("Total count:", count)
    print("Sum:", total)
    print("Mean (Average):", mean)
    print("Median:", median)
    print("Minimum:", minimum)
    print("Maximum:", maximum)

numbers_list = [7, 12, 5, 21, 8, 10, 15]
calculate_statistics(numbers_list)
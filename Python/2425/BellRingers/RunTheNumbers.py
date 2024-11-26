import statistics

numbers = []

for i in range(5):
    numbers.append(float(input("Enter a number: ")))

print(numbers)

print(f"Total of the numbers:              {sum(numbers)}")
print(f"Minimum of the numbers:            {min(numbers)}")
print(f"Maximum of the numbers:            {max(numbers)}")
print(f"Average of the numbers:            {sum(numbers) / len(numbers)}")
print(f"Mode of the numbers:               {statistics.mode(numbers)}")
print(f"Standard deviation of the numbers: {statistics.pstdev(numbers)}")
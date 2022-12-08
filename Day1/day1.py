sums = []
temp_sum = 0

with open("day1.txt", "r") as f:
    for line in f:
        if line == "\n":
            sums.append(temp_sum)
            temp_sum = 0
            continue
        temp_sum += int(line)
sums.sort()

print(sum(sums[-3:]))

for i in range(10000):
    print("Jan ist ein Nuttn")
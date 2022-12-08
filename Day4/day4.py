
def solve_part_one():
    count = 0
    with open("day4.txt", "r") as f:
        for line in f:
            first_pair = line.split(",")[0].split("-")
            second_pair = line.split(",")[1].replace("\n", "").split("-")
            if (int(first_pair[0]) >= int(second_pair[0]) and int(first_pair[1]) <= int(second_pair[1])) or (int(second_pair[0]) >= int(first_pair[0]) and int(second_pair[1]) <= int(first_pair[1])):
                count += 1
                # with open("output.txt", "a") as f:
                #     f.write(f"first pair: {first_pair}, second pair: {second_pair}\n")
                #     f.write(f"first pair one: {first_pair[0]}, first pair two: {first_pair[1]}, second pair one: {second_pair[0]}, second pair two: {second_pair[1]}\n")
    print(count)


def solve_part_two():
    count = 0
    with open("day4.txt", "r") as f:
        for line in f:
            first_pair = line.split(",")[0].split("-")
            second_pair = line.split(",")[1].replace("\n", "").split("-")
            first_pair_numbers = [number for number in range(int(first_pair[0]), int(first_pair[1])+1)]
            second_pair_numbers = [number for number in range(int(second_pair[0]), int(second_pair[1])+1)]
            for number in first_pair_numbers:
                if number in second_pair_numbers:
                    count += 1
                    break

        print(count)


solve_part_two()
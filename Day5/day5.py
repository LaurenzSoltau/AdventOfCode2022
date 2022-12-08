
# TODO input einlesen und in 2d Array speichern
# erste Zeile gibt Anzahl der Spalten und speichert in jeder spalte die dazugehörige Kiste
# Bis nur noch Zahlen in der Zeile sind, alle Kisten in die richtige Liste inserten


# TODO jede Anweisung nacheinander ausführen
# von wo und wie viele speichern
# solange aus einer liste removen und appenden bis anweisung erfüllt ist
# für alle Anweisungen wiederholen


# TODO ergebnis ablesen
# alle letzen einträge in der Liste ablesen


def solve_part_one():
    matrix = []

    raw_input = []
    input = []
    with open("day5.txt", "r") as f:
        raw_input = f.readlines()
    for item in raw_input:
        input.append(item.replace("\n", ""))

    # create matrix
    for i in range(3, len(input[0])+1, 4):
        matrix.append([])

    # fill matrix
    for line in input:
        # stop when input is over
        if line.replace(" ", "").isdigit():
            break
        for i in range(3, len(line)+1, 4):
            if line[i-3:i] != "   ":
                matrix[int(-0.75 + i*0.25)].insert(0, line[i-3:i])

    for line in input:
        if line[:4] == "move":
            instruction = [word for word in line.split()]
            amount = int(instruction[1])
            from_stack = int(instruction[3]) - 1
            to_stack = int(instruction[5]) - 1
            for _ in range(amount):
                matrix[to_stack].append(matrix[from_stack][-1])
                del matrix[from_stack][-1]
    answer_list = []

    for list in matrix:
        answer_list.append(list[-1])

    answer_string = "".join(answer_list).replace("[", "").replace("]", "")
    print(answer_string)


def solve_part_two():
    matrix = []

    raw_input = []
    input = []
    with open("day5.txt", "r") as f:
        raw_input = f.readlines()
    for item in raw_input:
        input.append(item.replace("\n", ""))

    # create matrix
    for i in range(3, len(input[0])+1, 4):
        matrix.append([])

    # fill matrix
    for line in input:
        # stop when input is over
        if line.replace(" ", "").isdigit():
            break
        for i in range(3, len(line)+1, 4):
            if line[i-3:i] != "   ":
                matrix[int(-0.75 + i*0.25)].insert(0, line[i-3:i])

    for line in input:
        if line[:4] == "move":
            instruction = [word for word in line.split()]
            amount = int(instruction[1])
            from_stack = int(instruction[3]) - 1
            to_stack = int(instruction[5]) - 1
            moved_stack = [] #D N Z
            for _ in range(amount):
                moved_stack.append(matrix[from_stack][-1])
                del matrix[from_stack][-1]
            moved_stack.reverse()
            for create in moved_stack:
                matrix[to_stack].append(create)
            print(matrix[to_stack])
    answer_list = []

    for list in matrix:
        answer_list.append(list[-1])

    answer_string = "".join(answer_list).replace("[", "").replace("]", "")
    print(answer_string)



solve_part_two()

def fuel_requirement(input):
    return input//3 - 2


def recursive_fuel_requirement(input):
    if input <= 0:
        return 0
    cur_fuel_requirement = fuel_requirement(input)
    if cur_fuel_requirement < 0:
        return 0
    return cur_fuel_requirement + recursive_fuel_requirement(cur_fuel_requirement)


def main():
    with open("input.txt") as f:
        inputs = f.readlines()
        sum = 0
        for input in inputs:
            sum += recursive_fuel_requirement(int(input))
    return sum


if __name__ == '__main__':
    print(main())

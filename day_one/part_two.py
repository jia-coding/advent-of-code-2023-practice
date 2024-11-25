def calibrate_part_two():
    typecast_bank = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9" 
    }

    with open('day_one/part_two_input.txt', 'r') as file:
        content = file.read()
        lines = content.splitlines()
        sum = 0
        for line in lines:
            string_number_list = []
            substring = ""
            for char in line:
                if char.isdigit():
                    string_number_list.append(char)
                else:
                    substring += char
                    if substring in typecast_bank:
                        string_number_list.append(typecast_bank[substring])
                        substring = ""
                    elif not any(word.startswith(substring) for word in typecast_bank):
                        substring = ""

            sum_string = string_number_list[0]+string_number_list[-1]
            sum += int(sum_string)

    return sum 

print(calibrate_part_two())

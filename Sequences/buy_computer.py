available_parts = ["computer",
                   "monitor",
                   "keyboard",
                   "mouse",
                   "mouse mat",
                   "hdmi cable",
                   "dvd drive"]
# valid_choices = [str(i) for i in range(1, len(available_parts)+1)]
valid_choices = []
for i in range(1, len(available_parts)+1):
    valid_choices.append(str(i))
print(valid_choices)
current_choice = '-'
computer_parts = []
# 1- computer,2- monitor, 3- keyboard, 4- mouse, 5- mouse mat, 0- exit

while current_choice != "0":
    if current_choice in valid_choices:
        index = int(current_choice)-1
        chosen_part = available_parts[index]
        if chosen_part in computer_parts:
            computer_parts.remove(chosen_part)   # I've already a chosen part so I removed it.
        else:
            computer_parts.append(chosen_part)
        print("Your cart now contain {}.".format(computer_parts))
    else:
        for number, part in enumerate(available_parts):  # enumerate function gives index pos and item as a pair value
            print("{0}: {1}".format(number+1, part))
    current_choice = input("Enter your item = ")

print(computer_parts)







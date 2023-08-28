PLACEHOLDER = "[name]"

with open("Input/Names/invited_names.txt") as names_file:
    invited_names = names_file.readlines()

with open("Input/Letters/starting_letter.txt") as start_letter_file:
    start_letter = start_letter_file.read()
    for name in invited_names:
        updated_name = name.strip("\n")
        new_letter = start_letter.replace(PLACEHOLDER, updated_name)
        with open(f"Output/ReadyToSend/letter_to_{updated_name}.txt", mode="w") as letter_file:
            letter_file.write(new_letter)

PLACEHOLDER = "[Name]"

with open("invited_names.txt","r") as names:
    names_list = names.readlines()


with open("starting_letter.txt") as letter:
    l = letter.read()
    for name in names_list:
        name = name.strip("\n")
        new_letter = l.replace(PLACEHOLDER, name)
        with open(f"letter_for_{name}.txt","w") as completed_letter:
            completed_letter.write(new_letter)
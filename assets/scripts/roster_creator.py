import sys

def get_input():
    name = raw_input("What is the player's name?\n")
    number = raw_input("What is the player's number?\n")
    return (name, number)
def write():
    while True:
        name, number = get_input()
        if name == "":
            sys.exit()
        f = open("../../_eighteen/" + str(name.lower().replace(" ", "")) + ".html", "w")
        content = "---\nlayout: player_card\n"
        content += "player_name: " + str(name) + "\n"
        content += "player_number: " + str(number) + "\n"
        content += "---"
        f.write(content)
        f.close()
write()


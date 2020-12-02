
def check(own, foreign):
    answer = str(input(f"{own}="))
    if str(answer) == str(foreign):
        print("Your answer is right! - next one")
    elif str(answer) == "q":
        return False
    else:
        print(f"Your answer is wrong! The correct answer would be: {foreign}")

if __name__ == "__main__":
    print("Please translate the following words! If you want to stop write q instead of the vocabulary.")
    with open("vocs.txt", "r") as vocab:
        for line in vocab:
            if line.startswith("#") or line.startswith(" ") or line.startswith("\n"):
                continue
            else:
                foreignvoc = str(str(line).split("=")[1]).split("\n")[0]
                ownvoc = str(line).split("=")[0]
                if check(ownvoc, foreignvoc) == False:
                    break

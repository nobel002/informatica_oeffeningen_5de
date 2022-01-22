def hint(guess, answer):
    output = ""
    for i in range(len(guess)):
        if guess[i] == answer[i]:
            output += guess[i].upper()
        elif guess[i] in answer:
            output += guess[i]
        else:
            output += "."
    return output


print(hint('spoed','depri'))

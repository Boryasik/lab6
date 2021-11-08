def rot(num):
    opening = str(num)
    ending = ''
    for i in range(len(opening)):
        if opening[i] != "9" and opening[i] != "6":
            return print("Нужно число состоящее только из цифр '6' и '9'")

    for i in range(len(opening)):
        if opening[i] == "9":
            ending += opening[i]
        else:
            ending += "9"
            ending += opening[i + 1:len(opening)]
            return int(ending)

def splits(getal):
    return tuple([int(i) for i in str(getal)])
    # or
    # a = getal %10
    # getal //= 10
    # b = getal % 10
    # getal //= 10
    # c = getal % 10
    # getal //= 10
    # d = getal % 10
    # return d, c, b, a


def oplopende_cijfers(a, b, c, d):

    # met min en max en max(min, min, min)
    temp = [a, b, c, d]
    temp.sort()
    return tuple(temp)

def op_af_getallen(a, b, c, d):
    #oplopend = ''.join([str(_) for _ in oplopende_cijfers(a, b, c, d)])
    #aflopend = ''.join([str(_) for _ in oplopend[::-1]])
    w, x, y, z = oplopende_cijfers(a, b, c, d)
    return str(w)+str(x)+str(y)+str(z), str(z)+str(y)+str(x)+str(w)

def verschil(string1, string2):
    return str(int(string1) - int(string2))

def kapkar(getal):
    getal_ = getal
    string = ""
    while getal_ != 6174:

        string += f"{} - {} = {}"
        string += "\n"


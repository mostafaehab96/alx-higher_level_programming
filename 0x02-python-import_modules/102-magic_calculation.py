from dis import dis

def magic_calulation(a, b):
    from magic_calulation_102 import add, sub

    if a < b:
        c = add(a, b)
        for i in range(4, 6):
            c = add(c, i)
        return c
    else:
        return sub(a, b)

dis(magic_calulation)

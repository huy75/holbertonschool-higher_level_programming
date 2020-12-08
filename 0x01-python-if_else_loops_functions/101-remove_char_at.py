def remove_char_at(str, n):
    if n < 0:
        return str

    temp = str[:n] + str[n + 1:]
    return temp

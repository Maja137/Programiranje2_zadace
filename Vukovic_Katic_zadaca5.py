def string_unazad (ime):
    if len(ime)==0:
        return ime
    else:
        return string_unazad(ime[1:])+ime[0]



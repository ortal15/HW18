"""1,a:"""

print('a:')
t1: tuple[int] = (99,)

"""b:"""
print('b:')
t2 = (99, 88, 77)
"""c:"""

print('c:')


def tup(tuple_c) -> int:
    return len(tuple_c)


print(tup(tuple_c=()))
"""d:"""

print('d:')


def tuple_2(tuple2, tuple1) -> int:
    tuple_d = tuple2 + tuple1
    return tuple_d


print(tuple_2(tuple2=(), tuple1=()))

"""e:"""
print('e:')


def tup_e(tup1, tup2) -> tuple:
    t_result: list[int] = []
    for i in tup1:
        if i in tup2:
            t_result.append(i)
    return tuple(t_result)


print(tup_e(tup1=(1, 2, 3, 4), tup2=(3, 4, 5, 6)))
"""f:"""

print('f:')


def tup_f(f1, f2) -> tuple:
    t_result: list[int] = []
    for i in f1:
        if i not in f2:
            t_result.append(i)
    for l in f2:
        if l not in f1:
            t_result.append(l)
    return tuple(t_result)


print(tup_f(f1=(1, 2, 3, 4), f2=(3, 4, 5, 6)))
"""g:"""
print('g:')


def indexx(tuple_g, ind):
    tuple_g: tuple = tuple(input('enter a tuple:'))
    ind: int = int(input('enter index:'))

    if ind > len(tuple_g):
        return 'None'
    else:
        return tuple_g[ind]


print(indexx(tuple_g=(), ind=()))

"""h:"""

print('h:')


def rev_tup(tuple_h) -> tuple:
    return tuple_h[::-1]


"""i:"""
print('i:')


def fon_i(tup_i, num) -> tuple:
    tup_i: tuple = tuple(input('enter int tuple:'))
    num: int = int(input('enter a number:'))
    return tup_i * num


print(fon_i(tup_i=(), num=()))
"""j"""
print('j:')


def def_j(tup_j, num_j) -> tuple:
    tup_j: tuple = tuple(input('enter a tuple:'))
    num_j: int = int(input('enter a number:'))
    list_j: list = [tup_j]
    for j in list_j:
        if num_j in list_j:
            list_j.pop(num_j)
    return tuple(list_j)


print(def_j(tup_j=(), num_j=()))

"""k"""
print('k:')


def def_k(tuple_k) -> tuple:
    list_k = []
    for item in tuple_k:
        if item not in list_k:
            list_k.append(item)
    return tuple(list_k)


tuple_k = tuple(input('enter a tuple:'))
print(def_k(tuple_k))
"""l:"""
print('l:')


def def_l(tup, num) -> tuple:
    tup = tuple(input('enter a tuple:'))
    num: int = int(input('enter a number:'))
    list_l: list[int] = []
    for l in range(len(tup)):
        if tup[l] == num:
            list_l.append(tup.index(num))

    return tuple(list_l)


# לצערי לא הצלחתי
print(def_l(tup=(), num=()))

"""m:"""


def zip_grade() -> tuple:
    names = []
    grades = []
    name: str = input('name? ["done" to finish]')
    while not name == "done":
        names.append(name)
        name: str = input('name? ["done" to finish]')
    grade: int = int(input('grade? ["-999" to finish]'))
    while not grade == -999:
        grades.append(grade)
        grade: int = int(input('grade? ["-999" to finish]'))
    result_zip = (tuple(zip(names, grades)))
    return result_zip


print('2:')
"""הוא מבנה נתןנים שלא ניתן לשינוי ותופס פחות זיכרון ובזכות זה הוא גם יותר מהיר - tuple """
"""list- כן ניתן לשינוי ובגלל זה תופס יותר זיכרון ויותר איטי לעבור על כל האיבקים שלו. """

print('3:')
"""הקוד לא גורם לשגיאה בגלל שבתוך ה (data_tuple) יש שני (dict) שהם בעצם
אלו שמשתנים ולא ה (data_tuple) עצמו ."""

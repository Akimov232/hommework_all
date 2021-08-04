letter_all = 'фывапролджэйцукенгшщзхъячсмитьбю'
def letter_upper(q):
    '''
    input: string user
    output: list of quantity letter capital
    '''
    letter_1 = 0
    for i in q:
        for q in letter_all.upper():
            if i == q:
                letter_1 += 1
    return letter_1



def letter_lower(a):
    '''
    input: string user
    output: list of quantity letter lower
    '''
    letter_2 = 0
    for i in a:
        for q in letter_all.lower():
            if i == q:
                letter_2 += 1
    return letter_2

def resalts_upper(letter_1 , letter_2):
    print(f'''Заглавных букв:{letter_1}
    строчных букв {letter_2}''')
    

         
def letter_app():
    string = 'Меня Зовут даня'
    range_of_string_upper = letter_upper(string)
    range_of_string_lower = letter_lower(string)
    resalts_upper(range_of_string_upper , range_of_string_lower )

letter_app()
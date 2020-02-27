'''
Дана непорожня послідовність слів з малих українських літер; між сусідніми
словами - кома, за останнім словом - крапка. Вивести на екран в алфавітному порядку всі
глухі приголосні букви, що входять в кожне непарне слово і не входять хоча б в одне
парне слово.
'''
while True:
    while True:
        try:
            user_words = (input('Enter your words: '))
            break
        except ValueError:
            print('Enter correct value')
    user_words_list = user_words[:-1].split(', ')
    user_words_set = set(user_words_list)
    pair_list = []
    not_pair_list = []
    control_set = {'к', 'с', 'п', 'т', 'ф', 'х', 'ц', 'ч', 'ш'}
    for i in range(1, len(user_words_list), 2):
        not_pair_list.append(user_words_list[i])
    for i in range(2, len(user_words_list), 2):
        pair_list.append(user_words_list[i])
    for i in pair_list:
        pair_set = control_set & set(i)
    for i in not_pair_list:
        final_set = pair_set - set(i)
    print(final_set)
    if input('Press Enter if you want continue:') != '':
        break




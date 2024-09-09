god_pushkin = '1799'
god_putin = '1952'
god_lenin = '1870'
god_stalin = '1878'
god_gagarin = '1934'

otv = 'Да'
while otv == 'Да':

    pravotv = 0

    otv_pushkin = input('Когда родился Пушкин А.С. :')
    if otv_pushkin == god_pushkin:
        pravotv += 1
    otv_putin = input('Когда родился Путин В.В. :')
    if otv_putin == god_putin:
        pravotv += 1
    otv_lenin = input('Когда родился Ленин В.И. :')
    if otv_lenin == god_lenin:
        pravotv += 1
    otv_stalin = input('Когда родился Сталин И.В. :')
    if otv_stalin == god_stalin:
        pravotv += 1
    otv_gagarin = input('Когда родился Гагарин Ю.С. :')
    if otv_gagarin == god_gagarin:
        pravotv += 1

    neprotv = 5 - pravotv

    print('Количество правильных ответов   :', pravotv)
    print('Количество неправильных ответов :', neprotv)
    print('Процент правильных ответов      :', (pravotv * 100) / 5)
    print('Процент непправильных ответов   :', (neprotv * 100) / 5)

    otv = input('Хотите продолжить игру (Да, Нет)')
    if otv != 'Да':
        break


god_r = '1799'
day_r = '6'
otv_g = input('Год рождения А.С Пушкина:')
if otv_g == god_r:
    otv_d = input('День рождения А.С Пушкина:')
    if otv_d == day_r:
        print('Верно')
    else:
        print('Неверный день рождения')
else:
    print('Неверный год')
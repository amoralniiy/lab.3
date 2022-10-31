astma=False # Астма отсутствует
bol=True # Заражение
c=30 #point
cfull=200 # Общее кол-во предметов
one=[15,25,15,5] # 1 ячейка
two=[15,15,20,20,20] # 2 ячейки
three=[25,20] # 3 ячейки
name1=['н','о','ф','и']
name2=['п','б','а','к','р']
name3=['в','т']
part1=['д']
part2=[]
x = zip(one,name1) # соответствие очков выживания к каждому предмету
y = zip(two,name2)
z = zip(three,name3)
xs = sorted(x, key=lambda tup: tup[0],reverse=True) # сортировка
ys = sorted(y, key=lambda tup: tup[0],reverse=True)
zs = sorted(z, key=lambda tup: tup[0],reverse=True)
c1=xs[0][0]+xs[1][0]+xs[2][0] # сумма очков выживания
c2=ys[0][0]+xs[1][0]
c3=zs[0][0]
if c1 == max(c1, c2, c3):
    c+=c1
    part1+=xs[0][1]+xs[1][1]+xs[2][1] # наличие предметов в инвентаре
    xs.reverse() # обратный список
    xs.pop() # удаление элемента
    xs.pop()
    xs.pop()
    xs.reverse()
elif c2 == max(c1, c2, c3):
    c+=c2
    part1+=ys[0][1]+ys[0][1]+xs[0][1]
    xs.reverse()
    xs.pop()
    xs.reverse()
    ys.reverse()
    ys.pop()
    ys.reverse()
else:
    c += c3
    part1 += zs[0][1] + zs[0][1] + zs[0][1]
    zs.reverse()
    zs.pop()
    zs.reverse()
print(part1)
c2=ys[0][0]+ys[1][0]
c3=zs[0][0]+xs[0][0]
if c3>c2:
    c+=c3
    part2 += zs[0][1]+zs[0][1]+zs[0][1]+xs[0][1]
    zs.reverse()
    zs.pop()
    zs.reverse()
    xs.reverse()
    xs.pop()
    xs.reverse()
else:
    c+=c2
    part2 += ys[0][1]+ys[0][1]+ys[1][1]+ys[1][1]
    ys.reverse()
    ys.pop()
    ys.pop()
    ys.reverse()
print(part2)
if c>=100:
    print('TRUE')
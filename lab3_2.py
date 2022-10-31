astma=True
bol=False
c=10
cfull=200
one=[15,25,15,10]
two=[15,15,20,20,20]
three=[25,20]
name1=['н','о','ф','д']
name2=['п','б','а','к','р']
name3=['в','т']
part1=[]
x = zip(one,name1)
y = zip(two,name2)
z = zip(three,name3)
xs = sorted(x, key=lambda tup: tup[0],reverse=True)
ys = sorted(y, key=lambda tup: tup[0],reverse=True)
zs = sorted(z, key=lambda tup: tup[0],reverse=True)
c1=zs[0][0]+zs[1][0]+xs[0][0]
c2=zs[0][0]+xs[0][0]+xs[1][0]+xs[2][0]+xs[3][0]
c3=zs[0][0]+ys[0][0]+ys[1][0]
c4=zs[0][0]+ys[0][0]+xs[1][0]+xs[0][0]
c5=ys[0][0]+ys[1][0]+xs[0][0]+xs[1][0]+xs[2][0]
c6=ys[0][0]+ys[1][0]+ys[2][0]+xs[0][0]
print(c1,c2,c3,c4,c5,c6)
if c1>=100:
    part1+=zs[0][1]+zs[1][1]+xs[0][1]
elif c2>=100:
    part1+=zs[0][1]+xs[0][1]+xs[1][1]+xs[2][1]+xs[3][1]
elif c3>=100:
    part1+=zs[0][1]+ys[0][1]+ys[1][1]
elif c4>=100:
    part1+=zs[0][1]+ys[0][1]+xs[1][1]+xs[0][1]
elif c5>=100:
    part1+=ys[0][1]+ys[1][1]+xs[0][1]+xs[1][1]+xs[2][1]
elif c6>=100:
    part1+=ys[0][1]+ys[1][1]+ys[2][1]+xs[0][1]
if len(part1)==0:
    print('NO')
else:
    print(part1)
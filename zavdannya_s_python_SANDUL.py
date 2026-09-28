print("Рівень 1: розминка")
a = 17
b = 5
ab = a+b
print(ab)

Ab = a-b
print(Ab)

aB = a*b
print(aB)

AB = a/b #Ділить з результатом після крапки
print(AB)

ABc = a//b #Ділить з округленням остачі
print(ABc)

ABC = a%b
print(ABC)

c = 2**10
print(c)

d = 10**3
print(d)

price = 249.99
count = 3
Total_price = price*count
print(Total_price)

print(type(7 / 2)) # class float тому що число ділиться на дробове
print(type(7 // 2)) # class intтому що число остається цілим
print(type(7.0 // 2)) # class float тому що число ділиться на дробове

name = "Python" * 3
print(name)

hello = "Привіт,"
world = " світ!"
print(hello+world)


print("Рівень 2: практичні обчислення")
ychni = 28
part = 6
povnix = ychni//part
ostacha = ychni%part
print("Повних парт:")
print(povnix)
print("Остача учнів:")
print(ostacha)

sec = 3725
min = sec//60
hour = min/60
print("Годин в 3725секундах")
print(hour)

mins = 150
hours = mins/60
print("Годин в 150 хвилинах")
print(hours)

cel = 36.6
fah = cel * 9 / 5 + 32
print("Фаренгейти")
print(fah)

A = 12.5
B = 8
S = A * B
P = 2 * (A + B)
print("Площа")
print(S)
print("Периметр")
print(P)

r = 7
pi = 3.14159
SS = pi * r**2
C = 2 * pi * r
print("Площа")
print(S)
print("Периметр")
print(P)

tovar = 1200
znizka = 15
discount = tovar * (znizka / 100)
print("Знижка в грн")
print(discount)
final = tovar - discount
print("Остаточна ціна")
print(final)

zp = 25000
podatok = 19.5
minus = zp - (podatok / 100)
print("На руки отримує:")
print(minus)

V = 90
t = 2.5
vidstan = V * t
print("Подолав відстань у км")
print(vidstan)

afifmetika = (10+11+8)//3
print("Середня оцінка:")
print(afifmetika)


print("Рівень 3: цифри та числа")
n = 7//2
print(n)
if n == 1:
    print("Парне")
else:
    print("Непарне")

N = 473
Ne = N % 10
print("Останнє число в 473")
print(Ne)

Nen = N // 100
NEn = (N%100) // 10
NEN = (N%100)%7
print("Числа отдельно")
print(Nen)
print(NEn)
print(NEN)

chislo = 859
ei = chislo//100
fi = (chislo%100)//10
nin = (chislo%100)//fi
print("Сума цифр", nin+fi+ei)


number = 123
d3 = number % 10
d2 = (number // 10) % 10
d1 = number // 100
r_n = d3 * 100 + d2 * 10 + d1
print("Перевернуте число:",r_n)

korin = 144**0.5
print("Корінь:", korin)

days = 365
hours = days * 24
minutes = hours * 60
seconds = minutes * 60
print("Кількість секунд у році:",seconds)


print("Рівень 4: типи даних і хитрощі")
x = "5"
y = "3"
xy = x + y
print("Зєднання:",x + y)
print("Обчислення:",int(x) + int(y))

c = 9.99
print(c)
print("Перетворило в ціле число із за int:",int(c))

res1 = True + True + True
res2 = True * 10
print("Посщитало тру за 1:",res1, type(res1))
print("умножило тру на 10:",res2, type(res2))

a = 5
b = 10
a = a + b
print(a)

deposit = 10000
rate = 0.12
years = 3
sum = deposit * (1+rate) ** years
summ = sum//1 #щоб позбавитись цифр за крапкою
print("Сума через 3 роки:",summ)


char = "-"
count = 20
print(char * count)
result_str = str(2 ** count)
print("Результат: " + result_str)
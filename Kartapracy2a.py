 #zad1
# a = int(input())
# b = int(input())
# if (a+b) %2 ==0:
#     print("Tak")
# else:
#     print("Nie")

#zad2

# a = int(input())
# g = int(input())
# if (a+g)/2 > (a**g)/(1/2):
#     print("Tak")
# else:
#     print("Nie")

#zad3 
# k, l, m = int(input()), int(input()), int(input())
# if (k == l) or (k == m) or (l == m):
#     print("tak") 
# else:
#     print("nie")

#zad4

# a, b, c, d, = int(input()), int(input()), int(input()), int(input())
# if a<b and a<c and a<d:
#     print("a jest najmniejsze")
# if b<a and b<c and b<d:
#     print("b jest najmniejsze")
# if c<a and c<b and c<d:
#     print("c jest najmniejsze")
# if d<a and d<b and d<c:
#     print("d jest najmnijesze")

# Zad 5

# a, b, c, = int(input("podaj a: ")), int(input("podaj b: ")), int(input("podaj c: "))
# if a < (b+c) and b < (c+a) and c< (a+b):
#   print('TAK')
# else:
#   print('NIE')

# Zad 6

a,b,c = int(input("podaj a = ")),int(input("podaj b = ")),int(input("podaj c = "))

if (a*a+b*b == c*c) or (a*a+c*c == b*b) or (c*c+b*b == a*a):
    print("prostokątny")
else:
    if (a*a+b*b < c*c) or (a*a+c*c < b*b) or (c*c+b*b < a*a):
        print("rozwartokątny")
    else:
        if (a*a+b*b > c*c) or (a*a+c*c > b*b) or (c*c+b*b > a*a):
            print("ostrokątny")
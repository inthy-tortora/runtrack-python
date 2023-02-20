a = input('Entrer la longueur a : \n ')
b = input('Entrer la longueur b : \n ')
c = input('Entrer la longueur c : \n 8')

def triangle(a,b,c):
    if b+c > a :
        if b*b+c*c == a*a and b==c :
            print('je suis un triangle rectangle isocèle.')
        elif b*b+c*c == a*a :
            print('je suis un triangle rectangle')
        elif b==a==c :
            print ('je suis un triangle equilatéral.')
        elif b==c or a==b or a==c :
            print ('je suis un triangle isocèle.')
        else :
            print('je suis un triangle quelconque.')         
    else :
        print ('je ne suis pas un triangle.')
               
triangle(float(a),float(b),float(c))
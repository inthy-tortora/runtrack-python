type = input('Entrer fruits ou legume : \n' )
saison = input ('Entrer votre saison, ete ou hiver : \n ')


def fruit_legume(type,saison):
    if type == 'fruits' and saison == 'hiver' :
        print ('Orange, Mandarine, Kiwi')
    elif type == 'fruits' and saison == 'ete' :
        print ('Poire, Fraise, Cassis')
    elif type == 'legume' and saison == 'hiver' :
        print ('Carotte, Topinambour, Endive')
    elif type == 'legume' and saison == 'ete' :
        print ('Artichaut, Aubergine, Navet')

fruit_legume(type,saison)

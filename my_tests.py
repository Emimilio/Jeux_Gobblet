
from joueur import Joueur, Automate
from plateau import Plateau


'''def best_colonne(plateau):
    for n in plateau:
        print(n)
    #plat = list(zip(*plateau[::-1]))
    plat = list(reversed(list(zip(*plateau))))
    print('')
    print('')
    for i in plat:
        print(i)
val = 1
while True:
    
    val += 1
    print(val)
    if val > 15:
        break

plateau = [[[[1,2], [1,3]], [], [], []], [[], [], [[1,3]], []], [[], [], [], []], [[], [], [], []]]
plat = Plateau(plateau)
print(plat[(0,0)])
for i in plat[(0,0)]:
    print(i)



x = plat.retirer_gobblet(0,3)
print(x)
joueur = Automate('em', 1, [[1,2], [1,2], [1,2]])
x = joueur.valid_moves(plat)

print(x)
x = {(1,2): 3, (1,1): 2, (1,1):0, (1,0): 5}
print(max(x))

gobs = {'gob': 0, 'i,j': 0, 'grosseur': -1}
print(gobs.get('i,j') is not None)'''
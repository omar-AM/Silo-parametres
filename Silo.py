# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""
import matplotlib as mpl
import scipy

mais = {'MV':1000,'densite':500,}
class silo:
    
    def __init__(self,D,H,Phi1,Phi2,D_T):
        self.D = D
        self.H = H
        self.Phi1 = Phi1
        self.Phi2 = Phi2
        self.Dt = D_T
           
 
    def __str__(self):
        return 'Silo de parametres(diametre = %r,hauteur = %r,D sortie = n\
                %r,Phi1 = %r,Phi2 = %r )' % (int(self.D), self.H, self.Dt, self.Phi1 .self.Phi2)


    


while(True):
    '''main program'''
    print('You need to enter the Silo parametres')
    print(' :) ')
    print(' ')
    
    
    
    
    
    
    print('all done, Enjoy')
    ''' end of main program. '''
    print('press "y" if you want to try another calculus')
    print('and "n" if you want to exit')
    try:
        v = str(input('__> '))
    except ValueError:
        print('valid response, Please')
        continue
        if v == 'y' or v == 'Y':
            continue
        elif v == 'N' or v == 'n':
            break
        break
    break

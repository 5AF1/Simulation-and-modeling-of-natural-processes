from random import *

rho=0.7
m_i=0.6
d_i='S'
p_i=0.4
p_d=0.6

def randomDirection():
    return choice(['N','S','E','W'])

def behaviour(rho,m_i,d_i):
    if rho<=m_i:
       p=p_d
    else:
       p=p_i
    if random()<=p:
       return rho,randomDirection()
    else:
       return rho,d_i

n,s,e,w = 0,0,0,0
for i in range(500000):
    a,b = behaviour(rho,m_i,d_i)
    if b == "N":
        n += 1
    elif b == "S":
        s += 1
    elif b == "E":
        e += 1
    elif b == "W":
        w += 1

print(f"n:{n} s:{s} e:{e} w:{w}")
import numpy as np
import matplotlib.pyplot as plt

def psi(x,n,t):
    A=np.sqrt(30)
    a=1
    h=6.62*10**-34/(2*np.pi)
    m=0.0001
    return A*np.sqrt(2*a)*((-1)**n-1)/(np.pi**3*n**3)*1*np.exp(complex(0,n**2*np.pi**2*h*t/(2*m*a**2))*np.sqrt(2/a)*np.sin(n*np.pi*x/a))
x=np.linspace(0,1,1000)
t=np.linspace(0,10,100)
psi_1=0
for n in range(1000):
    psi_1=psi_1+psi(x,n,1)

p1=psi_1*np.conj(psi_1)

plt.plot(x,p1)

plt.show()                                                            


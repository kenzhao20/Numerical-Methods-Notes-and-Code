import numpy as np
import matplotlib.pyplot as plt

ul=100 #Boundary condition at x=xi
ur=50 #Boundary condition at x=xf
sigma=0.5#Set sigma
mu=0.4009 #Set value of (sigma*dt)/(dx^2) which must be <0.5 for stability

xi=0 #Left Boundary
xf=1 #Right Boundary
dx=0.05 #step size x

ti=0 #Initial time
tf=1 #Final time
dt=dx**2*mu/sigma #step size in t is fixed by step size in x, mu, and sigma

x=np.arange(xi,xf,dx) #Create mesh
t=np.arange(ti,tf,dt) #


u=np.zeros((len(t),len(x))) #Create solution of size (length(t),length(x))

#Set initial condition
#u=1 for x between 0.4 and 0.6
#u[0,int(1/dx*0.4):int(1/dx*0.6)]=1


#Set boundary condition for left and right spatial boundary
u[:,0]=ul
u[:,u.shape[1]-1]=ur

#Plot

#fig=plt.figure(figsize=(6,2))
#plt.plot(x,u[0])
#plt.title('Initial condition at t=0')
#plt.xlabel('x')
#plt.ylabel('u')



fig=plt.figure(figsize=(6,6))
for k in range(1,len(t)): #Loop over t slices
    plt.clf()
    plt.ion()
    for i in range(1,len(x)-1): #Loop over x slices but exclude boundaries
        u[k,i]=u[k-1,i]+mu*(u[k-1,i+1]-2*u[k-1,i]+u[k-1,i-1]) #Execute scheme
    plt.plot(x,u[k-1,:],label=f't={t[k-1]}')
    plt.show()
    plt.axis([xi,xf,0,ul])
    plt.xlabel('x')
    plt.ylabel('u')
    plt.legend()
    plt.pause(0.00000001)
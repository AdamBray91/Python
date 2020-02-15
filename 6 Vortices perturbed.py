import numpy as np, matplotlib.pyplot as pt
fig1, ax1=pt.subplots(figsize=(5,5))

'vortices and respective circulations'

v1=complex(2,0.01)
v2=complex(1,3**0.5)
v3=complex(-1,3**0.5)
v4=complex(-2,0)
v5=complex(-1,-3**0.5)
v6=complex(1,-3**0.5)

c1=1
c2=1
c3=1
c4=1
c5=1
c6=1

'equations'
def potential_gradient(v1,v2,v3,v4,v5,v6,c2,c3,c4,c5,c6):
    u = (1/(2*np.pi*complex(0,1)))*(c2/(v1-v2)+c3/(v1-v3)+c4/(v1-v4)+c5/(v1-v5)+c6/(v1-v6))
    return complex(u.real, -u.imag)

def RK4(v1,v2,v3,v4,v5,v6,c2,c3,c4,c5,c6,h):
        
    k1 = potential_gradient(v1,v2,v3,v4,v5,v6,c2,c3,c4,c5,c6)*h
    k2 = potential_gradient(v1 + k1*0.5,v2 + k1*0.5,v3 + k1*0.5,v4 + k1*0.5,v5 + k1*0.5,v6 + k1*0.5,c2,c3,c4,c5,c6)*h
    k3 = potential_gradient(v1 + k2*0.5,v2 + k2*0.5,v3 + k2*0.5,v4 + k2*0.5,v5 + k2*0.5,v6 + k2*0.5,c2,c3,c4,c5,c6)*h
    k4 = potential_gradient(v1 + k3,v2 + k3,v3 + k3,v4 + k3,v5 + k3,v6 + k3,c2,c3,c4,c5,c6)*h
    v1 = v1 + 1/6*(k1 + 2*k2 + 2*k3 + k4)

    return v1

'Vortex Leapfrogging'


time=44
nsteps=880
h=time/nsteps
n=0

'Initial Conditions'
ax1.plot(v1.real,v1.imag,'r.')
ax1.plot(v2.real,v2.imag,'b.')
ax1.plot(v3.real,v3.imag,'g.')
ax1.plot(v4.real,v4.imag,'y.')
ax1.plot(v5.real,v5.imag,'c.')
ax1.plot(v6.real,v6.imag,'m.')

ax1.plot([2,1],[0,3**0.5],'k--')
ax1.plot([1,-1],[3**0.5,3**0.5],'k--')
ax1.plot([-1,-2],[3**0.5,0],'k--')
ax1.plot([-2,-1],[0,-3**0.5],'k--')
ax1.plot([-1,1],[-3**0.5,-3**0.5],'k--')
ax1.plot([1,2],[-3**0.5,0],'k--')
ax1.set_title(r"Perturbed system of 6 vortices")
ax1.set_xlabel("x")
ax1.set_ylabel("y")

for n in range(0,nsteps):
    v1 = RK4(v1,v2,v3,v4,v5,v6,c2,c3,c4,c5,c6,h)
    v2 = RK4(v2,v1,v3,v4,v5,v6,c1,c3,c4,c5,c6,h)
    v3 = RK4(v3,v1,v2,v4,v5,v6,c1,c2,c4,c5,c6,h)
    v4 = RK4(v4,v1,v2,v3,v5,v6,c1,c2,c3,c5,c6,h)
    v5 = RK4(v5,v1,v2,v3,v4,v6,c1,c2,c3,c4,c6,h)
    v6 = RK4(v6,v1,v2,v3,v4,v5,c1,c2,c3,c4,c5,h)

    
    ax1.plot(v1.real,v1.imag,'r.')
    ax1.plot(v2.real,v2.imag,'b.')
    ax1.plot(v3.real,v3.imag,'g.')
    ax1.plot(v4.real,v4.imag,'y.')
    ax1.plot(v5.real,v5.imag,'c.')
    ax1.plot(v6.real,v6.imag,'m.')
    n=n+1
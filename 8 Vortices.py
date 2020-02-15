import numpy as np, matplotlib.pyplot as pt
fig1, ax1=pt.subplots(figsize=(5,5))

'vortices and respective circulations'

v1=complex(2,0)
v2=complex(2*np.cos((2*np.pi)/8),2*np.sin((2*np.pi)/8))
v3=complex(2*np.cos((4*np.pi)/8),2*np.sin((4*np.pi)/8))
v4=complex(2*np.cos((6*np.pi)/8),2*np.sin((6*np.pi)/8))
v5=complex(2*np.cos((8*np.pi)/8),2*np.sin((8*np.pi)/8))
v6=complex(2*np.cos((10*np.pi)/8),2*np.sin((10*np.pi)/8))
v7=complex(2*np.cos((12*np.pi)/8),2*np.sin((12*np.pi)/8))
v8=complex(2*np.cos((14*np.pi)/8),2*np.sin((14*np.pi)/8))

c1=1
c2=1
c3=1
c4=1
c5=1
c6=1
c7=1
c8=1
'equations'
def potential_gradient(v1,v2,v3,v4,v5,v6,v7,v8,c2,c3,c4,c5,c6,c7,c8):
    u = (1/(2*np.pi*complex(0,1)))*(c2/(v1-v2)+c3/(v1-v3)+c4/(v1-v4)+c5/(v1-v5)+c6/(v1-v6)+c7/(v1-v7)+c8/(v1-v8))
    return complex(u.real, -u.imag)

def RK4(v1,v2,v3,v4,v5,v6,v7,v8,c2,c3,c4,c5,c6,c7,c8,h):
        
    k1 = potential_gradient(v1,v2,v3,v4,v5,v6,v7,v8,c2,c3,c4,c5,c6,c7,c8)*h
    k2 = potential_gradient(v1 + k1*0.5,v2 + k1*0.5,v3 + k1*0.5,v4 + k1*0.5,v5 + k1*0.5,v6 + k1*0.5,v7 + k1*0.5,v8 + k1*0.5,c2,c3,c4,c5,c6,c7,c8)*h
    k3 = potential_gradient(v1 + k2*0.5,v2 + k2*0.5,v3 + k2*0.5,v4 + k2*0.5,v5 + k2*0.5,v6 + k2*0.5,v7 + k2*0.5,v8 + k2*0.5,c2,c3,c4,c5,c6,c7,c8)*h
    k4 = potential_gradient(v1 + k3,v2 + k3,v3 + k3,v4 + k3,v5 + k3,v6 + k3,v7 + k3,v8 + k3,c2,c3,c4,c5,c6,c7,c8)*h
    v1 = v1 + 1/6*(k1 + 2*k2 + 2*k3 + k4)

    return v1

'Vortex Leapfrogging'


time=5.5
nsteps=550
h=time/nsteps
n=0

'Initial Conditions'
ax1.plot(v1.real,v1.imag,'r.')
ax1.plot(v2.real,v2.imag,'b.')
ax1.plot(v3.real,v3.imag,'g.')
ax1.plot(v4.real,v4.imag,'y.')
ax1.plot(v5.real,v5.imag,'c.')
ax1.plot(v6.real,v6.imag,'m.')
ax1.plot(v7.real,v7.imag,'k.')  
ax1.plot(v8.real,v8.imag,'.',color = '#835C3B')   
ax1.plot([2,2*np.cos((2*np.pi)/8)],[0,2*np.sin((2*np.pi)/7)],'k--')
ax1.plot([2*np.cos((2*np.pi)/8),2*np.cos((4*np.pi)/8)],[2*np.sin((2*np.pi)/8),2*np.sin((4*np.pi)/8)],'k--')
ax1.plot([2*np.cos((4*np.pi)/8),2*np.cos((6*np.pi)/8)],[2*np.sin((4*np.pi)/8),2*np.sin((6*np.pi)/8)],'k--')
ax1.plot([2*np.cos((6*np.pi)/8),2*np.cos((8*np.pi)/8)],[2*np.sin((6*np.pi)/8),2*np.sin((8*np.pi)/8)],'k--')
ax1.plot([2*np.cos((8*np.pi)/8),2*np.cos((10*np.pi)/8)],[2*np.sin((8*np.pi)/8),2*np.sin((10*np.pi)/8)],'k--')
ax1.plot([2*np.cos((10*np.pi)/8),2*np.cos((12*np.pi)/8)],[2*np.sin((10*np.pi)/8),2*np.sin((12*np.pi)/8)],'k--')
ax1.plot([2*np.cos((12*np.pi)/8),2*np.cos((14*np.pi)/8)],[2*np.sin((12*np.pi)/8),2*np.sin((14*np.pi)/8)],'k--')
ax1.plot([2*np.cos((14*np.pi)/8),2],[2*np.sin((14*np.pi)/8),0],'k--')
ax1.set_title(r"8 Vortices initially on an octagon of radius 2")
ax1.set_xlabel("x")
ax1.set_ylabel("y")

for n in range(0,nsteps):
    v1 = RK4(v1,v2,v3,v4,v5,v6,v7,v8,c2,c3,c4,c5,c6,c7,c8,h)
    v2 = RK4(v2,v1,v3,v4,v5,v6,v7,v8,c1,c3,c4,c5,c6,c7,c8,h)
    v3 = RK4(v3,v1,v2,v4,v5,v6,v7,v8,c1,c2,c4,c5,c6,c7,c8,h)
    v4 = RK4(v4,v1,v2,v3,v5,v6,v7,v8,c1,c2,c3,c5,c6,c7,c8,h)
    v5 = RK4(v5,v1,v2,v3,v4,v6,v7,v8,c1,c2,c3,c4,c6,c7,c8,h)
    v6 = RK4(v6,v1,v2,v3,v4,v5,v7,v8,c1,c2,c3,c4,c5,c7,c8,h)
    v7 = RK4(v7,v1,v2,v3,v4,v5,v6,v8,c1,c2,c3,c4,c5,c6,c8,h)
    v8 = RK4(v8,v1,v2,v3,v4,v5,v6,v7,c1,c2,c3,c4,c5,c6,c7,h)
    
    ax1.plot(v1.real,v1.imag,'r.')
    ax1.plot(v2.real,v2.imag,'b.')
    ax1.plot(v3.real,v3.imag,'g.')
    ax1.plot(v4.real,v4.imag,'y.')
    ax1.plot(v5.real,v5.imag,'c.')
    ax1.plot(v6.real,v6.imag,'m.')
    ax1.plot(v7.real,v7.imag,'k.')  
    ax1.plot(v8.real,v8.imag,'.',color = '#835C3B')      
    n=n+1
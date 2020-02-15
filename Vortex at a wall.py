import numpy as np, matplotlib.pyplot as pt
fig1, ax1=pt.subplots(dpi=200)

'vortices and respective circulations'

v1=complex(1,1)
v2=complex(-1,1)
v3=complex(0,0)
v4=complex(0,0)

c1=1
c2=-1
c3=0
c4=0

'equations'
def potential_gradient(v1,v2,v3,v4,c2,c3,c4):
    u = (1/(2*np.pi*complex(0,1)))*(c2/(v1-v2)+c3/(v1-v3)+c4/(v1-v4))
    return complex(u.real, -u.imag)

def RK4(v1,v2,v3,v4,c2,c3,c4,h):
        
    k1 = potential_gradient(v1,v2,v3,v4,c2,c3,c4)*h
    k2 = potential_gradient(v1 + k1*0.5,v2 + k1*0.5,v3 + k1*0.5,v4 + k1*0.5,c2,c3,c4)*h
    k3 = potential_gradient(v1 + k2*0.5,v2 + k2*0.5,v3 + k2*0.5,v4 + k2*0.5,c2,c3,c4)*h
    k4 = potential_gradient(v1 + k3,v2 + k3,v3 + k3,v4 + k3,c2,c3,c4)*h
    v1 = v1 + 1/6*(k1 + 2*k2 + 2*k3 + k4)

    return v1


'Initial Conditions'
ax1.plot(v1.real,v1.imag,'r.', label='Vortex at initial position $z_1 = 1+i$')
ax1.plot(v2.real,v2.imag,'b.', label='Mirrored Image Vortex at initial position $z_2 = -z^*_1$')
#ax1.plot(v3.real,-v3.imag,'g.', label='Mirrored vortex image at initial position $z_3 = z^*_1$')
#ax1.plot(v4.real,-v4.imag,'y.', label='Mirrored vortex image at initial position $z_4 = -z_1$')

ax1.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.,fontsize=15)
ax1.set_title("Vortex motion near a solid wall",fontsize=17)
ax1.set_xlabel("x")
ax1.set_ylabel("y")
ax1.plot([0,0],[0.2,1],'k-',linewidth=3.0)

time=10
nsteps=60
h=time/nsteps
n=0


for n in range(0,nsteps):
    v1 = RK4(v1,v2,v3,v4,c2,c3,c4,h)
    v2 = RK4(v2,v1,v3,v4,c1,c3,c4,h)
#    v3 = RK4(v3,v1,v2,v4,c1,c2,c4,h)
#    v4 = RK4(v4,v1,v2,v3,c1,c2,c3,h)

    
    ax1.plot(v1.real,v1.imag,'r.')
    ax1.plot(v2.real,v2.imag,'b.')
#    ax1.plot(v3.real,-v3.imag,'g.')
#    ax1.plot(v4.real,-v4.imag,'y.')

    n=n+1
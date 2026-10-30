from pathlib import Path
import math
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle

OUT=Path(__file__).resolve().parent
OUT.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,
 'axes.spines.top':False,'axes.spines.right':False,
 'axes.labelcolor':'#253047','text.color':'#253047',
 'axes.edgecolor':'#8794a7','xtick.color':'#526176','ytick.color':'#526176',
 'svg.fonttype':'none','figure.facecolor':'white','axes.facecolor':'white'})
BLUE='#2563ab'; ORANGE='#cc7543'

def save(fig,name):
    fig.savefig(OUT/(name+'.svg'),bbox_inches='tight')
    plt.close(fig)

fig,ax=plt.subplots(figsize=(8.4,4.8))
colors=['#dce9f4','#ebf0fa','#e1efe9','#e8eff9','#e1edf6','#f5e8dc','#e2eee9','#f2eee0','#e5e9f5']
for r in range(3):
    for c in range(3):
        i=3*r+c
        ax.add_patch(Rectangle((c,2-r),1,1,facecolor=colors[i],edgecolor='#6f8096',lw=1.3))
        ax.text(c+.2,2-r+.75,rf'$C_{{{i+1}}}$',fontsize=14)
ax.add_patch(Circle((1.52,1.48),.97,facecolor=BLUE,alpha=.12,lw=0))
ax.add_patch(Circle((1.52,1.48),.97,fill=False,edgecolor=BLUE,lw=2.5))
ax.text(1.47,1.48,'A',color=BLUE,fontsize=21,fontweight='bold')
ax.text(3.08,2.85,'S',fontsize=18,fontweight='bold')
ax.set(xlim=(-.08,3.35),ylim=(-.1,3.15),aspect='equal')
ax.axis('off')
fig.suptitle('Partição do espaço amostral',fontsize=15,fontweight='bold')
fig.text(.5,.025,r'$A=\bigcup_i(A\cap C_i)$, com parcelas disjuntas',ha='center')
save(fig,'particao')

def cdf_plot(xs,ys,xlim,title,name,yticks=None):
    fig,ax=plt.subplots(figsize=(8.4,4.6))
    ax.grid(axis='y',color='#e4eaf0',lw=.8,zorder=0)
    left=xlim[0]
    for k,(x,y) in enumerate(zip(xs,ys)):
        previous=0 if k==0 else ys[k-1]
        ax.plot([left,x],[previous,previous],color=BLUE,lw=2,zorder=3)
        ax.scatter([x],[previous],s=35,facecolors='white',edgecolors=BLUE,lw=1.5,zorder=5)
        ax.scatter([x],[y],s=32,color=BLUE,zorder=6)
        left=x
    ax.plot([xs[-1],xlim[1]],[ys[-1],ys[-1]],color=BLUE,lw=2)
    ax.axhline(1,color='#9da8b8',ls='--',lw=1,zorder=1)
    ax.set(xlim=xlim,ylim=(-.035,1.075),xlabel='$x$',ylabel='$F_X(x)$',title=title)
    ax.set_xticks(xs)
    if yticks is not None:
        ax.set_yticks([0,.125,.5,.875,1],['0','1/8','1/2','7/8','1'])
    fig.tight_layout()
    save(fig,name)

cdf_plot(np.arange(4),np.array([1,4,7,8])/8,(-.5,3.7),
         'Número de caras em três lançamentos', 'cdf-tres-moedas',True)
p=.3
x=np.arange(1,16)
cdf_plot(x,1-(1-p)**x,(0,15.8),r'Geométrica: $p=0{,}3$', 'cdf-geometrica')

x=np.linspace(1.35,2.1,600)
fig,axes=plt.subplots(2,1,figsize=(8.4,6.6),sharex=True)
for mu,sigma,color,name in [(1.65,.08,BLUE,'Modelo I'),(1.78,.09,ORANGE,'Modelo II')]:
    z=(x-mu)/sigma
    pdf=np.exp(-z*z/2)/(sigma*np.sqrt(2*np.pi))
    cdf=np.array([.5*(1+math.erf(float(t)/math.sqrt(2))) for t in z])
    label=f'{name}: média {mu:.2f} m; desvio {sigma:.2f} m'.replace('.',',')
    axes[0].plot(x,pdf,color=color,lw=2.2,label=label)
    axes[0].fill_between(x,0,pdf,color=color,alpha=.08)
    axes[1].plot(x,cdf,color=color,lw=2.2)
for ax in axes: ax.grid(color='#e4eaf0',lw=.8)
axes[0].set(ylabel='Densidade (1/m)',title='Alturas: dois modelos normais ilustrativos')
axes[0].legend(frameon=False,fontsize=9)
axes[1].set(xlabel='Altura (m)',ylabel='Probabilidade acumulada',ylim=(-.02,1.02))
fig.tight_layout()
save(fig,'alturas')
print('Figuras geradas em',OUT)

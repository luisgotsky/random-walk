import numpy as np
import matplotlib.pyplot as plt

def paso(l, d, p):
    
    return np.random.choice([l, d], p=[p, 1-p])

def paso2D(rl, p):
    
    l, r, u, d = rl
    
    lv, rv = [-l, 0], [r, 0]
    uv, dv = [0, u], [0, -d]
    desp = [lv, rv, uv, dv]
    
    return desp[int(np.random.choice([0, 1, 2, 3], p=p))]

def randomWalk(l, d, p, N):
    
    x = 0
    
    for i in range(N):
        
        x += paso(-l, d, p)
        
    return x

def randomWalk2D(rl, p, N):
    
    r = [0, 0]
    
    for i in range(N):
        
        r1 = paso2D(rl, p)
        r[0] += r1[0]
        r[1] += r1[1]
    
    return r

def buildHist(l, d, p, N, I, save=False):
    
    x = [randomWalk(l, d, p, N) for i in range(I)]
    media = np.mean(x)
    desv = np.std(x)
    
    fig = plt.figure(figsize=(9, 6))
    ax = plt.axes()
    ax.hist(x, density=True, align="right")
    ax.text(0.75, 0.9, "Media = " + str(round(media, 3)), transform=ax.transAxes)
    ax.text(0.75, 0.85, "$\\sigma = $" + str(round(desv, 3)), transform=ax.transAxes)
    ax.set_xlabel("X")
    ax.set_ylabel("P(X)")
    
    print("La media es: " + str(round(media, 3)))
    print("La desviación es: " + str(round(desv, 3)))
    
    if save:
        
        fig.savefig("Histograma1d.png", dpi=200)
    
def buildHist2D(rl, p, N, I, save=False):
    
    x, y = [], []
    
    for i in range(I):
        
        r = randomWalk2D(rl, p, N)
        x.append(r[0])
        y.append(r[1])
    
    fig = plt.figure(figsize=(9, 6))
    ax = plt.axes()
    ax.hist2d(x, y, density=True)
    
    if save:
        
        fig.savefig("Histograma2d.png", dpi=200)
    
def main():
    
    l = 1
    d = 1
    p = 0.9
    N = 1000
    I = 1000
    
    #buildHist(l, d, p, N, I, save=True)
    
    rl = [1, 0.5, 0.3, 1.2]
    p = [0.1, 0.3, 0.4, 0.2]
    
    buildHist2D(rl, p, N, I, save=True)
    
if __name__ == "__main__":
    
    main()
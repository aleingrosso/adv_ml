import numpy as np
import matplotlib.pyplot as plt

color_cycle = plt.rcParams['axes.prop_cycle'].by_key()['color']

# some function for plotting used in cds_ml/Lecture4.1
def plotting_utility(E, wrange, ws, losses, plot_contours = True, minimizer = None, label="w"):
    plt.figure(figsize=(12,4))
    
    plt.subplot(131)
    if minimizer is not None:
        plt.plot(minimizer[0], minimizer[1], 'x')
    plt.imshow(E, extent=[wrange[0], wrange[-1], wrange[0], wrange[-1]], cmap="coolwarm", alpha=0.3, origin="lower")
    if plot_contours:
        plt.contour(E, levels=[1,4,9], extent=[wrange[0], wrange[-1], wrange[0], wrange[-1]])
    plt.plot(ws[0,0], ws[0,1], 'o', color="black")
    plt.plot(ws[:,0], ws[:,1], '.-', ms=5, color="gray")
    plt.xlabel(f"${label}_1$")
    plt.ylabel(f"${label}_2$")
    
    plt.subplot(132)
    plt.plot(ws[:,0], '.-', ms=5, label=f"${label}_1$")
    plt.plot(ws[:,1], '.-', ms=5, label=f"${label}_2$")
    plt.ylabel(f'{label}')
    plt.xlabel('t')
    plt.legend();

    plt.subplot(133)
    plt.plot(losses, '.-', ms=5, label=f"${label}_1$")
    plt.ylabel('loss')
    plt.xlabel('t')
    plt.legend();

    plt.tight_layout();


def plot_points(X, t, ax, lim = 9, alpha = 1):
    ax.plot(X[t==1,0], X[t==1,1], 'x', color="black", alpha=alpha);
    ax.plot(X[t==0,0], X[t==0,1], 's', color="black", alpha=alpha);
    ax.hlines(y=0, xmin=-lim, xmax=lim, ls=':', color='gray')
    ax.vlines(x=0, ymin=-lim, ymax=lim, ls=':', color='gray')
    plt.gca().set_aspect('equal');


def plot_vec(w, fact=1, wlim = 10, label=None, color=None, alpha=0.5):
    plt.plot([0, w[0]*fact], [0, w[1]*fact], ls='--', alpha=alpha, color=color, label=label)
    plt.plot([-w[1]*fact, w[1]*fact], [w[0]*fact, -w[0]*fact], alpha=alpha, color=color);


def get_wgrid(wlim = 10, num = 100):
    wrange = np.linspace(-wlim, wlim, num)
    w1grid, w2grid = np.meshgrid(wrange, wrange)
    wgrid_stacked = np.dstack([w1grid, w2grid])
    return w1grid, w2grid, wgrid_stacked
"""Local plotting code."""

import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

####################################################################################################
####################################################################################################

def plot_autocorr(timepoints, autocorrs):
    """Plot autocorrelation results."""
    
    _, ax = plt.subplots(figsize=(6, 5))
    ax.plot(timepoints, autocorrs, color='k')
    ax.set(xlabel='Lag (Samples)', ylabel='Autocorrelation')

    ax.xaxis.set_tick_params(direction='out', length=5)
    ax.yaxis.set_tick_params(direction='out', length=5)

    plt.grid()


def plot_spectra_3D(freqs, powers, log_freqs=False, log_powers=True):
    """Plot a series of power spectra in a 3D plot."""
    
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    
    # Set background pane colors to white
    pane_color = (1.0, 1.0, 1.0, 1.0)
    plt.gca().xaxis.set_pane_color(pane_color)
    plt.gca().yaxis.set_pane_color(pane_color)
    plt.gca().zaxis.set_pane_color(pane_color)
    
    yticks = list(range(len(powers)))
    
    for cvals, yt in zip(powers, yticks):
        ax.plot(xs=freqs, ys=[yt] * len(freqs), zs=cvals)
    
    ax.set(
        
        # Labels
        xlabel='Frequency (Hz)',
        ylabel='Channels', 
        zlabel='Power',
        
        # Limits
        xlim=[min(freqs), max(freqs)],
        ylim=[0, max(yticks)],        
    )
    
    ax.set_yticks(yticks, yticks)
    
    # Set orientation
    ax.view_init(20, -50)    


## STYLE 

GS_FONT = fm.FontProperties(fname='/System/Library/Fonts/Supplemental/GillSans.ttc')

def plot_old_stylify(ax):
    """Apply an 'oldschool' style to a plot axis. 
    
    This function adapted from here:
    https://scipython.com/blog/old-style-matplotlib-charts/
    """
    
    ax.set_xlabel(ax.get_xlabel(), fontproperties=GS_FONT, fontsize=18)
    ax.set_ylabel(ax.get_ylabel(), fontproperties=GS_FONT, fontsize=18)

    for tick in ax.get_xticklabels():
        tick.set_fontname("Gill Sans")
        tick.set_fontsize(12)
    for tick in ax.get_yticklabels():
        tick.set_fontname("Gill Sans")
        tick.set_fontsize(12)

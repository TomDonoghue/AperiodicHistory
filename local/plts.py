"""Local plotting code."""

import warnings
from itertools import repeat, cycle

import numpy as np

import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

from neurodsp.plts.style import style_plot
from neurodsp.plts.utils import check_ax, savefig

####################################################################################################
####################################################################################################

@savefig
@style_plot
def plot_autocorr(times, acs, labels=None, colors=None, ax=None, **kwargs):
    """Plot autocorrelation results."""

    ax = check_ax(ax, figsize=kwargs.pop('figsize', (6, 5)))

    times, acs, labels, colors = _prep_multi_plot(times, acs, labels, colors)

    for time, ac, color, label in zip(times, acs, colors, labels):
        ax.plot(time, ac, color=color, label=label)

    ax.set(xlabel='Lag (Samples)', ylabel='Autocorrelation')


def plot_spectra_3D(freqs, powers, log_freqs=False, log_powers=True, colors=None, **kwargs):
    """Plot a series of power spectra in a 3D plot."""

    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    yticks = list(range(len(powers)))

    colors = repeat(colors) if not isinstance(colors, list) else cycle(colors)

    freqs = np.log10(freqs) if log_freqs else freqs

    for cvals, yt, color in zip(powers, yticks, colors):
        ax.plot(xs=freqs, ys=[yt] * len(freqs), zs=np.log10(cvals) if log_powers else cvals,
                color=color, **kwargs)

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

def plot_old_stylify(ax, label_fs=18, text_fs=12):
    """Apply an 'oldschool' style to a plot axis.

    This function adapted from here:
    https://scipython.com/blog/old-style-matplotlib-charts/
    """

    ax.set_xlabel(ax.get_xlabel(), fontproperties=GS_FONT, fontsize=label_fs)
    ax.set_ylabel(ax.get_ylabel(), fontproperties=GS_FONT, fontsize=label_fs)

    for tick in ax.get_xticklabels():
        tick.set_fontname("Gill Sans")
        tick.set_fontsize(text_fs)
    for tick in ax.get_yticklabels():
        tick.set_fontname("Gill Sans")
        tick.set_fontsize(text_fs)


def style_spectrum_plot(ax):
    """Style spectrum plot."""

    ax.xaxis.set_tick_params(direction='out', which='both', length=5)
    ax.yaxis.set_tick_params(direction='out', which='both', length=5)

    plt.minorticks_off()

    plt.grid(alpha=0.5)

    if len(ax.get_legend_handles_labels()[0]):
        plt.legend(loc=3, prop={'size': 15})

    plot_old_stylify(ax)


def style_autocorr_plot(ax):
    """Style autocorrelation plot."""

    ax.xaxis.set_tick_params(direction='out', length=5)
    ax.yaxis.set_tick_params(direction='out', length=5)

    plt.grid(alpha=0.5)

    if len(ax.get_legend_handles_labels()[0]):
        plt.legend(loc=1, prop={'size': 15})

    plot_old_stylify(ax)

    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        plt.tight_layout()


def style_3d_plot(ax):
    """Style 3D plot."""

    # Set background pane colors to white
    pane_color = (1.0, 1.0, 1.0, 1.0)
    ax.xaxis.set_pane_color(pane_color)
    ax.yaxis.set_pane_color(pane_color)
    ax.zaxis.set_pane_color(pane_color)

    plot_old_stylify(ax, 14, 8)

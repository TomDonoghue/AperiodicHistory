"""Local plotting code."""

import warnings

import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

####################################################################################################
####################################################################################################

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

    # If 3D plot, also update z-axis
    if hasattr(ax, 'get_zticklabels'):
        for tick in ax.get_zticklabels():
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

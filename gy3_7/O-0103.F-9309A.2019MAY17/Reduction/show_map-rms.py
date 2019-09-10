#!/usr/bin/env python
# coding: utf-8
''' show_rms.py
'''

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.interpolate import griddata
from sys import argv


def hist_bins(x):
    '''Estimate optimal number of bins for histogram based on pd.Series'''
    x_max = max(x)
    x_min = min(x)
    N_MIN = 4  # Minimum number of bins (integer)
    N_MAX = 100  # Maximum number of bins (integer)
    N = np.arange(N_MIN, N_MAX)
    D = (x_max - x_min) / N
    C = np.zeros(shape=(np.size(D), 1))
    C = np.zeros(np.size(D))

    # Computation of the cost function
    for i in range(np.size(N)):
        ki = np.histogram(x, bins=N[i])
        ki = ki[0]
        k = np.mean(ki)
        v = np.var(ki)
        C[i] = (2 * k - v) / (D[i]**2)

    # Optimal Bin Size Selection
    idx = np.argmin(C)
    optD = D[idx]
    return N[idx], optD


def show_rms(csv_file):
    '''Show rm histogram and map'''
    df = pd.read_csv(csv_file)
    """ py3:
    fig, (ax1, ax2) = plt.subplots(ncols=2,
                                   figsize=(9.6, 4.8),
                                   gridspec_kw={'width_ratios': [1, 2]})
    """
    fig = plt.figure(figsize=(9.6, 4.8))
    ax1 = plt.subplot(1, 3, 1)
    ax2 = plt.subplot(1, 3, (2, 3))
    fig.suptitle('Spectral (from baseline) noise distribution: ' +
                 csv_file.strip('_rms.csv'))
    df.rms.plot.hist(bins=hist_bins(df.rms)[0], ax=ax1, color='k', fc='k')
    ax1.set_xlabel('rms [mK/beam]')
    ax1.grid()
    ax1.axvline(df.rms.median(), lw=2, color='r', linestyle='--')
    ax1.text(0.95, 0.97, 'median rms:\n{:.1f} mK'.format(df.rms.median()),
             ha='right', va='top', transform = ax1.transAxes, color='r')
    nx = int(df.off_lambda.describe()[['min', 'max']].diff()[-1] / 10)
    ny = int(df.off_beta.describe()[['min', 'max']].diff()[-1] / 10)

    x_up = np.linspace(df.off_lambda.min(), df.off_lambda.max(), nx)
    y_up = np.linspace(df.off_beta.min(), df.off_beta.max(), ny)
    x3d, y3d = np.meshgrid(x_up, y_up)
    z3d = griddata((df.off_lambda, df.off_beta), df.rms,
                   (x3d, y3d), method="cubic")

    cbar1 = ax2.imshow(z3d, origin='lower',
                       extent=[df.off_lambda.min(), df.off_lambda.max(),
                               df.off_beta.min(), df.off_beta.max()])
    plt.gca().invert_xaxis()
    plt.xlabel('off_lambda [asec]')
    plt.ylabel('off_beta [asec]')
    cax = plt.colorbar(cbar1)
    cax.set_label('rms [mK/beam]')
    plt.tight_layout()
    plt.subplots_adjust(top=0.93, wspace=0.2)
    plt.savefig(csv_file.replace('.csv', '.png'), bbox_inches='tight')
    print('Figure saved to: ' + csv_file.replace('.csv', '.png'))
    return fig


def main(args=None):
    if args:
        fig = show_rms(args)
        plt.show(block=True)
    return fig


if __name__ == "__main__":
    fig = main(argv[1])

# Copyright (c) 2021, Anders Lervik.
# Distributed under the LGPLv2.1+ License. See LICENSE for more info.
"""
Elevation profiles - filled plots
=================================

This example will use the plotting methods of gpxplotter
to plot the elevation as a
function of distance and elapsed time.
"""
from matplotlib import pyplot as plt
from gpxplotter import read_gpx_file, plot_filled
plt.style.use('seaborn-talk')

for track in read_gpx_file('example1.gpx'):
    for i, segment in enumerate(track['segments']):
        # Plot elevation as function of distance:
        plot_filled(track, segment, xvar='Distance / km', yvar='elevation',
                    zvar='hr')
        # Plot elevation as function of elapsed time:
        plot_filled(track, segment, xvar='elapsed-time', yvar='elevation',
                    zvar='hr', cmap='plasma')
plt.show()

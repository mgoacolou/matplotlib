"""
===========
Broken Barh
===========

Make a "broken" horizontal bar plot, i.e., one with gaps
"""
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

start = datetime(2019, 9, 20, 10, 0, 0)

fig, ax = plt.subplots()
ax.broken_barh([(start+timedelta(seconds=110), timedelta(seconds=30)),
                (start+timedelta(seconds=150), timedelta(seconds=10))],
                (10, 9),
               facecolors='tab:blue')
ax.broken_barh([(start+timedelta(seconds=10), timedelta(seconds=50)),
                (start+timedelta(seconds=100), timedelta(seconds=20)),
                (start+timedelta(seconds=130), timedelta(seconds=10))],
               (20, 9),
               facecolors=('tab:orange', 'tab:green', 'tab:red'))
ax.set_ylim(5, 35)
ax.set_xlim(start, start+timedelta(seconds=200))
ax.set_xlabel('seconds since start')
ax.set_yticks([15, 25])
ax.set_yticklabels(['Bill', 'Jim'])
ax.grid(True)
ax.annotate('race interrupted', (start+timedelta(seconds=61), 25),
            xytext=(0.8, 0.9), textcoords='axes fraction',
            arrowprops=dict(facecolor='black', shrink=0.05),
            fontsize=16,
            horizontalalignment='right', verticalalignment='top')

plt.show()

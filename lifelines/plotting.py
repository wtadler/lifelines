#plotting

import matplotlib.pyplot as plt
import numpy as np


def plot_lifetimes(lifetimes, censorship = None, birthtimes=None, order=False):
    """

    lifetimes: an (nx1) numpy array of lifetimes. 
    censorship: an (nx1) numpy array of booleans: True if event observed, else False. 
    birthtimes: an (nx1) numpy array offsetting the births away from t=0. 


    Creates a lifetime plot, see 
    examples:

    """
    N = lifetimes.shape[0]
    if N>100:
      print "warning: you may want to subsample to less than 100 individuals."

    if censorship is None:
      censorship = np.ones(N, dtype=bool)

    if birthtimes is None:
      birthtimes = np.zeros(N)

    if order:
       """order by length of lifetimes; probably not very informative."""
       ix = np.argsort(lifetimes,0)
       lifetimes = lifetimes[ix,0]
       censorship = censorship[ix,0]
       birthtimes = birthtimes[ix]

    for i in range(N):
           c = "#A60628" if censorship[i] else "#348ABD"
           plt.hlines( N-1-i, birthtimes[i] , birthtimes[i] + lifetimes[i], color = c, lw=3)
           m = "|" if not censorship[i] else 'o'
           plt.scatter( (birthtimes[i]) + lifetimes[i] ,  N-1-i, color = c, s=30, marker = m)

    plt.ylim(-0.5, N)
    plt.show()

import pdb
def plot_dataframes(self, estimate):
    colors = [   "#348ABD",
                  "#A60628",
                  "#7A68A6",
                  "#467821",
                  "#CF4457",
                  "#188487",
                  "#E24A33"]
    def plot(color=colors, ignore_ci = False, **kwargs):
      """
      Plot the estimate and the confidence intervals.

      Parameters:
        color: an array of colors to cycle through
        ignore_ci: If true, do not plot the confidence intervals.
      """
      estimate_ = getattr(self, estimate)
      n,m = estimate_.shape
      pdb.set_trace()
      if n<=50:
         ax = estimate_.plot(color=colors[:m], marker='o', markeredgewidth=0, markersize=5, **kwargs)
      else:
         ax = estimate_.plot(color=colors[:m], **kwargs)
      #cycle through the conf. intervals
      if not ignore_ci:
        for i in range(0,m+2,2):
          col = self.confidence_interval_.columns[i:i+2]
          c_ = [color[i]]
          self.confidence_interval_[col].plot(color=c_, linestyle="--", ax=ax, **kwargs)

      return ax
    return plot


"""
	Simple tools to style an IPython Notebook.
	Author: htapia@lania.edu.mx (modified from Fernando Perez <fernando.perez@berkeley.edu>)
"""

#-----------------------------------------------------------------------------
# Imports
#-----------------------------------------------------------------------------

# stdlib
import os

# Third party
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# %matplotlib inline

# From IPython
from IPython.display import (HTML, Image, display, YouTubeVideo, Math,
                             Audio, clear_output, FileLinks)

from IPython.core.pylabtools import figsize

#-----------------------------------------------------------------------------
# Functions and classes
#-----------------------------------------------------------------------------

def prefix(url):
    prefix = '' if url.startswith('http') else 'http://'
    return prefix + url


def simple_link(url, name=None):
    name = url if name is None else name
    url = prefix(url)
    return '<a href="%s">%s</a>' % (url, name)


def html_link(url, name=None):
    return HTML(simple_link(url, name))


# Utility functions
def website(url, name='auto', width=800, height=450):
    html = []
    name = url if name == 'auto' else name
    if name:
        html.extend(['<div sytle="margin-bottom:10px">',
                     simple_link(url, name),
                     '</div>'] )

    html.append('<iframe src="%s"  width="%s" height="%s"></iframe>' % 
                (prefix(url), width, height))
    return HTML('\n'.join(html))


def nbviewer(url, name=None, width=800, height=450):
    return website('nbviewer.ipython.org/url/' + url, name, width, height)


def Video(fname):
    from IPython.display import HTML, display
    video = open(fname, "rb").read()
    video_encoded = video.encode("base64")
    video_tag = '''<video controls alt="test" src="data:video/x-m4v;base64,{0}">
    </video>'''.format(video_encoded)
    return HTML(data=video_tag)    

    
def plot_audio(fname):
    from scipy.io import wavfile
    rate, x = wavfile.read(fname)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))
    ax1.plot(x); ax1.set_title('Raw audio signal')
    ax2.specgram(x); ax2.set_title('Spectrogram');
    plt.show()

#loads a customer marplotlib configuration file
def CustomPlot():
    import json
    import matplotlib
    from IPython.core.pylabtools import figsize
    s = json.load( open("../../styles/matplotlibrc.json") )
    matplotlib.rcParams.update(s)
    figsize(18, 6) 
#-----------------------------------------------------------------------------
# Load and publish CSS
#-----------------------------------------------------------------------------
if __name__ == '__main__':
    display(HTML(open("../../styles/matstyle.css", "r").read()))

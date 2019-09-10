from django.shortcuts import render
from django.http import HttpResponse

# to avoid python crashing
import matplotlib
matplotlib.use('Agg')

from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np
from io import BytesIO

def index(request):
    return HttpResponse("Page Dashboard")

def graph(request):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    x = np.arange(-2,1.5,.01)
    y = np.sin(np.exp(2*x))
    ax.plot(x, y)

    FigureCanvasAgg(fig)

    buf = BytesIO()
    plt.savefig(buf, format='png')
    plt.close(fig)
    response = HttpResponse(buf.getvalue(), content_type='image/png')
    return response

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
import base64

def index(request):
    return render(request, 'dashboard/index.html')

def custom_graph(request):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    if request.method == "POST":
        x1 = request.POST["x1"]
        y1 = request.POST["y1"]
        x2 = request.POST["x2"]
        y2 = request.POST["y2"]
        x3 = request.POST["x3"]
        y3 = request.POST["y3"]
        plt.plot([int(x1), int(x2), int(x3)], [int(y1), int(y2), int(y3)], 'ro')
        plt.axis([0, 10, 0, 10])

    FigureCanvasAgg(fig)

    buf = BytesIO()
    plt.savefig(buf, format='png')
    plt.close(fig)
    response = HttpResponse(buf.getvalue(), content_type='image/png')
    return response


def graph(request):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    x = np.arange(-2,1.5,.01)
    y = np.sin(np.exp(2*x))
    ax.plot(x, y)

    FigureCanvasAgg(fig)

    buf = BytesIO()
    plt.savefig(buf, format='png', dpi=300)
    image_base64 = base64.b64encode(buf.getvalue()).decode('utf-8').replace('\n', '')
    plt.close(fig)
    #response = HttpResponse(buf.getvalue(), content_type='image/png')
    #return response
    return render(request, 'dashboard/graph.html', {'graph': image_base64})

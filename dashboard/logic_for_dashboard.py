"""

MongoDB

"""

import pymongo
from datetime import datetime, timedelta
from bson.json_util import dumps, loads
import time

# On définit le client comme étant le client local
client = pymongo.MongoClient()
# Le nom de la DB est "questions" (si elle n'existe pas elle est créée)
db = client["stats"]
sections = ["/dashboard", "/polls"]

def register_visit(request):
    date = datetime.now()
    print("currentDatetime:  ", date)
    page = request.path
    user_id = request.user.id
    visit = {'user_id': user_id,
            'date': date,
            'page': page }
    db["visits"].insert_one(visit)

def get_visits():
    visits = db["visits"].find().sort([("date", -1)]).limit(10)
    visits = loads(dumps(visits))
    return visits

def get_visits_by_sections():
    visits_by_sections = []
    for section in sections :
        visits = db["visits"].count({"page" : {'$regex' : '.*' + section + '.*'}})
        visits_by_sections.append({"section": section, "visits": visits})
    return visits_by_sections



def get_pages_for_section(section):
    pages = db["visits"].find({"page" : {'$regex' : '.*' + section + '.*'}}).distinct("page")
    return pages


def get_visits_by_pages(section):
    visits_by_pages = []
    pages = get_pages_for_section(section)
    for page in pages :
        visits = db["visits"].count({"page" : page})
        unique_visits = len(db['visits'].distinct("user_id", {"page" : page, "user_id": {"$ne": None }}))

        visits_by_pages.append({"page": page, "visits": visits, "unique_visits": unique_visits})
    return visits_by_pages


def get_visits_for_last_days(date, days):
    print("date: ", date)
    visits_for_last_days = []
    days = days

    while days >= 0:
        date_day = (date - timedelta(days=days))
        start_day = date_day.replace(hour=0, minute=0, second=0)
        end_day = date_day.replace(hour=23, minute=59, second=59)
        visits_for_day = db["visits"].count({"date" : {"$gte": start_day, "$lte": end_day}})
        visits_for_last_days.append({"day": date_day, "visits": visits_for_day})
        days -= 1

    visits_for_last_days = loads(dumps(visits_for_last_days))
    print(visits_for_last_days)
    return visits_for_last_days

"""

Matplotlib

"""

from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np
from io import BytesIO
import base64

def build_bar_chart(visits_object, title, ylabel, xticklabel, length, label1 = None, label2 = None):
    visits = []
    visits2 = []
    for visit_object in visits_object :
        visits.append(visit_object['visits'])
        if "unique_visits" in visit_object.keys():
            visits2.append(visit_object['unique_visits'])

    x = np.arange(len(length))  # the label locations
    width = 0.35

    fig, ax = plt.subplots()
    if len(visits2) :
        rects1 = ax.bar(x - width/2, visits, width, label = label1)
        rects2 = ax.bar(x + width/2, visits2, width, label = label2)
    else :
        rects1 = ax.bar(x, visits, width)

    ax.set_ylabel(ylabel)
    ax.set_title(title)
    ax.set_xticks(x)
    ax.set_xticklabels(xticklabel)
    ax.legend()

    autolabel(rects1, ax)
    if len(visits2) : autolabel(rects2, ax)

    fig.tight_layout()

    FigureCanvasAgg(fig)

    buf = BytesIO()
    plt.savefig(buf, format='png', dpi=300)
    image_base64 = base64.b64encode(buf.getvalue()).decode('utf-8').replace('\n', '')
    plt.close(fig)
    return image_base64


def autolabel(rects, ax):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


def build_graph(data):
    dates = []
    visits = []

    for object in data:
        dates.append(object["day"])
        visits.append(object["visits"])

    fig, axs = plt.subplots(1, 3, figsize=(9, 3), sharey=True)
    axs[0].bar(dates, visits)
    axs[1].scatter(dates, visits)
    axs[2].plot(dates, visits)
    fig.suptitle('Categorical Plotting')

    buf = BytesIO()
    plt.savefig(buf, format='png', dpi=300)
    image_base64 = base64.b64encode(buf.getvalue()).decode('utf-8').replace('\n', '')
    plt.close(fig)
    return image_base64

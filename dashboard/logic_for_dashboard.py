"""

MongoDB

"""

import pymongo
from datetime import datetime
from bson.json_util import dumps, loads

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
    visits = db["visits"].find()
    visits = loads(dumps(visits))
    return visits

def get_visits_by_sections():
    visits_by_sections = []
    for section in sections :
        visits = db["visits"].count({"page" : {'$regex' : '.*' + section + '.*'}})
        visits_by_sections.append({"section": section, "visits": visits})
    return visits_by_sections


def get_visits_by_pages(section):
    visits_by_pages = []
    pages = db["visits"].find({"page" : {'$regex' : '.*' + section + '.*'}}).distinct("page")

    for page in pages :
        visits = db["visits"].count({"page" : page})
        visits_by_pages.append({"page": page, "visits": visits})
    return visits_by_pages

"""

Matplotlib

"""

from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np
from io import BytesIO
import base64

def build_bar_chart():
    visits = []
    for visits_by_section in (get_visits_by_sections()) :
            visits.append(visits_by_section['visits'])

    x = np.arange(len(sections))  # the label locations
    width = 0.35

    fig, ax = plt.subplots()
    rects1 = ax.bar(x, visits, width)

    ax.set_ylabel('Visites')
    ax.set_title('Visites par sections')
    ax.set_xticks(x)
    ax.set_xticklabels(sections)
    ax.legend()

    fig.tight_layout()

    FigureCanvasAgg(fig)

    buf = BytesIO()
    plt.savefig(buf, format='png', dpi=300)
    image_base64 = base64.b64encode(buf.getvalue()).decode('utf-8').replace('\n', '')
    plt.close(fig)
    return image_base64

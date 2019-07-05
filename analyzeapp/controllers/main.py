from flask import Blueprint, render_template, flash, request, redirect, url_for, jsonify
from flask_login import login_user, logout_user, login_required

from analyzeapp.extensions import cache
from analyzeapp.forms import LoginForm, SelectForm
from analyzeapp.models import User, Recent, Setting
from analyzeapp import db

from werkzeug import secure_filename

import os
import os.path ,time
from datetime import datetime
import ntpath
import csv
from pandas import *

from math import ceil, floor
from statistics import stdev

from flask import jsonify

import json

main = Blueprint('main', __name__)

UPLOAD_PATH = "./uploads/"
EXPORT_PATH = "./exports/"
data_to = {
    "columns_meta" :[
        {
            "text": "timestamp",
            "col_idx": 0
        },
        {
            "text": "xlaccel1",
            "col_idx": 1
        },{
            "text": "xori1",
            "col_idx": 2
        },{
            "text": "xlaccel2",
            "col_idx": 3
        },{
            "text": "xori2",
            "col_idx": 4
        },{
            "text": "xlaccel3",
            "col_idx": 5
        },{
            "text": "xori3",
            "col_idx": 6
        },{
            "text": "xlaccel4",
            "col_idx": 7
        },{
            "text": "xori4",
            "col_idx": 8
        },{
            "text": "xlaccel5",
            "col_idx": 9
        },{
            "text": "xori5",
            "col_idx": 10
        },{
            "text": "ylaccel1",
            "col_idx": 11
        },{
            "text": "yori1",
            "col_idx": 12
        },{
            "text": "ylaccel2",
            "col_idx": 13
        },{
            "text": "yori2",
            "col_idx": 14
        },{
            "text": "ylaccel3",
            "col_idx": 15
        },{
            "text": "yori3",
            "col_idx": 16
        },{
            "text": "ylaccel4",
            "col_idx": 17
        },{
            "text": "yori4",
            "col_idx": 18
        },{
            "text": "ylaccel5",
            "col_idx": 19
        },{
            "text": "yori5",
            "col_idx": 20
        },{
            "text": "zlaccel1",
            "col_idx": 21
        },{
            "text": "zori1",
            "col_idx": 22
        },{
            "text": "zlaccel2",
            "col_idx": 23
        },{
            "text": "zori2",
            "col_idx": 24
        },{
            "text": "zlaccel3",
            "col_idx": 25
        },{
            "text": "zori3",
            "col_idx": 26
        },{
            "text": "zlaccel4",
            "col_idx": 27
        },{
            "text": "zori4",
            "col_idx": 28
        },{
            "text": "zlaccel5",
            "col_idx": 29
        },{
            "text": "zori5",
            "col_idx": 30
        }
    ]
}

new_data_to = {
    "columns_meta" :[
        {
            "text": "index",
            "col_idx": 0
        },
        {
            "text": "ch1",
            "col_idx": 1
        },{
            "text": "ch2",
            "col_idx": 2
        },{
            "text": "ch3",
            "col_idx": 3
        },{
            "text": "ch4",
            "col_idx": 4
        },{
            "text": "ch5",
            "col_idx": 5
        },{
            "text": "ch6",
            "col_idx": 6
        },{
            "text": "ch7",
            "col_idx": 7
        },{
            "text": "ch8",
            "col_idx": 8
        }
    ]
}

new_col = ["index", "ch1", "ch2", "ch3", "ch4", "ch5", "ch6", "ch7", "ch8"]

class DataFile:
    def __init__(self, file):
        self.data_cols = []
        self.file = file
        self.data_frame = None
        self.type = 0
        self.created = None
        self.name = ''
        self.status = True

        self.read()

    def read(self):
        self.data_frame = read_csv(self.file, skiprows=1)
        self.data_cols = []
        self.created = time.ctime(os.path.getmtime(self.file))
        self.name = ntpath.basename(self.file)
        if self.name.endswith("@.csv"):
            self.status = False
        try:
            for col in range(31):
                self.data_cols.append(self.data_frame[str(col)].tolist())
            self.data_frame = self.data_frame.set_index(str(0))
        except:
            self.type = 1
            self.data_frame = read_csv(self.file, skiprows=0)
            self.data_cols = []
            for col in range(9):
                self.data_cols.append(self.data_frame[new_col[col]].tolist())
            self.data_frame = self.data_frame.set_index(new_col[0])

data_dict = {

}

for root, dirs, files in os.walk(UPLOAD_PATH):
    for filename in files:
        if filename.endswith(".csv"):
            if not filename in data_dict:
                cur_file_path = os.path.join(UPLOAD_PATH, filename)
                data_dict[filename] = DataFile(cur_file_path)


@main.route('/')
@cache.cached(timeout=1000)
def home():
    loaded_counter = 0
    unloaded_counter = 0
    for val in data_dict.values():
        if val.status == True:
            loaded_counter += 1
        else:
            unloaded_counter += 1
    total_counter = loaded_counter+unloaded_counter

    settings = Setting.query.all()
    if len(settings) == 0:
        init_setting = Setting(5,True)
        db.session.add(init_setting)
        db.session.commit()

    recent_charts = Recent.query.all()
    print(recent_charts)
    recents = []
    recents_str = []
    for recent_chart in recent_charts:
        chart_json =json.loads(recent_chart.chart)
        recents.append(chart_json)
        recents_str.append(recent_chart.chart)
    print(recents)

    return render_template('index.html',recent_charts=recents,len=len(recents),recents_str = recents_str,total_counter = total_counter, loaded_counter = loaded_counter, unloaded_counter = unloaded_counter)

@main.route("/select", methods=["GET", "POST"])
def select():
    global data_dict
    data_dict = {}
    for root, dirs, files in os.walk(UPLOAD_PATH):
        for filename in files:
            if filename.endswith(".csv"):
                if not filename in data_dict:
                    cur_file_path = os.path.join(UPLOAD_PATH, filename)
                    data_dict[filename] = DataFile(cur_file_path)
    values = []
    for val in data_dict.values():
        values.append(val)
        
    return render_template("select.html",values=values)

@main.route("/upload", methods=["POST"])
def file_upload():
    uploaded_files = request.files.getlist("files[]")
    now = datetime.now()
    for f in uploaded_files:
        print(f.filename)
        if f.filename.endswith(".csv"):
            f.save(os.path.join(UPLOAD_PATH, ntpath.basename(f.filename)))
            date = datetime(year=now.year, month=now.month, day=now.day, hour=now.hour, minute=now.minute, second=now.second)
            modTime = time.mktime(date.timetuple())
            os.utime(os.path.join(UPLOAD_PATH, ntpath.basename(f.filename)), (modTime, modTime))            
    return redirect(url_for(".select"))

@main.route("/remove", methods=["GET"])
def remove_file():
    global data_dict
    file_name = request.args.get('fileName')
    print(UPLOAD_PATH+file_name)
    if os.path.exists(UPLOAD_PATH+file_name):
        os.remove(UPLOAD_PATH+file_name)
        data_dict = {}
        for root, dirs, files in os.walk(UPLOAD_PATH):
            for filename in files:
                if filename.endswith(".csv"):
                    if not filename in data_dict:
                        cur_file_path = os.path.join(UPLOAD_PATH, filename)
                        data_dict[filename] = DataFile(cur_file_path)
        return jsonify({
            "status": "success",
        })
    else:
        return jsonify({
            "status": "failed",
        })

@main.route("/unload", methods=["GET"])
def unload_file():
    global data_dict
    file_name = request.args.get('fileName')
    print(UPLOAD_PATH+file_name)
    if os.path.exists(UPLOAD_PATH+file_name):
        base_name, file_extension = os.path.splitext(file_name)
        if base_name.endswith('@'):
            os.rename(UPLOAD_PATH+file_name,UPLOAD_PATH+base_name[0:len(base_name)-1]+file_extension)
        else:
            os.rename(UPLOAD_PATH+file_name,UPLOAD_PATH+base_name+"@"+file_extension)
        
        data_dict = {}
        for root, dirs, files in os.walk(UPLOAD_PATH):
            for filename in files:
                if filename.endswith(".csv"):
                    if not filename in data_dict:
                        cur_file_path = os.path.join(UPLOAD_PATH, filename)
                        data_dict[filename] = DataFile(cur_file_path)
        return jsonify({
            "status": "success",
        })
    else:
        return jsonify({
            "status": "failed",
        })

@main.route("/settings", methods=["GET"])
def settings_page():
    settings = Setting.query.all()

    return render_template("settings.html",recent_number = settings[0].recent_num,reload_last = settings[0].reload_last)

@main.route("/change_setting", methods=["GET"])
def change_setting():
    recent_num = request.args.get("recent_num")
    checked = request.args.get("reload_last")
    reload_last = True
    if checked == 'false':
        reload_last = False

    settings = Setting.query.all()
    settings[0].recent_num = recent_num
    settings[0].reload_last = reload_last
    db.session.commit()

    return jsonify({
        "status": "success",
    })


@main.route("/analyze", methods=["GET"])
def analyze():
    global data_dict
    if not data_dict:
        return redirect(url_for(".select"))


    return render_template("analyze.html", values=data_dict.values(), files=list(data_dict.keys()), cols_meta=data_to, new_cols_meta=new_data_to)

@main.route("/saveRecent", methods=["GET"])
def save_recent():
    settings1 = Setting.query.all()
    recent_number = settings1[0].recent_num
    print("recent number :" + str(recent_number))

    recent_array = request.args.get("recents")
    recent_charts = Recent.query.all()
    if len(recent_charts) > recent_number:
        max_id = db.session.query(db.func.min(Recent.id)).scalar()
        Recent.query.filter_by(id=max_id).delete()

    print(recent_charts)
    flag = False
    for recent_chart in recent_charts:
        if recent_chart.chart == recent_array:
            flag = True
    if flag == False:
        recent = Recent(recent_array)
        db.session.add(recent)
        db.session.commit()


    return jsonify({
        "status": "success",
    })

@main.route("/getinfo", methods=["GET"])
def get_info():
    global data_dict

    file = request.args.get("file")
    xstart = floor(float(request.args.get("xstart")))
    xend = ceil(float(request.args.get("xend")))
    col_idx = int(request.args.get("col_idx"))

    data_cols = get_data_cols(file)
    data = data_cols[col_idx][xstart: xend+1]

    avg = sum(data) / len(data)
    cnt = 0
    for i in range(xstart + 1, xend):
        if (data_cols[col_idx][i] <= avg and data_cols[col_idx][i - 1] > avg) or (
                data_cols[col_idx][i] >= avg and data_cols[col_idx][i - 1] < avg):
            cnt += 1
    df = floor(cnt / 2) / (data_cols[0][xend-1] - data_cols[0][xstart])

    return jsonify({
        "stdev": round(stdev(data),3),
        "p2p": max(data) - min(data),
        "median": round(sum(data) / len(data), 3),
        "df": cnt/2,
        "xstart": int(xstart),
        "xend": int(xend)
    })

def get_data_cols(file):
    if not data_dict[file].data_cols:
        data_dict[file].read()
    return data_dict[file].data_cols

def get_data_frame(file):
    if not data_dict[file].data_cols:
        data_dict[file].read()
    return data_dict[file].data_frame


@main.route("/getdata", methods=["GET"])
def get_data():
    global data_dict

    file = request.args.get("file")
    col_idx = int(request.args.get("col_idx"))

    if file in data_dict:
        data = get_data_cols(file)[col_idx]

        return jsonify({
            "status": "success",
            "data": data
        })
    else:
        return jsonify({
            "status": "fail"
        })

@main.route("/exportdata", methods=["GET"])
def export_data():

    exportname = request.args.get("exportname")
    file = request.args.get("file")
    xstart = floor(float(request.args.get("xstart")))
    xend = ceil(float(request.args.get("xend")))
    col_idx = int(request.args.get("col_idx"))
    this_only = True if (request.args.get("this_only")) == "true" else False

    data_frame = get_data_frame(file)

    if this_only:
        data = data_frame[str(col_idx)][xstart: xend+1]
        path = os.path.join(EXPORT_PATH, exportname)
        data = data.reset_index()
        data = data.set_index(str(0))
        data.to_csv(path)
    else:
        data = data_frame[xstart: xend+1]
        path = os.path.join(EXPORT_PATH,exportname)
        data.to_csv(path)

    # flash("Successfully saved to " + path, "success")

    return jsonify({
        "status": "success",
        "file": path
    })


@main.route("/saveallselection", methods=["POST"])
def save_all_selection():
    global data_dict

    graphs = json.loads(request.form.get("graphs"))
    file_path = ""
    file_name = ""

    for i in range(1000):
        file_name = "allselection_" + str(i) + ".csv"
        file_path = os.path.join(EXPORT_PATH, file_name)
        if not os.path.exists(file_path):
            break

    with open(file_path, mode='w') as data_file:
        data_writer = csv.writer(data_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for graph in graphs:
            data_frame = get_data_frame(graph.get('file'))

            data = data_frame[str(graph.get('col'))][int(graph.get('xstart')): int(graph.get('xend'))+1]
            data = data.reset_index()
            data = data.set_index(str(0))
            
            col_name = data_to['columns_meta'][int(graph.get('col'))]['text']
            data_writer.writerow(["## " + col_name + " of " + graph.get('file')])
            data = data.reset_index()
            for row in data.values:
                data_writer.writerow([row[0], row[1]])
            data_writer.writerow([])

    return jsonify({
        "file_name": file_path,
        "status": "success"
    })

@main.route("/gettype", methods=["GET"])
def get_type():
    global data_dict

    return jsonify({
        "status": "success",
        "type": data_dict[request.args.get("file")].type
    })


# ---------------------------------------------------------------
@main.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).one()
        login_user(user)

        flash("Logged in successfully.", "success")
        return redirect(request.args.get("next") or url_for(".home"))

    return render_template("login.html", form=form)


@main.route("/logout")
def logout():
    logout_user()
    flash("You have been logged out.", "success")

    return redirect(url_for(".home"))


@main.route("/restricted")
@login_required
def restricted():
    return "You can only see this if you are logged in!", 200

from flask import Flask,render_template,redirect,url_for,flash
from incapsula.sparc_api import get_imperva_api , convert_utc_to_phtime,  write_log_file , purge_logs, capture_alert
from timeutils.timezones import print_diff_time
from automate.divert import Divert
from automate.forms.forms import DivertForm
from nornir.plugins.functions.text import print_result
from apscheduler.schedulers.background import BackgroundScheduler
import requests,json
import time
import os
import atexit
# from alert.detect_ddos import capture_alert, write_log_file, purge_logs

os.environ['TZ']= 'Asia/Manila'

app = Flask(__name__)
app.config['SECRET_KEY'] = '3134253qbueue5u5uyey44eytyney4yeby4'

@app.route("/")
def home():

    ddos_time = convert_utc_to_phtime(get_imperva_api()[1])

    return  render_template ("home.html", ddos_data=get_imperva_api()[0],
                             ddos_time=ddos_time, time_checked=get_imperva_api()[2],
                             table_data=get_imperva_api(), time_diff=print_diff_time(),ddos_alert=capture_alert())

@app.route("/divert", methods=['GET','POST'])
def divert():
    form = DivertForm()
    if form.validate_on_submit():
         user_divert = Divert(form.network.data, form.task.data)
         result = user_divert.nr.run(task=user_divert.advertise_to_incapsula)
         user_divert.nr.run(task=user_divert.clear_bgp)
         user_divert.nr.close_connections()

         hosts = user_divert.nr.inventory.hosts
         failed_host = result.failed_hosts.keys()

         for x in hosts:
             if x in failed_host:
                 flash(f"FAILED! {form.network.data} is not executed in {x}", 'danger')
             else:
                 flash(f"SUCCESS! {form.network.data} has been executed in {x}", 'success')
         return redirect(url_for('divert', form=form, result=result))

    return render_template('divert.html',title="DDOS", form=form, ddos_data=get_imperva_api()[0], time_diff=print_diff_time())


if __name__ == "__main__":
    sched = BackgroundScheduler(daemon=True)
    sched.add_job(get_imperva_api, 'interval',seconds=5, id='task1',max_instances=6)
    sched.add_job(print_diff_time,'interval',seconds=10, id='task2',max_instances=6)
    sched.add_job(write_log_file,'interval',seconds=5, id='task3',max_instances=6)
    sched.add_job(purge_logs,'interval',minutes=30,id='task4',max_instances=6)
    sched.add_job(capture_alert,'interval',seconds=5,id='task5',max_instances=6)
    sched.start()
    atexit.register(lambda: sched.shutdown())

    # app.run(debug=True, host="0.0.0.0", port=8090)
from apscheduler.schedulers.background import BackgroundScheduler
import requests , json
from pytz import timezone
from datetime import datetime
import datetime
from threading import local
from time import localtime
import pytz
from datetime import datetime, timedelta
import time
from automate.divert import Divert
import os
from incapsula.discordnotify import imperva_notify

def get_imperva_api():
    try:
        url = "https://my.imperva.com/api/v1/infra/events?/api_id=43504&api_key=b3b822ed-a5ab-44f7-bde1-029b0c223c10&event_type= DDOS_START_IP_RANGE&="
        payload={}
        headers = {
                    'x-API-Key': 'b3b822ed-a5ab-44f7-bde1-029b0c223c10',
                    'x-API-Id': '43504',
                    'Cookie': 'visid_incap_181=nt7W8dM3Qlyj93fNlMwpAfNAP2AAAAAAQkIPAAAAAAAZC92j6CsJB2319BIfznzd; nlbi_181_1249472=8AIfWGPu7krbzxvWNbRAWAAAAAD8/W466UztnrxCzygzVidW; incap_ses_430_181=39lgAlzQ7HmDjYSnBav3BYtzkmAAAAAAU1uUFun3yNXbRFRlvTPWLA==; nlbi_181_2147195=C4AhWZOj7VG+c6OlNbRAWAAAAACketnMGs6KocF2XXq0hXNM; incap_ses_796_181=BrtzZ+l+MFakGeaIEPYLCxt6kmAAAAAA9FSEXvye/Gyyf4P4A/Uu1w==; PLAY_ESESSION=7E%2F1Kz7VJ7t4%2FSbu5NzrtXFhd4nPEN9jNmJbYmFa%2Fj5U4r2acIG2VNtlxfy1woooeZ4BOzkec3X4YTM6tQk1Rg6boiiBbHg4SwKajlaHYUFRLGXb4BzaYg%3D%3D'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        result = response.text
        data = json.loads(result)

        # gathered data
        prev_time = (data["events"][1]["eventTime"])
        prev_target = (data["events"][1]["eventTarget"])
        all_data = data["events"]
        ddos_target = (data["events"][0]["eventTarget"])
        ddos_time = (data["events"][0]["eventTime"])
        time_stamp = print_date_time()
        # network_address = f"{ddos_target} last Attacked!"
        data_list = [ddos_target, ddos_time, time_stamp, all_data]
        return data_list
    except:
        pass

def convert_utc_to_phtime(pht):
    try:
        test = datetime.strptime(get_imperva_api()[1], '%Y-%m-%d %H:%M:%S UTC')
        test_utc = test.replace(tzinfo=timezone('UTC'))
        date_format='%A, %d. %B %Y %I:%M:%S %p'
        date = test_utc.astimezone(pytz.timezone('Asia/Manila'))
        pht = date.strftime(date_format)
        return pht
    except:
        pass

def print_date_time():
    current_time_stamp =  time.strftime("%A, %d. %B %Y %I:%M:%S %p")
    return current_time_stamp


def capture_alert():
    new_ddos = f"{get_imperva_api()[0]}-{get_imperva_api()[1].rstrip()}"
    # prev_ddos_target = f"{get_imperva_api()[4]}-{get_imperva_api()[5]}".rstrip()
    if new_ddos == new_ddos:
        return "Last Attack Details Below."
    else:
        imperva_notify(get_imperva_api()[0].replace("/24",""),get_imperva_api()[1].rstrip())
        return f"New DDOS Target Detected! See Details Below"

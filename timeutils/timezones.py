from incapsula.sparc_api import get_imperva_api, convert_utc_to_phtime
from datetime import datetime
import datetime
from threading import local
from time import localtime
from pytz import timezone
import pytz
from datetime import datetime, timedelta
import time

def print_diff_time():
    try:
        imperva_utc = convert_utc_to_phtime(get_imperva_api()[1])
        imperva_time = (datetime.strptime(imperva_utc, '%A, %d. %B %Y %I:%M:%S %p'))
        local_time = datetime.now().replace(microsecond=0)
        time_diff = local_time - imperva_time
        # secs = time_diff.total_seconds()
        # minutes = time_diff.total_seconds() / 60
        # hours = time_diff.total_seconds() / 60**2
        return time_diff
    except:
        pass

# def write_imperva_to_text():
#     with open("data/imperva.txt", 'a') as f:
#         detail = f"{imperva_api_call()[0]}-{imperva_api_call()[1]}"
#         f.write(f"{detail}\n")

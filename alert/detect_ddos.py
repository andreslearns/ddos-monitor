from incapsula.sparc_api import get_imperva_api
import os

def read_log_file():
    with open("data/imperva.log", "r") as f:
        return f.readlines()

def write_log_file():
    with open("data/imperva.log","a") as f:
        f.write(f"{get_imperva_api()[0]}-{get_imperva_api()[1].rstrip()}\n")

def capture_alert():
    new_ddos = f"{get_imperva_api()[0]}-{get_imperva_api()[1].rstrip()}"

    if new_ddos == read_log_file()[-1].rstrip():
        return "Relax! No Ongoing Attack."
    else:
         return "DDOS DETECTED! DIVERT NOW!!!"

def purge_logs():
    os.system("cat /dev/null > imperva.log")

from flask import Flask, jsonify, request, Response
import os
import json
from hashlib import sha256
from datetime import datetime, timezone, timedelta

app = Flask(__name__)

@app.route("/post")
def func():
    args = request.args
    deviceID = args.get('id')
    toSave = {}
    toSave['cpu_name'] = args.get('cpu_name')
    toSave['cpu_usage'] = args.get('cpu_usage')
    toSave['mem_min'] = args.get('mem_min')
    toSave['mem_max'] = args.get('mem_max')
    toSave['mem_used_mb'] = args.get('mem_used_mb')
    toSave['mem_used_percentage'] = args.get('mem_used_percentage')
    toSave['mem_free'] = args.get('mem_free')
    toSave['kernel'] = args.get('kernel')
    toSave['hostname'] = args.get('hostname')
    toSave['update_status'] = args.get('update_status')
    toSave['ip_addr'] = args.get('ip_addr')
    toSave['uptime'] = args.get('uptime')
    toSave['timestamp'] = args.get('timestamp')

    #Disks
    toSave['disks'] = []
    if deviceID == "0": #0 = laptop
        for i in range(0, 2):
            toSave['disks'].append({"name": args.get(f'disk{i}name'), "total_mb": args.get(f'disk{i}total_mb'), "use_percentage": args.get(f'disk{i}use_percentage'), "use_mb": args.get(f'disk{i}use_mb')})
        
        toSave['primary_disk'] = {
            "name": args.get('primary_disk_name'),
            "total_mb": args.get('primary_disk_total_mb'),
            "use_percentage": args.get('primary_disk_use_percentage'),
            "use_mb": args.get('primary_disk_use_mb')
        }

    with open(f'{deviceID}', 'w') as f:
        json.dump(toSave, f)
    return Response('ok', status=200)

@app.route("/")
def hello_world():
    """
    primaryDiskName='/dev/nvme0n1p2'
    diskAmount = 3

    toReturn = {}
    toReturn['cpu_name'] = os.popen("sshpass -pSander210404! ssh sander@desktop '/home/sander/monitoringscripts/cpu_name.sh'").read()[:-1]
    toReturn['cpu_usage'] = os.popen("sshpass -pSander210404! ssh sander@desktop '/home/sander/monitoringscripts/cpu_usage.sh'").read()[:-2]
    toReturn['mem_min'] = os.popen("sshpass -pSander210404! ssh sander@desktop '/home/sander/monitoringscripts/mem_min.sh'").read()[:-1]
    toReturn['mem_max'] = os.popen("sshpass -pSander210404! ssh sander@desktop '/home/sander/monitoringscripts/mem_max.sh'").read()[:-1]
    toReturn['mem_used_mb'] = os.popen("sshpass -pSander210404! ssh sander@desktop '/home/sander/monitoringscripts/mem_used_mb.sh'").read()[:-1]
    toReturn['mem_used_percentage'] = os.popen("sshpass -pSander210404! ssh sander@desktop '/home/sander/monitoringscripts/mem_used_percentage.sh'").read()[:-1]
    toReturn['mem_free'] = os.popen("sshpass -pSander210404! ssh sander@desktop '/home/sander/monitoringscripts/mem_free.sh'").read()[:-1]
    toReturn['primary_disk'] = {
        "name": primaryDiskName,
        "total_mb": os.popen("sshpass -pSander210404! ssh sander@desktop '/home/sander/monitoringscripts/primary_disk_total_mb.sh'").read()[:-1],
        "use_percentage": os.popen("sshpass -pSander210404! ssh sander@desktop '/home/sander/monitoringscripts/primary_disk_use_percentage.sh'").read()[:-2],
        "use_mb": os.popen("sshpass -pSander210404! ssh sander@desktop '/home/sander/monitoringscripts/primary_disk_use_mb.sh'").read()[:-1]
    }
    toReturn['disks'] = []
    for i in range(0,diskAmount):
        toReturn['disks'].append({"name": os.popen(f"sshpass -pSander210404! ssh sander@desktop '/home/sander/monitoringscripts/disk_name.sh {i+2}'").read()[:-1], "total_mb": os.popen(f"sshpass -pSander210404! ssh sander@desktop '/home/sander/monitoringscripts/disk_total_mb.sh {i+2}'").read()[:-1], "use_percentage": os.popen(f"sshpass -pSander210404! ssh sander@desktop '/home/sander/monitoringscripts/disk_use_percentage.sh {i+2}'").read()[:-2], "use_mb": os.popen(f"sshpass -pSander210404! ssh sander@desktop '/home/sander/monitoringscripts/disk_use_mb.sh {i+2}'").read()[:-1]})

    toReturn['kernel'] = os.popen("sshpass -pSander210404! ssh sander@desktop '/home/sander/monitoringscripts/kernel.sh'").read()[:-1]
    toReturn['hostname'] = os.popen("sshpass -pSander210404! ssh sander@desktop '/home/sander/monitoringscripts/hostname.sh'").read()[:-1]
    #toReturn['update_status'] = os.popen("sshpass -pSander210404! ssh sander@desktop '/home/sander/monitoringscripts/update_status.sh'").read()[:-1]
    toReturn['update_status'] = "no"
    toReturn['ip_addr'] = os.popen("sshpass -pSander210404! ssh sander@desktop '/home/sander/monitoringscripts/ip_addr.sh'").read()[:-1]
    toReturn['uptime'] = os.popen("sshpass -pSander210404! ssh sander@desktop '/home/sander/monitoringscripts/uptime.sh'").read()[:-1]
    toReturn['timestamp'] = datetime.now(timezone(timedelta(hours=2))).strftime("%H:%M:%S")
    return jsonify(toReturn)
    """

    args = request.args
    deviceID = args.get('deviceID')

    with open(f'{deviceID}', 'r') as f:
        data = json.load(f)
        return jsonify(data)
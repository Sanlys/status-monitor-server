from flask import Flask, jsonify, request, Response
import json

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
    args = request.args
    deviceID = args.get('deviceID')

    with open(f'{deviceID}', 'r') as f:
        data = json.load(f)
        return jsonify(data)
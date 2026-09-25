from fastapi import FastAPI, HTTPException

app = FastAPI()

readings = [
    {"name": "front-door", "room": "hall",    "temp": 27.4, "online": True},
    {"name": "hall-lamp",  "room": "hall",    "temp": 26.1, "online": True},
    {"name": "attic",      "room": "attic",   "temp": 31.9, "online": True},
    {"name": "fridge",     "room": "kitchen", "temp": 4.2,  "online": False},
    {"name": "patio",      "room": "outside", "temp": 29.8, "online": True},
]

def hottest(devices):
    hottest_device = devices[0]
    for device in devices:
        if device["temp"] > hottest_device["temp"]:
            hottest_device = device
    return hottest_device

def average_temp(devices):
    total = 0
    for device in devices:
        total += device["temp"]
    return total / len(devices)



    @app.get("/devices")
def get_devices():
    return readings

@app.get("/devices/hottest")
def get_hottest():
    return hottest(readings)

@app.get("/devices/online")
def get_online():
    online_devices = []
    for device in readings:
        if device["online"]:
            online_devices.append(device)
    return online_devices




@app.get("/devices/{name}")
def get_device(name: str):
    for device in readings:
        if device["name"] == name:
            return device
    raise HTTPException(status_code=404, detail="No device called " + name)
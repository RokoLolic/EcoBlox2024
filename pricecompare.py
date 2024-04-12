import time
import requests
import json
import datetime

UpperLimit = 0.05 #How much percentage increase compared to before
DownLimit = 0.05 #How much percentage decrease compared to before
NoChangeLimit = 0.01 #maximum change needed to declare that change is irrelevant

CurrentTime = int(time.time())
CurrentTime = (CurrentTime//3600) * 3600000
PastTime = CurrentTime - 7200000
print(CurrentTime, PastTime)

urlBitcoin = f"https://api.coincap.io/v2/assets/bitcoin/history?interval=m1&start={PastTime}&end={CurrentTime+1000}"

payload = {}
headers = {}

response = requests.request("GET", urlBitcoin, headers=headers, data=payload)

JsonBitcoin = response.json()
SumPrice = 0;
PoitsOfMeasure = len(JsonBitcoin["data"])
for i in range(PoitsOfMeasure):
    SumPrice += float(JsonBitcoin["data"][i]["priceUsd"])
average = SumPrice/PoitsOfMeasure
print(average)
PriceAtEnd = float(JsonBitcoin["data"][PoitsOfMeasure-1]["priceUsd"])
print(PriceAtEnd/average-1)

urlGovee = "https://openapi.api.govee.com/router/api/v1/device/control"
RelativeChange = PriceAtEnd/average-1
if (RelativeChange >UpperLimit):
    RGBSegment = 65280
    BrightnessSegment = 100
elif (NoChangeLimit<= RelativeChange <= UpperLimit ):
    RGBSegment = 65280
    BrightnessSegment = 50
elif (-NoChangeLimit < RelativeChange <= NoChangeLimit):
    RGBSegment = 16776960
    BrightnessSegment = 100
elif (-DownLimit <= RelativeChange <= -NoChangeLimit):
    RGBSegment = 16711680
    BrightnessSegment = 100
else:
    RGBSegment = 16711680
    BrightnessSegment = 100

dt = datetime.datetime.fromtimestamp(CurrentTime/1000)
print(dt.hour)
if (dt.hour == 22):
    ChosenSegment = 0
else:
    ChosenSegment = int(dt.hour/2 +1)
payload = json.dumps({
  "requestId": "uuid",
  "payload": {
    "sku": "H61A5",
    "device": "EF:C2:38:30:34:16:59:FF",
    "capability": {
      "type": "devices.capabilities.segment_color_setting",
      "instance": "segmentedColorRgb",
      "value": {
        "segment": [ChosenSegment],
        "rgb": RGBSegment
      }
    }
  }
})
headers = {
  'Content-Type': 'application/json',
  'Govee-API-Key': 'db7e93a6-ec0d-468f-bc24-449793e3d44f'
}

response = requests.request("POST", urlGovee, headers=headers, data=payload)

#print(response.text)


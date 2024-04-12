import requests

#BrightnessSegment = [0]*12
#ColorSegment = [0]*12

#Day = 1712779200000 # 22 your time, 20 utc
#CurrentTime = 1712836800000 # 14 your time, 12 utc

def AverageSegments(Day, CurrentTime):
    TwoHours = 7200000
    AveragePrices = [0]*12
    url = f"https://api.coincap.io/v2/assets/bitcoin/history?interval=m1&start={Day}&end={CurrentTime+1000}"
    print(url)
    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    JsonBitcoin = response.json()
    #print(JsonBitcoin["data"][0])


    SegmentsActive = (CurrentTime - Day)//TwoHours
    print(SegmentsActive, len(JsonBitcoin["data"]))
    for segment in range(SegmentsActive):
        SumPrice = 0;
        #CurrentPeriodStart = 1712779200000 + segment * TwoHours
        #print(CurrentPeriodStart)
        #CurrentPeriodEnd = 1712779200000 + segment * (TwoHours) + TwoHours
        #print(CurrentPeriodEnd)
        #print(JsonBitcoin["data"][segment*120])
        #print(JsonBitcoin["data"][segment*120+120])
        for i in range(120):
            #if ( len(JsonBitcoin["data"]) > segment*120+i):
            #    print(segment, i)
            SumPrice += float(JsonBitcoin["data"][segment*120+i]["priceUsd"])
        
        average = SumPrice/120
        AveragePrices[segment] = average
    
    return AveragePrices

        #print(JsonBitcoin["data"].index(CurrentPeriodStart))
        #print(JsonBitcoin["data"].index(CurrentPeriodEnd))

        #PoitsOfMeasure = len(JsonBitcoin["data"])
        #for i in range(PoitsOfMeasure):
        #    SumPrice += float(JsonBitcoin["data"][i]["priceUsd"])
        #average = SumPrice/PoitsOfMeasure
        #print(average)

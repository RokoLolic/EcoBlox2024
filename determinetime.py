import time

CurrentTime = int(time.time())
CurrentDay = (CurrentTime // 86400) * 86400000 - 7200000
CurrentTwoHour = (CurrentTime // 7200) * 7200000

print(CurrentDay, CurrentTwoHour)

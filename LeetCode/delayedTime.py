def findDelayedArrivalTime(arrivalTime, delayedTime):
    return (arrivalTime+delayedTime) % 24



at = 15
dt = 5
print(findDelayedArrivalTime(at,dt))

at = 13
dt = 11
print(findDelayedArrivalTime(at,dt))
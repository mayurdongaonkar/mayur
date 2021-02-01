distance = [1,2,3,4] 
start = 0
destination = 3
###distance[i] = i and (i + 1) % n

def distancebtwnstops(distance : list, start : int, destination : int) -> int:
    clockwise_sum = 0
    anti_clockwise_sum = 0

    for i in range(start,destination):
        clockwise_sum += distance[i]
    
    anti_clockwise_sum = sum(distance) - clockwise_sum

    return min(clockwise_sum,anti_clockwise_sum)

print(distancebtwnstops(distance,start,destination))
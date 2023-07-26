'''
Until we reach the end of the road, do:

If there is no traffic light at the current position, increase the position and time by 1.
If there is a traffic light that is green, also increase the position and time by 1.
If there is a traffic light that is red, increase the time by 1.
What remains is to determine the light at a traffic light at a given time index T. If T starts from zero, then a traffic light is red when Tmod(R+G)<R, and green otherwise.
'''


N, L = list(map(int, input().split(" ")))

Distance = 0
Overall_time = 0

for i in range(N):
    D, R, G = list(map(int, input().split(" ")))
    Overall_time += D - Distance
    Distance = D
    while (Overall_time % (R + G) < R):
        Overall_time += 1

Overall_time += L - Distance
Distance = L

print(Overall_time)
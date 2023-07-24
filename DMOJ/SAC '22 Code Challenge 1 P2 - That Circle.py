import math

L, H, W = list(map(int, input().split()))
D = int(input())
R = D/2

volume_rect = L*H*W
volume_cy = H*(math.pi*R**2)
print('{0:.2f}'.format(volume_rect-volume_cy))
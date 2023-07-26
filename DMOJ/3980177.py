from collections import Counter
n = int(input())
markers = input().split()
count_markers = Counter(markers)
print(min(n, (n-count_markers.most_common()[0][1])*2+1))
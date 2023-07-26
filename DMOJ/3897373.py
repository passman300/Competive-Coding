def h_index(list1):
    h = len(list1)
    while h > 0 and list1[h - 1] < h:
        h -= 1
    return h

n_l = input().split(" ")
n = int(n_l[0])
l = int(n_l[1])

papers = []
papers_input = input().split(" ")
for i in range(n):
    papers.append(int(papers_input[i]))

papers.sort(reverse=True)

h = h_index(papers)
if h != n:
    for j in range(h, -1, -1):
        if j > h - l:
            papers[j] += 1

papers.sort(reverse=True)

print(h_index(papers))
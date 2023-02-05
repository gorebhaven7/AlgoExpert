from collections import defaultdict
def tournamentWinner(competitions, results):
    # Write your code here.
    hm = defaultdict(int)
    maxx = float('-inf')
    for i in range(len(results)):
        home,away = competitions[i][0], competitions[i][1]
        print(home,away)
        if home not in hm:
            hm[home] = 0
        elif away not in hm:
            hm[away] = 0

        if results[i] == 0:
            hm[away] += 3
            if hm[away] > maxx:
                maxx = hm[away]
        else:
            hm[home] += 3
            if hm[home] > maxx:
                maxx = hm[home]
    # print(hm,maxx)
    for k,v in hm.items():
        if v == maxx:
            return k



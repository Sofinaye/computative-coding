def findWinners(self, matches):
    winner = {}
    losser = {}
    win = []
    loss = []
    for i in range(len(matches)):
        winner[matches[i][0]] = winner.get(matches[i][0], 0) + 1
        losser[matches[i][1]] = losser.get(matches[i][1], 0) + 1
    for j in winner:
        if j not in losser:
            win.append(j)
    for k in losser:
        if losser[k] == 1:
            loss.append(k)
    return [sorted(win), sorted(loss)]

# -*- coding: utf-8 -*-

class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def __repr__(self):
        return 'Point(name=%s, score=%s)' % (self.name, self.score)
    def comparator(a,b):
        if a.score > b.score:
            return b.score
        else:
            return a.score
            
n = int(raw_input())
data = []
for i in range(n):
    name, score = raw_input().split()
    score = int(score)
    player = Player(name, score)
    data.append(player)
    
data = sorted(data, )
for i in data:
    print i.name, i.score
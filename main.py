# -*- coding:UTF-8 -*-
import sys
sys.path.append("cars")
sys.path.append("data");
sys.path.append("map");
sys.path.append("tools");
import dev as devs
import move as moves
import distance as distances
import steering as steerings

dev=devs.Dev()
move=moves.Move(dev)
turn=steerings.Steering(dev)
dist=distances.Distance(dev)

if __name__ == "__main__":
    print 'main begin new'
    while True:
        for i in range(0,181,10):
            turn.Todo(i)
            distValue=dist.GetDistance()
            print distValue

        move.Todo(t.FORWARD,1)


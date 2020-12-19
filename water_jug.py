def put(jug1, jug2):
    max1, max2, fill = 3, 5, 4
    print("%d\t%d" % (jug1, jug2))
    if jug2 is fill:
        return
    elif jug2 is max2:
        put(0, jug1)
    elif jug1 != 0 and jug2 is 0:
        put(0, jug1)
    elif jug1 is fill:
        put(jug1, 0)
    elif jug1 < max1:
        put(max1, jug2)
    elif jug1 < (max2-jug2):
        put(0, (jug1+jug2))
    else:
        put(jug1-(max2-jug2), (max2-jug2)+jug2)
print("<---solution of Water jug problem BFS--->") 
print("|JUG:1|\t|JUG:2")

put(0, 0)


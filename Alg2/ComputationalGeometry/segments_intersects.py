def direction(Pi, Pj, Pk):
    r1 = (Pj[0] - Pi[0], Pj[1] - Pi[1])
    r2 = (Pk[0] - Pi[0], Pk[1] - Pi[1])
    return (r1[0] * r2[1]) - (r1[1] * r2[0])

def on_segment(Pi, Pj, Pk):
    if(min(Pi[0], Pj[0]) <= Pk[0] and Pk[0] <= max(Pi[0], Pj[0])) and (min(Pi[1], Pj[1]) <= Pk[1] and Pk[1] <= max(Pi[1], Pj[1])):
        return True
    else:
        return False

def segments_intersect(p1, p2, p3, p4):
    d1 = direction(p3, p4, p1)
    d2 = direction(p3, p4, p2)
    d3 = direction(p1, p2, p3)
    d4 = direction(p1, p2, p4)

    if((d1 > 0 and d2 < 0) or (d1 < 0 and d2 > 0)) and ((d3 > 0 and d4 < 0) or (d3 < 0 and d4 > 0)):
        return True
    else if d1 == 0 and on_segment(p3, p4, p1):
        return True
    else if d2 == 0 and on_segment(p3, p4, p2):
        return True
    else if d3 == 0 and on_segment(p1, p2, p3):
        return True
    else if d4 == 0 and on_segment(p1, p2, p4):
        return True
    else:
        return False


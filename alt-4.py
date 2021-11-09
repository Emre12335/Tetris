coor = (9.5, 4.5)


class rr:
    def __init__(self,difx, dify):
        self.difx = difx
        self.dify = dify


a1 = rr(-0.5, 0.5)
a2 = rr(-0.5, -1.5)
a3 = rr(-0.5, -0.5)
a4 = rr(-0.5, 1.5)
li = [a1, a2, a3, a4]
max_x = 0
min_x = 0
for m in li:
    if coor[0] - m.dify < 0 and coor[0] - m.dify < min_x:
        min_x = coor[0] - m.dify
    elif coor[0] - m.dify > 9 and coor[0] - m.dify - 9 > max_x:
        max_x = (coor[0] - m.dify) - 9 # one of these should give 2.0 and max_x should be 2.0 but every time it is 1.0
print(f"max_x = {max_x},min_x = {min_x}")

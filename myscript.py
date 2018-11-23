import c1

C = c1.myClass([1,2,3,4,5], [1,0,1])

C.insertX(6)
C.insertY(5)

print("X: {} len:{}".format(C.getX(),C.lenX()))
print("Y: {} len:{}".format(C.getY(),C.lenY()))

x = 4
y = -4
print(f"{x}")
print(f"{y}")
if y>0 and x<0:
    print(f"Point P({x},{y}) is in the first quadrant of the coordinate system")
if y>0 and x>0:
    print(f"Point P({x},{y}) is in the second quadrant of the coordinate system")
if y<0 and x<0:
    print(f"Point P({x},{y}) is in the third quadrant of the coordinate system")
if y<0 and x>0:
    print(f"Point P({x},{y}) is in the fourth quadrant of the coordinate system")    
if y==0 and x==0:
    print(f"Point P({x},{y}) is in the {x},{y} of the coordinate system")
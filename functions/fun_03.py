# Cube of a number
def cube(n=4):
    print(n * n * n)

# Compare two characters
def compare(lt1, lt2):
    if lt1 == lt2:
        return True
    else:
        return False

print("cube() =>")
cube()

print("cube(10) =>")
cube(10)

print("compare('a', 'b') :", compare('a', 'b'))
print("compare('a', 'a') :", compare('a', 'a'))
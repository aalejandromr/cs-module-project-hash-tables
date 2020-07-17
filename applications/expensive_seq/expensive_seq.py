# Your code here

cache = {}

def exps(x, y, z):
     if x <= 0:
        return y + z
     if x >  0:
        return exps(x-1,y+1,z) + exps(x-2,y+2,z*2) + exps(x-3,y+3,z*3)

def expensive_seq(x, y, z):
    # Your code here
    # print(f"Cache: {cache}")
    if x <= 0:
        return y + z

    if x >  0:
        x_from_cache, y_from_cache, z_from_cache = 0, 0, 0
        # print(f"is {(x-1,y+1,z)} in {cache}?")
        if (x-1,y+1,z) not in cache:
            cache[(x-1,y+1,z)] = expensive_seq(x-1,y+1,z)

        if (x-2,y+2,z*2) not in cache:
            cache[(x-2,y+2,z*2)] = expensive_seq(x-2,y+2,z*2)

        if (x-3,y+3,z*3) not in cache:
            cache[(x-3,y+3,z*3)] = expensive_seq(x-3,y+3,z*3)

        return cache[(x-1,y+1,z)] + cache[(x-2,y+2,z*2)] + cache[(x-3,y+3,z*3)]

if __name__ == "__main__":
    for i in range(10):
        x = exps(i*2, i*3, i*4)
        print(f"{i*2} {i*3} {i*4} = {x}")

    print("\n")

    for i in range(10):
        x = expensive_seq(i*2, i*3, i*4)
        print(f"{i*2} {i*3} {i*4} = {x}")

    # print(expensive_seq(150, 400, 800))

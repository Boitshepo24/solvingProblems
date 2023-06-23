def greatest_cd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

def find_lowestcm():
   
    lcm = 1
    for i in range(2, 11):
        lcm = (lcm * i) // greatest_cd(lcm, i)

    return lcm


lcm = find_lowestcm()
print(lcm) 


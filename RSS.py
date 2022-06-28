def test_function(w,x,y,z,counter):
    sum = w + x + y + z
    if(w >= 90 or x >= 90):
        sum += 10
    if(y <= 30 and z <= 30):
        sum -= 5
    print('id:%d:w=%d,x=%d,y=%d,z=%d. sum: %d '%(counter,w,x,y,z,sum))
    
def test_cases_generator():
    counter = 0
    groupA = [100,90,80]
    groupB = [40,30,20]
    for w in groupA:
        for x in groupA:
            for y in groupB:
                for z in groupB:
                    counter += 1
                    test_function(w,x,y,z,counter)
def test(a,b):
    num = 0.0023688
    print(a*b/num)
if __name__ == '__main__':
    #test_cases_generator()
    test(0.018,0.08)
    test(0.00288,0.5)
    test(0.018,0.0396)
    test(0.00216,0.33)
    test(0.0108,0.02)
    test(0.000864,0.25)



    

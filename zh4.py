def shui1 ():
    for i in range (1000,10000):
        s = str(i)
        qian = int (s[0])
        bai = int (s[1])
        shi = int (s[2])
        ge = int (s[3])
        if  i == qian **4 +bai **4 +shi **4 +ge **4:
          print (i)  
def shui2 ():
    for i in range (100,1000):
        s = str(i)
        bai = int (s[0])
        shi = int (s[1])
        ge = int (s[2])
        if  i == bai **3 +shi **3 +ge **3:
          print (i)   

shui1()

shui2()

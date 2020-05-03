#tempconvert
while (True):
    degree = input ("Please input a degree with a mark in Celsius or Farenhait,eg. 36C or 45F: ")
    if degree [-1] in ('C','c'):
        Farenhait = int(degree [0:-1])*1.8+32
        print("The temperature converted into Farenhait is %.2fF" %Farenhait)
    elif degree [-1] in ('F','f'):
        Celsius = int(degree [0:-1])/1.8-32
        print ("The temperature converted into Celsius is %.2fC" %Celsius)
    else:
         print ("The degree is in wrong format.Please try again.")
    print ('''********************
********************''')


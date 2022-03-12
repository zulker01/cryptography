# -*- coding: utf-8 -*-
"""

log1 : removed mod () from xor string

Name : Zulker Nayeen
Roll : FH-11

This assignment does add , sub, mult , div on polynomials withing galois field.
input polynomials as bit stream  
"""


import itertools

# compares 2 binary string , by converting them to int, 
# if 1st is big then retunr 1, 2nd big return -1 , same if zero
def compare2values(str1,str2):
    
    #print(type(str1))
    #print(type(str2))
    #print("first: "+str(int(str1,2)))
    #print("2nd: "+str(int(str2,2)))
    # if dividend out of bound of 256
    if int(str1,2)>255:
        return 1
    if int(str1,2)>int(str2,2):
        
        return 1
    elif int(str1,2)<int(str2,2):
        return -1
    else:
        return 0
        


# divide str1 / str2 1
"""
1001 ) 101011 ( 100 -> ans
       100100 -> tmp divi
      ----------
               -> divi new
"""

# function to get mod / reminder
def mod(moddivi,moddivisor):
    modans = 0b00 # ans after mod opertation / reminder
    i = 1
    #print("ans = "+str(modans)+" divisor = "+moddivisor+ " dividend = "+moddivi)
    # if divisor is already big , return ans
    if compare2values(moddivi, moddivisor)==-1:
        #print("return do nothing ans = "+str(modans)+" divisor = "+moddivisor+ " dividend = "+moddivi)
        return moddivi
    while(compare2values(moddivi, moddivisor)!=-1):
        # if both string has same len, then div ans append 1
        # and direct mod with the divisor & dividend , 
        #print("ans = "+str(modans)+" divisor = "+moddivisor+ " dividend = "+moddivi)
        if len(moddivi)==len(moddivisor):
            
            tmpmodans=0b1
            modans = tmpmodans+modans
            moddivi = xorStrings(moddivi,moddivisor)
            #print("inside if : tmpans = "+str(tmpmodans)+" divi= "+moddivi+" ans = "+str(modans))
        else:
            # if dividend is greater , means it has higher power, so have to multiply,
            # that's why left shift to get tmp dividend, then xor
            tmpmodans = 0b1<<(len(moddivi)-len(moddivisor))
            
            tmpmoddivi = leftShift(moddivisor,(len(moddivi)-len(moddivisor)))
            moddivi = xorStrings(tmpmoddivi, moddivi) # new divisor
            modans = tmpmodans+modans
            #print("inside else : tmpans = "+str(tmpmodans)+" tmpdivi = "+str(int(tmpmoddivi,2))+" divi= "+str(int(moddivi,2))+" ans = "+str(modans))
            
        
        
            
        
    #print("ans = "+str(modans)+" divisor = "+moddivisor+ " dividend = "+moddivi)       
        
    return moddivi
    


# this funciton xors 2 binary strings

def xorStrings(str1,str2):
    ans = ""
    # make the the string same len 
    if len(str1)<len(str2):
        for i in range(len(str2)-len(str1)):
            str1 = "0"+str1
            
    elif len(str1)>len(str2):
        for i in range(len(str1)-len(str2)):
            str2 = "0"+str2
    for i in range(len(str2)-1,-1,-1):
    
        if str2[i]==str1[i]:
           ans="0"+ans
        else:
            ans="1"+ans
    if len(ans)==0:
        return "0"
    # delete the extra zeros from front
    while(ans[0]=="0"):
            
        ans = ans[1:]
        if(len(ans)==1):
                break
    return ans

# left shift string
def leftShift(str1,cnt):
    ans = "".join(["0" for i in range(cnt)] )
    return str1+ans 

# multiply strings of binary
def multiply(str1,str2):
    """
    str1
    *str2
    
    101
   *011
   
   -----
   101
  101
 000
    """
    j=0
    # initial ans = 0000000 
    ans = "".join(["0" for i in range(len(str2))] )
    # loop from last to first, if 1 then, left shift & xor, else do nothing
    
    for i in range(len(str2)-1,-1,-1):
       if str2[i]=="1":
           ans = xorStrings(ans, leftShift(str1,j))
       j+=1

    #print("multiply ans : "+ans)   
    return mod(ans,irrpoly)

# divide the 2 binary strings
def division(dividend,divisor):
    
    if len(divisor)<8:
        tmpstr = ""
        for i in range(8-len(divisor)):
            tmpstr+="0"
        divisor = tmpstr+divisor
    # get the multiplicative inverse, then multiply them & mod
    mulInverseofDivisor = multInverseDict[divisor]
    return multiply(dividend, mulInverseofDivisor)
    
def getAllPossible8bitString():
    
    # possible bit for every position
    possiblebit = ["01","01","01","01","01","01","01","01"]
    
    global allpossibleBitString
    allpossibleBitString=[]
    
    # get all possible binary  list
    for element in itertools.product(*possiblebit):
        currentBin = "".join(element)
        
        allpossibleBitString.append(currentBin)
        
    print(" all p ossible Len "+str(len(allpossibleBitString)))
    
def calculateMulInverse():
    global multInverseDict
    multInverseDict = {}
    for i in range(256):
        #if i>3: break
        for j in range(256):
            # if we got its mod inverse, continue
            if allpossibleBitString[i] in multInverseDict:
                continue
            multAns = multiply(allpossibleBitString[i], allpossibleBitString[j])
            #print(multAns+" int : "+str(int(multAns,2)))
            #if j>4: break
            if int(multAns,2)==1:
                multInverseDict[allpossibleBitString[i]] = allpossibleBitString[j]
                multInverseDict[allpossibleBitString[j]] = allpossibleBitString[i]
                #print("inverse found : "+allpossibleBitString[i]+ "   ->   "+allpossibleBitString[j])
    #print("multinver : "+str(len(multInverseDict)))            
        
# this function starts appropriate operation

def getAns(input1,input2, operationInput):
    
    if operationInput=="+" or operationInput=="-":
        return xorStrings(input1,input2)
    
    if operationInput=="*":
        return multiply(input1,input2)
    if operationInput=="/":
        return division(input1, input2)
    else:
        
        return "!!!!!!!!!! invalid operation !!!!!!! try again"
    
# check if string is valid binary
def check(string) :
 
    # set function convert string
    # into set of characters .
    p = set(string)
 
    # declare set of '0', '1' .
    s = {'0', '1'}
 
    
    if s == p or p == {'0'} or p == {'1'}:
        return True
    else :
        return False

# main function

# irreducable polynomial
#x^8 +x^4+ x^3 + x+ 1.
irrpoly = "100011011"
getAllPossible8bitString()
calculateMulInverse()
while(True):
    # take input 
    
    print("\nEnter first polynimial ( As binary bit stream ):")
    input1= input()
    if input1=="end":
        break
    if not check(input1):
        print("invalid input  , try again ")
        continue
    print("Enter 2nd polynimial ( As binary bit stream ):")
    
    input2= input()
    if not check(input2):
        print("invalid input  , try again ")
        continue
    print("Enter operation : \n ( valid input : +  , -  , *  , /")
    operationInput = input()
    
    ans = getAns(input1,input2,operationInput)
    
    print("\n************\nans = ",ans)

# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 20:03:42 2022

@author: User
"""





def compare2values(str1,str2):
    
    if int(str1,2)>int(str2,2):
        return 1
    elif int(str1,2)<int(str2,2):
        return -1
    else:
        return 0
        


# divide str1 / str2 
"""
1001 ) 101011 ( 100 -> ans
       100100 -> tmp divi
      ----------
               -> divi new
"""
def mod(divi,divisor):
    ans = 0b00
    i = 1
    # if divisor is already big , return ans
    if compare2values(divi, divisor)==-1:
        return divi
    while(compare2values(divi, divisor)!=-1):
        # if both string has same len, then div ans append 1
        #print("ans = "+str(ans)+" divisor = "+divisor+ " dividend = "+divi)
        if len(divi)==len(divisor):
            
            tmpans=0b1
            ans = tmpans+ans
            divi = xorStrings(divi,divisor)
            #print("inside if : tmpans = "+str(tmpans)+" divi= "+divi+" ans = "+str(ans))
        else:
            tmpans = 0b1<<(len(divi)-len(divisor))
            
            tmpdivi = leftShift(divisor,(len(divi)-len(divisor)))
            divi = xorStrings(tmpdivi, divi) # new divisor
            ans = tmpans+ans
            #print("inside else : tmpans = "+str(tmpans)+" tmpdivi = "+str(int(tmpdivi,2))+" divi= "+str(int(divi,2))+" ans = "+str(ans))
        if i==10:
            break
        i+=1
            
        
        
            
        
    print("finalans = "+str(ans)+" divisor = "+divisor+ " dividend = "+divi)       
        
    return divi
    


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
    while(ans[0]=="0"):
            
        ans = ans[1:]
        if(len(ans)==1):
                break
    return mod(ans,ip)

def leftShift(str1,cnt):
    ans = "".join(["0" for i in range(cnt)] )
    return str1+ans 

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
       
    return ans

def division(divi,divisor):
    ans = 0b00
    i = 1
    # if divisor is already big , return ans
    if compare2values(divi, divisor)==-1:
        return divi
    while(compare2values(divi, divisor)!=-1):
        # if both string has same len, then div ans append 1
        #print("ans = "+str(ans)+" divisor = "+divisor+ " dividend = "+divi)
        if len(divi)==len(divisor):
            
            tmpans=0b1
            ans = tmpans+ans
            divi = xorStrings(divi,divisor)
            #print("inside if : tmpans = "+str(tmpans)+" divi= "+divi+" ans = "+str(ans))
        else:
            tmpans = 0b1<<(len(divi)-len(divisor))
            
            tmpdivi = leftShift(divisor,(len(divi)-len(divisor)))
            divi = xorStrings(tmpdivi, divi) # new divisor
            ans = tmpans+ans
            #print("inside else : tmpans = "+str(tmpans)+" tmpdivi = "+str(int(tmpdivi,2))+" divi= "+str(int(divi,2))+" ans = "+str(ans))
        if i==10:
            break
        i+=1
            
        
        
            
    #print("ans = "+str(ans)+" divisor = "+divisor+ " dividend = "+divi)       
        
    # get bit stream 
    finalans = str(bin(ans))
    finalans = finalans[1:]    
    return finalans
        
# this function starts appropriate operation

def getAns(input1,input2, operationInput):
    
    if operationInput=="+" or operationInput=="-":
        return xorStrings(input1,input2)
    
    if operationInput=="*":
        return multiply(input1,input2)
    
    else:
        
        return "!!!!!!!!!! invalid operation !!!!!!!"

    

# main function

# irreducable polynomial
#x^8 +x^4+ x^3 + x+ 1.
ip = "100011011"
"""
# take input 
print(" Enter first polynimial ( As binary bit stream ):\n")
input1= input()
print(" Enter first polynimial ( As binary bit stream ):\n")

input2= input()
print(" Enter operation : \n ( valid input : +  , -  , *  , /")
operationInput = input()

ans = getAns(input1,input2,operationInput)

print(" ans = ",ans)
"""
#print(" ans  = = = "+str(int(multiply("10011110", "100110"),2)))
print(mod("1000010000100", ip))
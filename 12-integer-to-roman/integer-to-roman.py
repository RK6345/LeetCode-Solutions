# Interger to Roman
class Solution:
    def intToRoman(self,num : int)->str:  

        s=""
        d={1000:"M",900:"CM",500:"D",400:"CD",100:"C",90:"XC",50:"L",40:"XL",10:"X",9:"IX",5:"V",4:"IV",1:"I"}

    
        for i in d.items():
                 
                 while num>=i[0]:
    
                      s+=i[1]
                      num-=i[0]
           

        return s

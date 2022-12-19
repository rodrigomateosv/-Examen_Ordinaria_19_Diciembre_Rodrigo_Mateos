
import sys

def hollow_triangle(height):
                  

  if height==0  
   return []
    
  if height==1:
    return ["#"]
    
  if height==2:
    return ["#", "##", "###"]
    
  triangle=["_" * (2 * height - 1)]
  for i in range(1,height-1):
    triangle.append("" * (height - i - 1) + "#" + "" * (2 * i - 1) + "#" + "_" * (height - i - 1))
    
  
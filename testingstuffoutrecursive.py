
import turtle
#sL=sideLength,lvls=levels
def snowflakeSide(sL,lvls):
    if lvls<=0:
        turtle.forward(sL)
        return
    turtle.forward(sL/3)
    turtle.left(60)
    snowflakeSide(sL/3,lvls-1)
    turtle.right(120)

#check tree fxn

def snowflake(sL,lvls):
    return #range
    
    
        
    
    


if __name__=="__main__":
    x=raw_input("press return when ready to draw")
    snowflakeSide(200,1)
    x=raw_input("press return when done")

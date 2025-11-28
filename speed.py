import sys
def cal_speed(distance,time):
    """REturns the calculated speed"""
    return (distance/time)

if __name__ == "__main__":
    try:
       #command line interface for jenkins
        if len(sys.argv) == 2:
          distance = int(sys.argv[1])
          time = int(sys.argv[2])
        else:
            distance = int(input("Enter the distance covered:"))
            time = int(input("Enter the time taken:"))
            if distance < 0:
                 print("Invalid! the distance cannot be in negative")
            #result
            result = cal_speed(distance,time)
            print("calculated speed is : ",result)
                 
    except ValueError:
           print("Invalid please enter the input in correct format")                
        
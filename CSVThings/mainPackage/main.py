# main.py

from utilsPackage.utils import *

# Call the function and store what it returns 
#  in a variable called data

if __name__ == "__main__":

    data = read_CSV_file()
    
    print("# of rows in dataset:", len(data))
    
    print(data[0])
    print(data[-1])
    
    # i want a list comprehension expression
    # to pull out all the collision Types into a set
    
    collisionTypes = {myData[6] for myData in data}
    
    
    #FOR THURSDAY
    # modify the expression above to exclude the blank collision type
    '''
    for data in myData:
    # how to check here?
        if not any(data):
            continue
        data.append(data)
    '''
        
    print("# of collision types:", len(collisionTypes))
    print(collisionTypes)
    
    
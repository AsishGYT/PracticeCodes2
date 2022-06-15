#Change a Dictionary Into a Class

# Turns a dictionary into a class
class Dict2Class(object):
      
    def __init__(self, my_dict):
          
        for key in my_dict:
            setattr(self, key, my_dict[key])
  
# Driver Code
if __name__ == "__main__":
      
    # Creating the dictionary
    my_dict = {"Name": "ash",
               "Rank": "99",
               "Subject": "Python"}
      
    result = Dict2Class(my_dict)
      
    # printing the result
    print("After Converting Dictionary to Class : ")
    print(result.Name, result.Rank, result.Subject)
    print(type(result))
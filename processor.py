from scipy.spatial.distance import cosine

import re
import pandas as pd
def weight_processor(weight_string):
    """
    takes - weight_string
        ex: 1 kg 200 g, 
    returns - weight in kg with no units
        ex: 1.2000
    """
    # can handle, 1 kg 200 g, 1.2 kg 
    pattern1 = r".*(\b\d+).*(\b\d+).*"
    # can handle 1 kg, 2 kg
    pattern2 = r".*(\b\d+).*"

    result_pat1 = re.search(pattern1, weight_string)

    if result_pat1:
        groups = result_pat1.groups()
        return float(groups[0] + "." + groups[1])
    
    result_pat2 = re.search(pattern2, weight_string)

    if result_pat2:
        groups = result_pat2.groups()
        weight = float(groups[0])
        if weight > 100:
            return weight / 1000
        return float(weight)






    
if __name__ == "__main__":
    
    laptop_data = pd.read_csv("test.csv")
    weights = laptop_data["Item Weight"]
    laptop_data["Weight Num"] =  laptop_data["Item Weight"].apply(weight_processor)
    min_weight = laptop_data["Weight Num"].min()
    laptop_data["Weight Num"] =  laptop_data["Item Weight"].apply(weight_processor)
    min_weight = laptop_data["Weight Num"].min()
    max_weight = laptop_data["Weight Num"].max()
    laptop_data["Weight Num"] = laptop_data["Weight Num"].apply(lambda x : (x - min_weight) / (max_weight - min_weight)) * 100
    
    
    question = "How often you travell along with your laptop?"
    print(question)
    q1_options = {
        "0":{
            "text": "yes, I travell a lot.",
            "vector": [0]
        },
        "1":{
            "text": "Not much, Usaully stay at my desk.",
            "vector": [100]
        },
        "2":{
            "text": "Do not have any specification .",
            "vector": [50]
        },

    }

    inp = input()
    user_vector = q1_options[inp]["vector"]

    #laptop_data["cosine similarity"] = laptop_data["Weight Num"].apply(lambda x: 1 - cosine([x], user_vector))
    
    cosine_sims = []
    for i in laptop_data["Weight Num"]:
        print(i)
        cosine_sims.append(1 - cosine([i], user_vector))

    
    print(cosine_sims)
        
    

# List1 = [4, 47, 8, 3]
# List2 = [3, 52, 12, 16]
# result = 1 - spatial.distance.cosine(List1, List2)print(result)
    print(user_vector)


    





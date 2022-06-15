from tokenize import group
from scipy.spatial.distance import cosine
import numpy as np
from numpy.linalg import norm

import re
import pandas as pd
from sqlalchemy import false
def weight_processor(weight_string):
    """
    takes - weight_string
        ex: 1 kg 200 g, 
    returns - weight in kg with no units
        ex: 1.2000
    """
    if weight_string == None:
        return None
    # can handle, 1 kg 200 g, 1.2 kg 
    pattern1 = r".*(\b\d+).*(\b\d+).*"
    # can handle 1 kg, 2 kg
    pattern2 = r".*(\b\d+).*"

    result_pat1 = re.search(pattern1, weight_string)

    if result_pat1:
        groups = result_pat1.groups()
        kg = float(groups[0])
        gm = float(groups[1])
        return kg + gm / 1000
        # return float(groups[0] + "." + groups[1])
    
    result_pat2 = re.search(pattern2, weight_string)

    if result_pat2:
        groups = result_pat2.groups()
        weight = float(groups[0])
        if weight > 100:
            return weight / 1000
        return float(weight)



def storage_processor(storage_string):
    """
    takes - storage_string
        ex: 1 TB, 4 GB
    return -
        1 TB -> 1024, 4 Gb -> 4
    """
    # 1 Tera byte
    # 1 giga byte
    storage_string = str(storage_string)
    tb_pattern = r".*(\b\d+)(\s+)[tT].*"
    gb_pattern = r".*(\b\d+)(\s+)[gG].*"

    result_tbpat = re.search(tb_pattern, storage_string)
    if result_tbpat:
        groups = result_tbpat.groups()
        return float(groups[0]) * 1024
    
    result_gbpat = re.search(gb_pattern, storage_string)
    if result_gbpat:
        
        groups = result_gbpat.groups()
        return float(groups[0])


# cpu power
def processor_speed(speed_string):

    #take 2.4 GHz and show as 2.4
    ghz_pattern_Decimal = r".*(\b\d+).*(\b\d+)(\s)[GHz].*"
    ghz_pattern_NoDecimal = r".*(\b\d+)(\s)[GHz].*"


    result_ghz_decimal = re.search(ghz_pattern_Decimal, speed_string)
    if result_ghz_decimal:    
        print("ghz value is")
        groups = result_ghz_decimal.groups()
        value = float(groups[0]) + float(groups[1])/10
        return (value)
    
    result_ghz_Nodecimal = re.search(ghz_pattern_NoDecimal, speed_string)
    if result_ghz_Nodecimal:    
        print("ghz value is")
        groups = result_ghz_Nodecimal.groups()
        value = float(groups[0])
        return (value)


#battery life
def battery_life(batteryLife_string):
    #6 hours to 6
    battery_life_pattern_Decimal = r".*(\b\d+).*(\b\d+)(\s)[Hours].*"
    battery_life_pattern_NoDecimal = r".*(\b\d+)(\s)[Hours].*"

    result_battery_decimal = re.search(battery_life_pattern_Decimal, batteryLife_string)
    if result_battery_decimal:    
        print("battery life is")
        groups = result_battery_decimal.groups()
        value = float(groups[0]) + float(groups[1])/10
        return (value)
    
    result_battery_Nodecimal = re.search(battery_life_pattern_NoDecimal, batteryLife_string)
    if result_battery_Nodecimal:    
        print("battery life is")
        groups = result_battery_Nodecimal.groups()
        value = float(groups[0])
        return (value)




#screen size
def screen_size(screensize_string):
    #take 13.5 inches and convert to 13.5
    #take 30 centimeters and convert to 30/2.54 = 12
    inch_pattern_decimal = r".*(\b\d+).*(\b\d+)(\s)[Inches].*"
    inch_pattern_nodecimal = r".*(\b\d+)(\s)[Inches].*"
    cm_pattern_decimal = r".*(\b\d+).*(\b\d+)(\s)[Centi].*"
    cm_pattern_nodecimal = r".*(\b\d+)(\s)[Centi].*"

    result_screen_In_decimal = re.search(inch_pattern_decimal, screensize_string)
    if result_screen_In_decimal:    
        print("screen size is")
        groups = result_screen_In_decimal.groups()
        value = float(groups[0]) + float(groups[1])/10
        return (value)
    
    result_screen_In_Nodecimal = re.search(inch_pattern_nodecimal, screensize_string)
    if result_screen_In_Nodecimal:    
        print("screen size is")
        groups = result_screen_In_Nodecimal.groups()
        value = float(groups[0])
        return (value)

    result_screen_cm_decimal = re.search(cm_pattern_decimal, screensize_string)
    if result_screen_cm_decimal:    
        print("screen size is")
        groups = result_screen_cm_decimal.groups()
        value = float(groups[0]) + float(groups[1])/10
        return (value/2.54)
    
    result_screen_cm_Nodecimal = re.search(cm_pattern_nodecimal, screensize_string)
    if result_screen_cm_Nodecimal:    
        print("screen size is")
        groups = result_screen_cm_Nodecimal.groups()
        value = float(groups[0])
        return (value/2.54)


def numbers_extractor(string):
    """
    extract numbers out of the string
    """
    if not string:
        return None
    pattern = r"[-+]?(?:\d*\.\d+|\d+)"
    numbers = re.findall(pattern=pattern, string=string)
    return numbers

def get_first_or_none(nums):
    if nums:
        return float(nums[0])
    return None


# user vec  - 1, 4, nan, nan, 10
# product v - nan, 5, 8, nan,  8

def cosine_similarity(a, b):
    matrix = pd.DataFrame({"A": a, "B": b})
    matrix = matrix.dropna(axis = 0, how='any')
    a = matrix[['A']]
    b = matrix[['B']]
    return 1 - (cosine(a, b))

def update_user_vector(prev_vec, change_dict):
    prev_vec[change_dict["index"]] = change_dict["value"]

    return prev_vec

def update_similarity_scores(dataFrame, user_vec):
    """
    for each row in dataFrame, calculte similarity score wiht user_vec and add as new col
    """
    rows = dataFrame.values.tolist()
    cols = list(dataFrame.columns)
    for row in rows:
        row.append(cosine_similarity(row, user_vec))
    cols.append("similarity score")

    return pd.DataFrame(rows, columns=cols)

  
if __name__ == "__main__":
    
    laptop_data = pd.read_csv("test.csv")
    laptop_data["price"] = laptop_data["price"].apply(lambda x: x.replace(",",""))
    laptop_data = laptop_data.astype({"price": float})
    weights = laptop_data["Item Weight"]
    laptop_data["Weight Num"] =  laptop_data["Item Weight"].apply(weight_processor)
    laptop_data["RAM Num"] =  laptop_data["RAM Size"].apply(lambda x: get_first_or_none(numbers_extractor(str(x))))
    #laptop_data["RAM Num"] =  laptop_data["RAM Size"].apply(storage_processor)
    laptop_data["Disk Num"] =  laptop_data["Hard Drive Size"].apply(storage_processor)
    laptop_data["Graphic flag"] =  laptop_data["Graphics Card Ram Size"].apply(lambda x: 1 if x else 0)
    laptop_data["Battery Life"] =  laptop_data["Average Battery Life (in hours)"].apply(lambda x: get_first_or_none(numbers_extractor(str(x))))


    df = laptop_data[["Brand", "Series","Weight Num", "RAM Num", "price", "Graphic flag", "Disk Num", "Battery Life",  "product url" ]]
    
    product_features = df[["Weight Num", "RAM Num", "Graphic flag", "Disk Num", "Battery Life", "price"]]
    product_features_unchanged = product_features


    # columns
    #Graphic flag,Disk Num,RAM Num,Weight Num,Battery Life,price,product url,Brand,Series

    user_vec = [np.nan for i in range(9)]

    # min_weight = laptop_data["Weight Num"].min()
    # laptop_data["Weight Num"] =  laptop_data["Item Weight"].apply(weight_processor)
    # # min_weight = laptop_data["Weight Num"].min()
    # # max_weight = laptop_data["Weight Num"].max()
    # # laptop_data["Weight Num"] = laptop_data["Weight Num"].apply(lambda x : (x - min_weight) / (max_weight - min_weight)) * 100

    question1 = "How often you travell along with your laptop?"
    print(question1)

    q1_options = {
        "0":{
            "text": "yes, I travell a lot.",
            "change": {
                "index":2,
                "value":1.5
            }
        },
        "1":{
            "text": "Not much, Usaully stay at my desk.",
            "change": {
                "index":2,
                "value":3
            }
        },
        "2":{
            "text": "Do not have any specification .",
            "change": {
                "index":2,
                "value":np.nan
            }
        },

    }

    print("0 : yes, I travell a lot.")
    print("1 : Not much, Usaully stay at my desk.")
    print("2 : Do not have any specification .")

    inp = input()
    user_vec = update_user_vector(user_vec, q1_options[inp]["change"])
    print("user vec after q1", user_vec)

    product_features = update_similarity_scores(df, user_vec)
    print(product_features.sort_values(by = ["similarity score"], ascending=0))


    # print("user vec", user_vector)
    # #laptop_data["cosine similarity"] = laptop_data["Weight Num"].apply(lambda x: 1 - cosine([x], user_vector))
    
    # cosine_sims = []
    # # [100], [100]
    # for i in laptop_data["Weight Num"]:
    #     A = np.array(user_vector)
    #     B = np.array([i])
    #     cosine = np.dot(A,B)/(norm(A)*norm(B))
    #     print("Cosine Similarity:", cosine)
        
    question2 = "What is your laptop typically used for ?"
    print(question2)
    #RAM

    q2_options = {
        "0":{
            "text": "gaming and media development",
            "change": 
            {
                "index":3,
                "value":16
            }
        },
        "1":{
            "text": "office and general business purpose",
            "change": {
                "index":3,
                "value":4
            }
        },
        "2":{
            "text": "student usage/design and development",
            "change": {
                "index":3,
                "value":8
            }
        },

    }

    print("0 : gaming and media development")
    print("1 : office and general business purpose")
    print("2 : student usage/design and development")

    inp = input()
    user_vec = update_user_vector(user_vec, q2_options[inp]["change"])

    print("user vec after q2", user_vec)
    product_features = update_similarity_scores(df, user_vec)
    print(product_features.sort_values(by = ["similarity score"], ascending=0))    






    question3 = "What is the price range you want for your laptop ?"
    print(question3)
    #RAM

    q3_options = {
        "0":{
            "text": "less than 30000",
            "change": 
            {
                "index":4,
                "value":15000
            }
        },
        "1":{
            "text": "30000 to 50000",
            "change": {
                "index":4,
                "value":50000
            }
        },
        "2":{
            "text": "more than 50000",
            "change": {
                "index":4,
                "value":75000
            }
        },

    }

    print("0 : less than 30000")
    print("1 : 30000 to 50000")
    print("2 : more than 50000")

    inp = input()
    user_vec = update_user_vector(user_vec, q3_options[inp]["change"])

    print("user vec after q3", user_vec)


    product_features = update_similarity_scores(df, user_vec)
    print(product_features.sort_values(by = ["similarity score"], ascending=0))

    print(product_features["similarity score"][1])
    print(product_features["similarity score"][40])
    print(product_features["similarity score"][18])


# user_vec - [{priority, value}] 

# change - {
#  index ,
#  priority - ,
#  how -  direct, aggregate
# }

list1 = [3,4,15000]
list2 = [1.5,16,50000]
list3 = [1.6, 8, 29900]



    





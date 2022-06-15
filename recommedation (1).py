from copy import copy, deepcopy
from typing import List
from unicodedata import name
import pandas as pd


class Value:
    def __init__(self, match_type: str, value: str) -> None:
        # match_type - exact, contains, gt, lt
        self.match_type = match_type
        self.value = value


def filter_df(df, match_type: str, column, value):
    print(match_type, column, value)
    if match_type == 'exact':
        df = (df[df[column] == value])
        return df


class Option:
    def __init__(self, option: int, option_text: str, filter_properties: List, filter_values: List[Value]) -> None:
        # filter_properties -> [Grahic processor, grahic memory]
        # fiter_values  ->  [Filter(exact, Nvida), Filter(gt, 6)]
        self.option = option
        self.option_text = option_text
        self.filter_properties = filter_properties
        self.filter_values = filter_values
        # for each filter_property
        # iterate over rows, keep rows that match filter criteria on filter_property


class QuestionAndOptions:
    def __init__(self, question: str, options: List[Option]) -> None:
        self.selected_options = []
        self.question = question
        self.options = options

    def apply_filter_data(self, df):
        """
        for each row in laptop data
            for each selected option
                {
                0,
                ["type", "manufacturer"] -> cols,

                [{exact, abc}, {}]  
                } 
                    for i in  len(cols):
                        if my_filter(FilterValues[i].filter_type, FilterValues[i].value, row[cols[i]]):
                            add_row
                        else:
                            pass
        """
        # rec = pd.DataFrame(columns=df.columns)
        df_list = []
        for option in self.selected_options:
            for i in range(len(option.filter_properties)):
                print("properties it effect - ",  option.filter_properties[i])
                temp_df = filter_df(df, option.filter_values[i].match_type,
                                    option.filter_properties[i], option.filter_values[i].value)
                df_list.append(temp_df)

        return pd.concat(df_list)


if __name__ == "__main__":
    laptop_data = pd.read_excel("test.xlsx")
    laptop_data_mutate = deepcopy(laptop_data)

    q1 = "what do you use it for?"
    q1_options = [
        Option(0, "gaming and video editing", ["Brand"], [
            Value("exact", "ASUS")]),
        Option(1, "Office and bussiness intelligence", [
            "Brand"], [Value("exact", "Dell")]),
        Option(2, "student use", [
            "Brand"], [Value("exact", "HP")]),
    ]

    Q1 = QuestionAndOptions(q1, q1_options)

    Q1.selected_options.append(q1_options[0])
    #Q1.selected_options.append(q1_options[2])

    resp = Q1.apply_filter_data(laptop_data_mutate)

    print(resp)
    #filter_df(laptop_data_mutate, "exact", "type", "Office")


###
#TO DO
#HOW TO DEAL WITH CONVERTING THE TABLE VALUES TO CONTINOUS & DISCONTINOUS FUNCTIONS
###
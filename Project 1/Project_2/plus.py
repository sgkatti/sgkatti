import os
import math
import random
import pandas as pd
class Plus:
    def __init__(self):
        pass

    def add(self, a, b):
        return a + b

    def multiply(self, a, b):
        return a * b
    def dataframe_info(self, df: pd.DataFrame):
        print("DataFrame Info:")
        print(df.info())
        print("\nDataFrame Head:")
        print(df.head())
        print("\nDataFrame Description:")
        print(df.describe())
if __name__ == "__main__":
    plus = Plus()
    result_add = plus.add(5, 10)
    result_multiply = plus.multiply(5, 10)
    print(f"Addition Result: {result_add}")
    print(f"Multiplication Result: {result_multiply}")
    
    # Example DataFrame
    data = {
        'A': [1, 2, 3, 4, 5],
        'B': [10, 20, 30, 40, 50],
        'C': ['a', 'b', 'c', 'd', 'e']
    }
    df = pd.DataFrame(data)
    plus.dataframe_info(df)

import pandas as pd

# TODO: Read the data from the csv file and create a list of objects
# return the list of objects
def read_from_file(file_name: str) -> list:
    """
    Read the data from the csv file and create is as a pandas dataframe

    :param file_name: The name of the file to read from
    """


    try:
        df = pd.read_excel(file_name)
        print(df.head())
        print(f"File reading successful:{file_name}")
        return df
    except Exception as e:
        print(f"File reading error:{file_name}. Exception: {e}")
        return None
 



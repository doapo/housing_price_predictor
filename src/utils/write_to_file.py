import pandas as pd

# TODO: Write the content to the file
# return nothing
def write_to_file(file_name: str, content: str) -> None:
    """
    Write the content to the csv file

    :param file_name: The name of the file to write to
    :param content: The content to write to the file

    :return: None
    
    """

    try:
        if isinstance(content, pd.DataFrame):
            content.to_csv(file_name, index=False)
    except Exception as e:
        print(f"File writting error:{file_name}. Exception: {e}")
        return
    pass
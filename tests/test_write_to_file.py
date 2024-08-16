import pytest
import pandas as pd

from src.utils.write_to_file import write_to_file

def test_write_to_file():
    # Test writing to a file with a non-pandas dataframe
    write_result = write_to_file("non_existent_file.csv", "content")
    
    # Check if the function returns None
    assert write_result is None
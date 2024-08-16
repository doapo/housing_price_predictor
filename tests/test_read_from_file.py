import pytest
import pandas as pd

from src.utils.read_from_file import read_from_file

def test_read_from_file():
    # Test reading a non-existent file
    df_result = read_from_file("non_existent_file.xlsx")
    
    # Check if the function returns None
    assert df_result is None
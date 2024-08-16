import pytest

from src.classes.House import House

def test_update_house_by_id():
    house = House(
        id = 1461,
        neighborhood = "NAmes",
        house_style = "1Story",
        overall_condition = 6,
        year_built = 1961,
        roof_type = "Gable",
        roof_material = "CompShg",
        foundation_material = "CBlock",
        heating = "GasA",
        central_air = "Y",
        electrical = "SBrkr",
        fireplace = 1,
        garage_area = 730,
        date_sold = 2010
    )
    house.update_house_by_id(1461, {"neighborhood": "Disneyland"})
    assert house.neighborhood == "Disneyland"

def test_delete_house_by_id():
    house = House(
        id = 1461,
        neighborhood = "NAmes",
        house_style = "1Story",
        overall_condition = 6,
        year_built = 1961,
        roof_type = "Gable",
        roof_material = "CompShg",
        foundation_material = "CBlock",
        heating = "GasA",
        central_air = "Y",
        electrical = "SBrkr",
        fireplace = 1,
        garage_area = 730,
        date_sold = 2010
    )
    house.delete_house_by_id(1461)
    assert house.house_data == {}

def test_get_houses_by_filters():
    house = House(
        id = 1462,
        neighborhood = "NAmes",
        house_style = "1Story",
        overall_condition = 6,
        year_built = 1958,
        roof_type = "Hip",
        roof_material = "CompShg",
        foundation_material = "CBlock",
        heating = "GasA",
        central_air = "Y",
        electrical = "SBrkr",
        fireplace = 0,
        garage_area = 312,
        date_sold = 2010
    )
    filtered_houses = house.get_houses_by_filters({"year_built": 1958, "neighborhood": "NAmes"})
    assert filtered_houses[0].__dict__ == house.__dict__

    
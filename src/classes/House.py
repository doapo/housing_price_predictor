# TODO: create the house class including a number of fields including id, neighborhood,
# house_style, overall_condition, year_built, roof_type, roof_material, foundation_material,
# heating, central air, electrical, fireplace, garage_area, date_sold (MM/YYYY)


class House:
    def __init__():
        # TODO: Initialize the house objects, this should have the following properties: id, 
        # neighborhood, house_style, overall_condition, year_built, roof_type, roof_material, 
        # foundation_material, heating, central_air, electrical, fireplace, garage_area, date_sold
        pass
    
    @classmethod
    def update_house_by_id(self, house_id: int, updated_fielda:dict) -> None:
        # TODO: Update the house by id
        # Example: id = 1, updated_fields = {"neighborhood": "Gilbert"}
        # This should update the neighborhood of the house with id 1 to Gilbert
        pass

    def delete_house_by_id(self, house_id: int) -> None:
        # TODO: Delete the house by id
        pass
    @classmethod
    def get_houses_by_filters(self, filters: list) -> list:
        # TODO: Get the houses by filters
        # Example: filters = ["id" : 1, "neighborhood": "Gilbert"]
        # This should return the house with id 1 and neighborhood Gilbert
        pass
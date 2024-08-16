# TODO: create the house class including a number of fields including id, neighborhood,
# house_style, overall_condition, year_built, roof_type, roof_material, foundation_material,
# heating, central air, electrical, fireplace, garage_area, date_sold (MM/YYYY)


class House:
    house_data = {}
    def __init__(self, id:int, neighborhood:str, house_style:str, overall_condition:int, year_built:int, roof_type:str, roof_material:str, foundation_material:str, heating:str, central_air:str, electrical:str, fireplace:int, garage_area:int, date_sold:str):
        self.id = id
        self.neighborhood = neighborhood
        self.house_style = house_style
        self.overall_condition = overall_condition
        self.year_built = year_built
        self.roof_type = roof_type
        self.roof_material = roof_material
        self.foundation_material = foundation_material
        self.heating = heating
        self.central_air = central_air
        self.electrical = electrical
        self.fireplace = fireplace
        self.garage_area = garage_area
        self.date_sold = date_sold
        House.house_data[id] = self

    @classmethod
    def update_house_by_id(self, house_id: int, updated_fields:dict) -> None:
        """
        This method updates the house by id with the updated fields

        :param house_id: The id of the house to update
        :param updated_fields: The fields to update

        :return: None
        """
        for key, value in updated_fields.items():
            setattr(House.house_data[house_id], key, value)
        

    def delete_house_by_id(self, house_id: int) -> None:
        """
        This method deletes the house by id

        :param house_id: The id of the house to delete

        :return: None
        """

        # TODO: Delete the house by id
        del House.house_data[house_id]

    @classmethod
    def get_houses_by_filters(self, filters: dict) -> list:
        """
        This method gets the houses by filters

        :param filters: The filters to apply

        :return: The list of houses that match the filters
        """
        filtered_houses = []

        for house in House.house_data.values():
            if all(getattr(house, key) == value for key, value in filters.items()):
                filtered_houses.append(house)
        return filtered_houses

        
from utils.read_from_file import read_from_file
from utils.write_to_file import write_to_file
from classes.House import House

def main():

    # read the data from the file and create the house objects
    df = read_from_file("data.xlsx")

    # create a dictionary with key being the "id" and value being the house object
    house_data = {}

    for _, row in df.iterrows():
        house = House(
            id = row['Id'],
            neighborhood = row['Neighborhood'],
            house_style = row['HouseStyle'],
            overall_condition = row['OverallCond'],
            year_built = row['YearBuilt'],
            roof_type = row['RoofStyle'],
            roof_material = row['RoofMatl'],
            foundation_material = row['Foundation'],
            heating = row['Heating'],
            central_air = row['CentralAir'],
            electrical = row['Electrical'],
            fireplace = row['Fireplaces'],
            garage_area = row['GarageArea'],
            date_sold = row['YrSold']   
        )
        house_data[row['Id']] = house
    

    # Call the methods on the house objects
    # 1. Get the houses built in 2006 and the neighborhood Gilbert
    print("Filtered houses:")
    filtered_houses = house.get_houses_by_filters({"year_built": 2006, "neighborhood": "Gilbert"})
    print(filtered_houses[0].__dict__)

    # 2. Update those houses to have a new neighborhood as "Disneyland"
    print("Updated houses:")
    for house in filtered_houses:
        house.update_house_by_id(house.id, {"neighborhood": "Disneyland"})
        print(house.__dict__)

    print(house_data[2314].__dict__)
    
    # 3. Lastly, delete those houses 
    print("Deleted houses:")

    for house in filtered_houses:
        house.delete_house_by_id(house.id)
        del house_data[house.id]
    
    updated_df = df[df['Id'].isin(list(house_data.keys()))]

    print(len(updated_df))
    # write the updated data to the csv file
    print(df.head())
    write_to_file("data_updated.csv", updated_df)


if __name__ == "__main__":
    main()

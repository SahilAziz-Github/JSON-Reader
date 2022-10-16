import json

file_name = 'Pathao Courier.geojson'

with open(file_name, 'r', encoding='utf-8') as f:
    my_list = json.load(f)
    #print(my_list)
    #print(my_list["features"])

    print("View zone names: ")
    a = str(input())
    if a == "yes":
        for x in my_list["features"]:
            print("Zone Name: ", x["properties"]["zone_name"])
            print("Zone Code: ", x["properties"]["zone_code"])
            continue

    print("Change zone name ? ")
    b = str(input())

    print("Old Zone Name:")
    m = str(input())
    print("New Zone Name:")
    n = str(input())


    if b == "y":
        for y in my_list["features"]:
            if y["properties"]["zone_name"] == m:
                y["properties"]["zone_name"] = n
                print("Old zone name: ",m)
                print("New zone name: ",n)
                print("Zone Name: ", y["properties"]["zone_name"])
                print("Zone Code: ", y["properties"]["zone_code"])
                print("Co-Ordinate: ", y["geometry"]["coordinates"])
                break









    #
    # for x in my_list["features"]:
    #
    #     if x["properties"]["zone_name"] == m :
    #         x["properties"]["zone_name"] = n
    #
    #
    #
    #     print("Co-Ordinate: ", x["geometry"]["coordinates"])
    #
    #
    #     coordinates = x["geometry"]["coordinates"][0]


        # for point in coordinates:
        #     #if x["properties"]["zone_name"] == "Tongi":
        #     print(point)
        # print("Zone Name: ", x["properties"]["zone_name"])






    # 👇️ [{'id': 1, 'name': 'Alice'}, {'id': 2, 'name': 'Bob'}, {'id': 3, 'name': 'Carl'}]
#    print(my_list)
#   print(" ")
#    print(my_list.get(features))





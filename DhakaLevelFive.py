import json

file_name = 'SLICED DHAKA BY NAIM.json'

with open(file_name, 'r', encoding='utf-8') as f:
    my_list = json.load(f)
    #print(my_list)
    #print(my_list["features"])

    print("View zone names: ")



    #a = str(input())
    #z = False
    # for x in my_list["features"]:
    #     if x["properties"]["level_2"] == "Dhaka":
    #         print("Zone Name: ", x["properties"]["level_1"])
    #         print("Zone Name: ", x["properties"]["level_2"])
    #         print("Zone Name: ", x["properties"]["level_3"])
    #         print("Zone Name: ", x["properties"]["level_4"])
    #         print("Zone Name: ", x["properties"]["level_5"])
    #         break

    c = 0
    for x in my_list["features"]:

       if x["properties"]["level_5"] != "":

           c = c + 1
           print("Serial:       ", c)
           print("Division:     ", x["properties"]["level_1"])
           print("District:     ", x["properties"]["level_2"])
           print("Area:         ", x["properties"]["level_3"])
           print("Sub-Area:     ", x["properties"]["level_4"])
           print("Granular:     ", x["properties"]["level_5"])
           print("Co-Ordinates: ", x["geometry"]["coordinates"])

           print("\n")

















    #        Dhaka =[
    #            "Division": x["properties"]["level_1"],
    #            "District": x["properties"]["level_2"],
    #            "Area": x["properties"]["level_3"],
    #            "SubArea": x["properties"]["level_4"],
    #            "Granular": x["properties"]["level_5"],
    #            "Co-Ordinates": x["geometry"]["coordinates"]
    #        ]
    # jsonfile = json.dumps(Dhaka,indent=6)
    #
    #
    #
    # with open("onlyDhaka.json", "w") as export:
    #     export.write(jsonfile)





    #         print("Zone Code: ", x["properties"]["zone_code"])
    #         continue
    #
    # print("Change zone name ? ")
    # b = str(input())
    #
    # print("Old Zone Name:")
    # m = str(input())
    # print("New Zone Name:")
    # n = str(input())
    #
    #
    # if b == "y":
    #     for y in my_list["features"]:
    #         if y["properties"]["zone_name"] == m:
    #             y["properties"]["zone_name"] = n
    #             print("Old zone name: ",m)
    #             print("New zone name: ",n)
    #             print("Zone Name: ", y["properties"]["zone_name"])
    #             print("Zone Code: ", y["properties"]["zone_code"])
    #             print("Co-Ordinate: ", y["geometry"]["coordinates"])
    #             break



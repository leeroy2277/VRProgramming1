province_list = {"QC": "Quebec", "BC": "British columbia", "MNT": "manatoba"}
prov = input("enter the province code > ")

if prov.upper() not in province_list:
    print ("sorry not correct !")
else:
    result = province_list[prov.upper()]
    print("the province name is {0}".format(result))


province_list = {'qc' : 'Quebec', 'bc' : 'British columbia', 'mnt' : 'manatoba'}


prov = input("the provence name is {0}",(result))

result = province_list[prov.upper()]

print("The province name is {0}".format(result))
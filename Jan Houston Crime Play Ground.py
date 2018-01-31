
# coding: utf-8

# In[ ]:


# open file and make list of lists, split new lines and commas
def openfile(file_name):
    string_data = open(file_name).read()
    string_list = string_data.split("\n")[1:]
    final_list = []

    for row in string_list:
        string_fields = row.split(",")
        int_fields = []
        for value in string_fields:
            int_fields.append(value)
        final_list.append(int_fields)
    return final_list

# Trying to get strings that only contain integers changed to integers in the list
# I think I need to do a new list, if the string is a string, pass it along, if it contains only numbers, turn it into an int
# then store it into the new list // Proving difficult, and research shows a list should only contain one type of data
# so maybe a dictionary?
#   def var_to_int():
#        for i in final_list:
#            for z in i:
#                if isinstance(z, int):
#                    return final_list.map(int(z))
#                else:
#                    pass


# Testing the above string to int function above
#x = [["1", "2", 3], [4, 5, 6], ["7", "8", "9"]]
#y = isinstance(x[2], str)
#x2 = []
#x3 = []
#for i in x:
#    for z in i:
#    print(z)
#
#    if str(z):
#       print("yay?")
#       x2 = list(list(str(z) for z in i) for i in x if True)
#
#    elif int(z):
#        print("not!")
#        x3 = list(list(str(z) for z in i) for i in x if True)
#print(x)
#print(x2)
#print(x3)

crime = openfile("Houston_crime_Jan_2017.csv")
#print(crime[0:10])

def offense_type(input_file, user_input):
    count = 0
    for i in input_file:
        for z in i:
            #print(z)
            #print(count)
            if z != user_input:
                pass
            else:
                count += 1
    return count

interest = input("""\nWhat are you interested in?
Murder, Rape, Robbery, Aggravated Assault, Burglary, Theft, Auto Theft
This is case sensitive.
>>> """)

t = offense_type(crime, interest)
print("There were", t, interest, "'s in Houston in January")

#list2 = [list(map(int, z)) for z in x] # if list only contains integers
#new_list = list(list(int(a) for a in b) for b in T1 if a.isdigit())


# # Date[0], Hour[1], Offense Type[2], Beat[3], Premise[4], Block Range[5], Street Name[6], Type[7], Suffix[8], # offenses[9]
# ## Murder Rape Robbery Aggravated Assault Burglary Theft Auto theft

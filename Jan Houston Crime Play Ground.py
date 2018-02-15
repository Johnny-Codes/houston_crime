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

crime = openfile("Houston_crime_Jan_2017.csv")

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

# # Date[0], Hour[1], Offense Type[2], Beat[3], Premise[4], Block Range[5], Street Name[6], Type[7], Suffix[8], # offenses[9]
# ## Murder Rape Robbery Aggravated Assault Burglary Theft Auto theft

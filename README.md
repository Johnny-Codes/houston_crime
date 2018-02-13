# Houston Crime Data
Learning data science in Python using Jupyter notebook. This is my practice play ground for what I learn

# Changelog
13 FEB 18:
Uploaded getthedata.py which will download all available data from the website in the excel format. They also have Access format which can be downloaded by changing '.xls' to '.mdb' on line 15. Next step is to write a script to convert the .xls into .csv which I will update this file to do it all at the same time. Also, I need to get all these different files into one file, which I should've just read the pages to memory and written to a CSV file and delete the header data.

31 JAN 18:
Initial

# What it does right now:

opens the CSV file, takes a users input, and returns how many of that crime happened in the data set.


# What I learned:

getthedata.py:

wget module to download files to the hard drive. Although, since I want these to be CSV files, I'll probably add a function or two to read it and save it as a CSV so there aren't 30+ excel documents to go through.

How to iterate over links and then iterate them to get the href. This initially stumped me because I was returning to a list initially and trying to use the list to do the .attrs['href'] command but once I put it in the for loop the Response Error (I think) resolved itself.

Initial:

I spent a lot of time trying to get the strings that only contain integers to be integers in the data set. After some research I realized it best to leave all the data in the list as the same type of data. So, to take that into account, I created a variable (count = 0) to count how many times the string showed up

There was lots and lots of research into isinstance(), int(), str() and fiddling around with for loops and if statements,
  which really helped me learn more of how those execute
 
 Also got to utlize the Jupyter Notebook which helps visualize the data while playing with it (hence the Play Ground title)

# To Do:

[] Make input more user friendly using numbers (ie 1 = Murders) so the user doesn't have to type so much

[] As mentioned earlier, get the files to write one large file in CSV format

# Completed To Do's:

[X] Make the input a function that will rerun again so the user can find more information

# Where I want this to eventually go:

[] make a heatmap

[1/2] integrate all the data I can get (the website goes back to 2012 I think). The getthedata.py downloads the excel or access data right now but it really needs to convert it to a CSV file and maintain only 1 header data row for reference.

[] allow user to select a date range and find data for that range

[] find out how to run the function with multiple inputs and if there are not those multiple inputs, don't break

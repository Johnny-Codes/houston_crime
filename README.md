# houston_crime
Learning data science in Python using Jupyter notebook. This is my practice play ground for what I learn

31 JAN 18:
Initial

What it does right now:

opens the CSV file, takes a users input, and returns how many of that crime happened in the data set.


What I learned:

I spent a lot of time trying to get the strings that only contain integers to be integers in the data set. After some research I realized it best to leave all the data in the list as the same type of data. So, to take that into account, I created a variable (count = 0) to count how many times the string showed up

There was lots and lots of research into isinstance(), int(), str() and fiddling around with for loops and if statements,
  which really helped me learn more of how those execute

To Do:

Make input more user friendly using numbers (ie 1 = Murders) so the user doesn't have to type so much

Make the input a function that will rerun again so the user can find more information


Where I want this to eventually go:

[] make a heatmap

[] integrate all the data I can get (the website goes back to 2012 I think)

[] allow user to select a date range and find data for that range

[] find out how to run the function with multiple inputs and if there are not those multiple inputs, don't break

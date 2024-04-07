# This pogram print a tuple that stores all months on the year
# This program contains a second tuple that stores only summer months
# Then iy prints all summer months one at a time

Months_of_year = ("January",
                  "February",
                  "March", 
                  "April",
                  "May",
                  "June",
                  "July",
                  "August",
                  "September",
                  "October",
                  "November",
                  "December")


summer_months = Months_of_year[4:7]
for month in summer_months:
    print(month)



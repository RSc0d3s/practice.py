#store info in key value pairs
# word = meaning for real world dictionaries
# key = value (python dictionary)

#name your dictionary
#Jan = key, January = value
# make sure keys are unique
#curly brackets for dicitionaries
monthConversions = {"Jan": "January",
                    "Feb": "February",
                    "Mar": "March",
                    "Apr": "April",
                    "May": "May",
                    "Jun": "June",
                    "Jul": "July",
                    "Aug": "August",
                    "Sep": "September",
                    "Oct": "October",
                    "Nov": "November",
                    "Dec": "December",}

print(monthConversions["Nov"])
print(monthConversions.get("Feb"))

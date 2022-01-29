#help program make decisions
#allow program to respond to conditions

#I wake up
#If I'm hungry
#    I eat breakfast

#I'm at a restaurant
#if I want meat = if
#   I order steak
#Otherwise = elif
#   otherwise if I want pasta
#   I order spaghetti and meatballs
#otherwise = else
#   I'LL check the menu

is_male = True 
is_tall = True #modify according to data required

#can also use "and" instead or or
if is_male or is_tall : #if male or tall execute
    print("You are a male or tall or both.")

elif is_male and not(is_tall):  #means else if
    print("You are a short male.")

elif not(is_male) and is_tall:
    print("You are a short male.")

else:
    print("You are neither male or tall.")

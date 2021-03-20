import builtins

# Create a string: team
team = "teen titans"
# Define change_team()
def change_team():
    """Change the value of the global variable team."""
    global team


    # Use team in global scope

    # Change the value of team in global: team
    team = "justice league"


# Print team
print(team)

# Call change_team()
change_team()

# Print team
print(team)

print(dir(builtins))

#array

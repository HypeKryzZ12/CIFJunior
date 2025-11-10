weather = [
    ["Sunday",[6, 7]],
    ["Monday",[2, 5]],
    ["Tuesday",[7, 10]],
    ["Wednesday",[2, 6]],
    ["Thursday",[4, 9]],
    ["Friday",[1, 4]],
    ["Saturday",[9, 11]],
]

print ("This is the weather forecast for this week:")
for day, temps in weather:
    print(f"{day}: {temps[0]} {temps[1]}")

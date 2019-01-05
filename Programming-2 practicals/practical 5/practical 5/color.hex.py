COLORS ={"aquamarine1": "#7fffd4", "AliceBlue": "#f0f8ff","azure2": "#e0eeee", "azure3": "#c1cdcd",  "beige": "#f5f5dc", "black":"#000000", "BlueViolet": "#8a2be2","CadetBlue1":"#98f5ff",
"chartreuse1":"#7fff00", "cornsilk3":"#cdc8b1"}

color = input("Enter a color: ").upper()
while color !="":
    if color in COLORS:
        print ("Color code for", color, "is", COLORS[color])
    else:
         print("Invalid color")
    color = input("enter a color:")
    #checkig something
    #add docstring to prgoram fie
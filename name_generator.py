from random import randint

#print(randint(0,3))

adj = ["Lovely", "Eccentric", "Wild", "Dreamy", "Hateful", "Enchanting", "Malevolent", "Lithe", "Hostile", "Forgiving" ]
fname = ["Annalise", "Brielle", "Armeria", "Loliya", "Typhina", "Lavandula", "Pinera", "Gallae", "Willonia", "Juniperis"]
place = ["of the Norns", "of Crysalius", "of Slityia", "of the Wilderns", "of Vonteliar", "of the Tralleses", "of Nalleas", "of Delinkus", "of the Plines", "of Utralita"]
print(adj[randint(0,9)] + " " + fname[randint(0,9)] + " " + place[randint(0,9)])

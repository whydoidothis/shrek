#super duper fun text adventure game

def menu(list, question):
    for entry in list:
        print 1 + list.index(entry),
        print ") " + entry

    return input(question) - 1

holes = ["safe","suitcase","locked closet","window","shoe","door"]
keys = ["blue key","red key"]

keylocation = 2
key = 0
loop = 1
loopd = 1

print "You find yourself locked in your room. You don't know how you got there, or what time it is. Outside, you hear a grumbling. 'I miss my swamp.' You realise.. it's Shrek! You're Shrek's hostage! You panic. 'What do I do?', you ask yourself. You soon realise that there is no escape. Shrek is love. Shrek is life. You begin to lose hope, but then you spot something in the corner of your eye. A key! But to what? You see "

print len(holes), "holes in the room:"
for x in holes:
    print x
print ""

print ""
print "Which hole do you want to use the key on?"

while loop == 1:
    choice = menu(holes,"What do you want to try the key on? ")
    if choice == 0:
        if choice == keylocation:
            print "You unlock the safe. There are two keys inside of it. What?"

            print ""
            key = 1
        else:
            print "The key doesn't work on the safe."
            print ""
    elif choice == 1:
        if choice == keylocation:
            print "You unlock the suitcase. There are two keys inside of it. What?"
            print ""

            key = 1
        else:
            print "The key doesn't work on the suitcase."
            print ""
    elif choice == 2:
        if choice == keylocation:
            print "You unlock the closet. Gay people pour out. There are also two keys inside of it. What?"
            print ""
            key = 1
        else:
            print "You can't open the closet. It remains closed, and the LGBT movement gets set back several years. Thanks a lot."

            print ""
    elif choice == 3:
        if choice == keylocation:
            print "You unlock the window. There are two keys inside of it. What?"
            print ""
            key = 1
        else:
            print "The key doesn't work on the window. You look out anyway, trying to attract the attention of your neighbours, but since that time you wrecked the block party, they all pretend you don't exist, and even if they saw you now, they'd probably just ignore you. Hey, anything for the Vine, right?"
            print ""

    elif choice == 4:
        if choice == keylocation:
            print "You unlock the shoe. There are two keys inside of it. Wait what? How can a shoe have a lock? wow, Daphne sure is dumb."
        
            print ""
            key = 1
        else:
            print "You found nothing in the shoe. Seriously, did you try to unlock a shoe???"
            print ""
    elif choice == 5:
        if key == 1:
            while loopd == 1:
                koy = menu(keys,"You have two keys. Which one do you choose to use?")
                if koy == 0 :
                    loop = 0
                    loopd = 0
                    print "You put in the key, turn it, and hear a click"
                else:
                    print "Nope, nothing happens. The mere thought of Shrek is enough to make anyone nervous. Try again!"

            print ""
            
        else:
            print "The door is locked, you need to find a key."
            print ""


print "Light floods into the room as you open the door to your freedom. Just kidding! Shrek is outside, waiting for you. Rip in pieces."

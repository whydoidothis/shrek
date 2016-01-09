def bmim (a,b):
    lolm = a/(b**2)
    return "Your BMI is: %.1f" %lolm

def bmis (a,b):
    lols = (703)*(a/(b**2))
    return "Your BMI is: %.1f" %lols

def finalbmi (a):
    if 16 > a or 35 < a:
        print "Does this look like a game to you, ", name , "?"
        print "You think you're funny, ", name, "?"
        print "Do you have any idea how many people die from obesity every year?"
        print "Do you dare me to slit your throat while you sleep?? HMMM?"
        
    elif 16 < a < 18.5:
        return "Oh dear! Looks like you're underweight!"
    
    elif 24.9 >= a >= 18.5:
        return "Brilliant! You're at a healthy weight!"
    
    elif 29.9 >= a >= 25.0 :
        return "Sorry, but it looks like you're just a bit overweight."

    else :
        return "Looks like you're obese!"
      
print ("Hello! Welcome to the BMI calculator! My name is Margaret :)")
name = raw_input ("What's your name? I promise not to keep record ")
ms = raw_input("Would you like you use metric or standard? ")

if ms in ("metric","Metric","m"):
    print "Alright! How much do you weigh in kg?"
    weightm = input()
    print "Awesome! How tall are you in metres?"
    heightm = input()
    print bmim (weightm, heightm)
    print finalbmi(bmim)
    
elif ms in ("standard","Standard","s"):
    print "Coolio! How much do you weigh in pounds?"
    weights = input()
    print "Radical! How tall are you in inches?"
    print "Remember, 1 foot = 12 inches!"
    heights = input()
    print bmis (weights, heights)
    print finalbmi(bmis)

print "Bye! ~Margaret"

    

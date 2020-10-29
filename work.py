
    name=input("What is your name?")
    bucket=0
    passinggrade=int(input("What is your passing grade?"))
    for arrow in range (4):
        quiz=int(input("Enter your quiz grade"))
        quizscore=quiz*0.12
        totbucket=bucket+quizscore+quizscore+quizscore+quizscore
    #print("Your quiz average is",totbucket)
    classpart=int(input("Enter your class participation grade"))
    totclasspart=classpart*0.10
    #print("Your class participation grade is",totclasspart)
    hw=int(input("Enter your homework grade"))
    tothw=hw*0.22
    #print("Your hw grade is",tothw)
    exam=int(input("Enter your final exam grade"))
    totexam=exam*0.20
    #print("Your final exam grade is",totexam)
    bucket=totbucket+totclasspart+tothw+totexam
    print("Your final grade is",bucket)
    if passinggrade<bucket:
        print("Great job", name)
    elif passinggrade==bucket:
        print("Right on the dot",name)
    else:
        print("Better luck next time", name)



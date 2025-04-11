for i in range(1, 5): 
    print(f"Enter grades for Lesson {i}:")
    
    mid = float(input("Enter your midterm grade: "))
    fin = float(input("Enter your final grade: "))
    
    average = (mid * 0.4) + (fin * 0.6)
    
    if average < 50:
        print(f"Lesson {i}: FAILED\n")
    else:
        print(f"Lesson {i}: SUCCESSFUL\n")
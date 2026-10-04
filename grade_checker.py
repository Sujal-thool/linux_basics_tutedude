score = int(input("Enter your score: "))

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print("Grade:", grade)



'''PS C:\Users\hp\OneDrive\Desktop\tutedude\Python_and_Bash_sujal> py grade_checker.py                                                                           
Enter your score: 98                       
Grade: A
PS C:\Users\hp\OneDrive\Desktop\tutedude\Python_and_Bash_sujal> py grade_checker.py
Enter your score: 45
Grade: F
PS C:\Users\hp\OneDrive\Desktop\tutedude\Python_and_Bash_sujal> py grade_checker.py
Enter your score: 81
Grade: B
PS C:\Users\hp\OneDrive\Desktop\tutedude\Python_and_Bash_sujal>   
'''
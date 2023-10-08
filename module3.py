import average

s1=int(input("Enter the subject 1 marks: "))
s2=int(input("Enter the subject 2 marks: "))
s3=int(input("Enter the subject 3 marks: "))
s4=int(input("Enter the subject 4 marks: "))
s5=int(input("Enter the subject 5 marks: "))

print ("the average of student is :",average.avg(s1,s2,s3,s4,s5))
print ("the percentage of student is :" ,average.percent(s1,s2,s3,s4,s5))

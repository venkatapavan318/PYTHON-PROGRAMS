#string interpolation using format method.....

student_name="venkata pavan"
totalmarks=999
rollno=318
print("name of the student:\"{}\"\ntotal marks of the student:{}\nrollno the student:{}".format(student_name,totalmarks,rollno))
print(25*"*")
print("name of the student:{}\ntotal marks of the student:{}\nrollno of the student:{}".format(student_name,totalmarks,rollno))
print(25*"*")
print('name of the student:"{}"\ntotal marks of the student:{}\nroll no of the student:{}'.format(student_name,totalmarks,rollno))
print(25*"*")
print("roll no of the student:{2}\nname of the student:{0}\ntotal marks of the student:{1}".format(student_name,totalmarks,rollno))
print(25*"*")
print("total marks of the student:{TM}\nname of the student:{NM}\nroll no of the  student:{RN}".format(NM=student_name,TM=totalmarks,RN=rollno))
print(25*"*")

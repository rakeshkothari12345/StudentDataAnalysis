#  can make it as a separate project for Intermediate

# import ModulesProgram
#
# ModulesProgram.some_name()

sooraj_marks = {
    "physics": 21,
    "chemistry":34,
    "maths":45,
    "name":"sooraj"
}

dheeraj_marks = {
    "physics": 49,
    "chemistry":34,
    "maths":23,
    "name":"dheeraj"
}

bhim_marks = {
    "physics": 45,
    "chemistry":34,
    "maths":9,
    "name":"bhim"
}

student_list = [sooraj_marks,dheeraj_marks,bhim_marks]

print(student_list)

highest_in_physics = 0
highest_in_chem=0
highest_scorer_name_physics = ""
highest_scorer_name_chem = ''
for each_student in student_list:
    if(each_student.get("physics") > highest_in_physics):
        highest_in_physics = each_student.get("physics")
        highest_scorer_name_physics = each_student.get("name")

    if (each_student.get("chemistry") > highest_in_chem):
        highest_in_chem = each_student.get("chemistry")
        highest_scorer_name_chem = each_student.get("name")

print(f"Now the highest in physics is  {highest_in_physics} by {highest_scorer_name_physics}")
print(f"Now the highest in physics is  {highest_in_chem} by {highest_scorer_name_chem}")


#Next steps - add more subjects
#Add new analysis - may be total
#region wise highest scorer

#loop through it and the highest scorer in each subject
#count the number of students above 40 marks
#below 15

#make it dynamic entry input - may be tone it down to 1 subject

# number_of_students = int(input("Enter the num of students "))
#
# student_marks_my_school = []
# while(number_of_students > 0):
#     physics_marks = int(input("Physics Marks "))
#     chem_marks = int(input("Chemistry Marks "))
#     maths_marks = int(input("Maths Marks "))
#     student_name_pls = input("Student Name")
#
#     temp_marks = {
#         "Physics": physics_marks,
#         "Chemistry":chem_marks,
#         "Maths":maths_marks,
#         "name":student_name_pls
#     }
#     student_marks_my_school.append(temp_marks)
#     number_of_students = number_of_students - 1
#
# print(student_marks_my_school)




# can play with it
import numpy as np

student_data = [
    ['644244112','นายชวกร  เมืองถาวร'],
    ['644244115','นายญาณวุฒิ  บริบูรณ์'],
    ['674244101','นางสาวกนกวรรณ  พรหมเทพ'],
    ['674244102','นางสาวเกศินี  รุ่งเจริญดี'],
    ['674244103','นางสาวจิดาภา  ยิ้มย่อง'],
    ['674244104','นางสาวณาตาฌา  เรืองชัย'],
    ['674244105','นางสาวณิชนัทนท์  แสงทอง']
]

midterm = [[10],[9],[5],[10],[10],[10],[7]]
for student in student_data:
    print(f"รหัส: {student[0]}, ชื่อนามสกุล: {student[1]}")

student_np = np.array(student_data)

student_np = np.append(student_np, midterm, axis = 1)
print(student_np)

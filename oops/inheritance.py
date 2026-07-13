class User:
    def login(self):
        print("login")


    def register(self):
        print("Register")


class Student(User):
    def enroll(self):
        print("Enroll")


    def review(self):
        print("Review")


stu = Student()

stu.enroll()
stu.review()
stu.login()
stu.register()
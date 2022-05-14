# oopbasic.py

class Student:

	def __init__(self,name,age,gender):
		self.name = name
		self.age = age
		self.gender = gender

	def study(self):
		print(f'{self.name}กำลังเรียนอยู่...')

	def sawatdee(self):
		if self.gender == 'ชาย':
			tail = 'ครับ'
			callme = 'ผม'
		else:
			tail = 'ค่ะ'
			callme = 'หนู'
		print(f'สวัสดี{tail} {callme}ชื่อ{self.name}') # เติมหางเสียง ค่ะ ครับ


class SpecialStudent(Student):

	def __init__(self,name,age,gender,parent):
		super().__init__(name,age,gender)
		self.parent = parent

	def hello(self, person='เพื่อน'):
		if person == 'เพื่อน':
			print('เฮ้ย! ว่ายังไง? มีขนมไหม?')
		else:
			print('รีบเดินหนีดีกว่า ไม่อยากคุย')

	def sawatdee(self):
		print(f'หวัดดี ชื่อ{self.name}')

	def myfather(self):
		print('รู้ไหม? ผมลูกใคร')
		print(f'ผมลูก{self.parent}')


class Teacher:

	def __init__(self,name,gender,subject):
		self.name = name
		self.gender = gender
		self.subject = subject

	def teach(self):
		print('คุณครู{}กำลังสอนวิชา{}'.format(self.name,self.subject))


if __name__ == '__main__':
	student1 = Student('สมชาย',14,'ชาย')
	student2 = Student('สมศรี',14,'หญิง')
	special_student = SpecialStudent('จ้อย',16,'ชาย','นายกอบต.เจท')

	teacher1 = Teacher('จอห์น','ชาย','ภาษาอังกฤษ')
	print(teacher1.name)
	print(teacher1.subject)

	print('---8.30 น.---')
	student1.sawatdee()
	student2.sawatdee()
	teacher1.teach()
	student1.study()
	student2.study()
	print('---8.45 น.---')
	special_student.sawatdee()
	special_student.hello('ครู')
	print('เดินไปที่โต๊ะตัวเอง')
	special_student.hello('เพื่อน')
	print(f'ครู{teacher1.name}! ขอเกรดดีๆหน่อย')
	special_student.myfather()
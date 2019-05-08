''' creating a class named project which is the model of whole project 
    this projects takes user detail involved in social work and save to database
    and we can chek user detail using user id and user name '''

# user choice to creat or read detail of social worker
user_choice = input("Eneter `I` to add detail or press `any key` to read detail  :  ")
print()

# creating database
import sqlite3
if user_choice == 'I' or user_choice == 'i':
	db = sqlite3.connect('projectDB.db')
	db.execute('''CREATE TABLE IF NOT EXISTS Workers_detail (ID int primary key autoincrement, user text, post text, comments text, friends text);''')
	# db.close()

	# defining the class
	class Social:

		# Initializing the attribute
		def __init__(self, user, post, comments, friends):
			self.user = user
			self.post = post
			self.comments = comments
			self.friends = friends

	# taking input from user for detail
	user = input('Enter your Name here : ')
	post = input("Enter your Post : ")
	comments = input("Enter your comments : ")
	friends = input('Enter your friends name : ')

	# creating instance of object
	detail = Social(user,post,comments,friends)

	# Accessing the attributes of the instances

	# storing it in database
	db.execute("INSERT INTO Workers_detail VALUES (?, ?, ?, ?);", (detail.user,detail.post, detail.comments, detail.friends));
	db.commit()
	print('records created successfully')
	db.close()

else:
	# opening the database to read
	db = sqlite3.connect('projectDB.db')

	# printing the names of student
	data = db.execute("SELECT user from Workers_detail ")

	nameList = []
	for row in data:
		nameList.append(row[0])
	print()

	# taking user choice to get detail of student 
	user1 = input('Enter the "name" of the worker in string or ID to get detail  :   ')
	print()

	if user1[1:-1] in nameList:
		detail = db.execute("SELECT user,post,comments,friends from Workers_detail where user = "+user1)
		for i in detail:
			print('Name :',i[0])
			print('Post :',i[1])
			print('Comments :',i[2])
			print('Friends :',i[3])
	else:
		print('your name is not in our database')
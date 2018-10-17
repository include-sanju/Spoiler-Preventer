from multiprocessing import Pool
from send_email import send_email
from createUserDatabase import createUserDatabase
from findURL import findURL

#parameter for sorting value list (sort according to imdb rating)
def takeFourth(elem):
    return elem[3]

n_user = input('Enter number of users: ')
for i in range(int(n_user)):
  email = input('Enter your email id: ')
  #names = 'attack on titan, got, suits, friends,game of thrones'
  names = input("Enter names of tv series: ")
  #create userdatabase and store all information using mysql
  myUsercursor,myUserdb = createUserDatabase()
  sql = "INSERT INTO User_data (email,TVshows) VALUES (%s,%s);"
  val=(email,names)
  myUsercursor.execute(sql,val)
  myUserdb.commit()
#fetch data from table User_data
sql = "SELECT * FROM User_data;"
myUsercursor.execute(sql)
myUser = myUsercursor.fetchall()
#fetch specific data of last n requested users
for _ in myUser[-int(n_user):]:
  name = _[1].split(',')
  value = []
  #Use multithreading to reduce processing(webscraping) time
  with Pool(5) as thread:
    value = thread.map(findURL, name)
  subject = 'Requested TV series\' air dates'

  text = ''
  #sort in increasing order of imdb rating
  value.sort(key=takeFourth,reverse=False)
  #creating mail content to be sent
  for v in value:
      if v[3]=='-1':
        text = text + "Tv Series Name: {}  \nEnter valid name\n\n".format(v[0])
      else:
        text = text + "Tv Series Name: {}  \nStatus: {} \nStoryline: {}\nimdb Rating: {}\n\n".format(v[0],v[1],v[2],v[3])
  #sending mail to given email id
  send_email(subject,text,_[0])

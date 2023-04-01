import csv 
file = open('users_info.csv' , 'a')
writer = csv.writer(file)
file.close()
 file = open('users_info.csv' , 'a')
 writer = csv.writer(file)
writer.writerow([message.from_user.username, message.from_user.first_name,message.from_user.last_name,message.from_user.id])
 file.close()

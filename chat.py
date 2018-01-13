import fbchat
from getpass import getpass
username = "urviarya123"
passw="123urvashi"
client = fbchat.Client(username, passw)
#no_of_friends = int(raw_input("Number of friends: "))
for i in range(1):
    name = "shubham bansal"
    friends = client.getUsers(name)  # return a list of names
    friend = friends[0]
    #for i in range(len(friends)):
       #print(friends[i])
    friend1 = client.getUsers('shubham')[1]
    #friend2 = client.getUsers('<friend name 2>')[0]
    friend1_info = client.getUserInfo(friend1.uid) # returns dict with details
    #both_info = client.getUserInfo(friend1.uid,friend2.uid) # query both together, returns list of dicts
    friend1_name = friend1_info['name']
    print(str(friend1_info))
    #client.saveSession(sessionfile)
    '''
    img="C:/kk.jpg"
    client.sendLocalImage(friend.uid,message='I have something',image=img)
    '''

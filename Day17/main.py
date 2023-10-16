class User:
    def __init__(self,userid,username):
        self.username=username
        self.userid=userid
        self.followers=0
        self.following=0

    def follow(self,user):
        self.following+=1
        user.followers+=1

user1=User("1","Eric")
user2=User("2","Ren")
user1.follow(user2)


print(user1.followers)
print(user1.following)

print(user2.followers)
print(user2.following)
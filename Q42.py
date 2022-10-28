#Cathy Doherty
string= "This # weekend # I # am # going # to # a # hockey # game"
def hash_spam(string,target):
        if string >= 4:
            print("this tweet will be considered as a spam!")
        else:
            return ("none")

print(hash_spam(string,"#"))

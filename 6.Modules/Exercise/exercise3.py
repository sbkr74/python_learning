from random import shuffle as sh
from random import sample as sa
from random import randint
# modifying the original list
def shuffle_list(inList:list):
    sh(inList)
    return inList
# without modifying original list
def sample_list(userList:list):
    return(sa(userList,len(userList)))

def random7():
    rand7 = []
    while len(rand7)<7:
        r = randint(0,9)
        if r not in rand7:
            rand7.append(r)
    return rand7



if __name__ == '__main__':
    myList = [1,2,3,4,5]
    shuffleList = shuffle_list(myList)
    print(shuffleList)

    print(sample_list(myList))
    print(shuffleList)

    print(random7())
    


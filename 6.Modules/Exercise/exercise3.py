from random import shuffle as sh
from random import sample as sa

# modifying the original list
def shuffle_list(inList:list):
    sh(inList)
    return inList
# without modifying original list
def sample_list(userList:list):
    return(sa(userList,len(userList)))

    

if __name__ == '__main__':
    myList = [1,2,3,4,5]
    shuffleList = shuffle_list(myList)
    print(shuffleList)

    print(sample_list(myList))
    print(shuffleList)



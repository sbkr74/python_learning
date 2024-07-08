from random import shuffle as sh


def shuffle_list(inList:list):
    sh(inList)
    return inList

if __name__ == '__main__':
    myList = [1,2,3,4,5]
    newList = shuffle_list(myList)
    print(newList)


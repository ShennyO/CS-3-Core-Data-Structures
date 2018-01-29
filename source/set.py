from hashtable import HashTable


class Set(object):

    def __init__(self, elements=None):
        """ initialize a set object with a Hashtable """
        self.set = HashTable()

    def size(self):
        """ Returns how many items are in the set """
        return self.set.size

    def contains(self, key):
        """ Returns True if the key exists in our hash table, False otherwise """
        return self.set.contains(key)

    def add(self, key):
        """ Adds an item to the set, which is adding a key to our hashtable if it doesn't already exist """
        self.set.set(key, None)

    def remove(self, key):
        """ Removes an item from the set, which is removing a key from our hashtable if it exists """
        self.set.remove(key)



def main():
    s = Set()
    s.add('Sunny')
    s.add('Eddy')
    print(s.set)
    print(s.size())
    print(s.contains('Shut'))

if __name__ == '__main__':
    main()

from hashtable import HashTable
import pdb


class Set(object):

    def __init__(self, elements=None):
        """ initialize a set object with a Hashtable """
        if elements is None:
            self.set = HashTable()
        else:
            self.set = HashTable()
            for element in elements:
                self.set.set(element, None)

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
        self.set.delete(key)

    def union(self, new_set):
        """ Returns a new set of the combination between our self.set and the given set """
        for key in new_set.set.keys():
            self.set.set(key, None)
        return self

    def intersect(self, new_set):
        """ Returns a new set of the items that are both in the 2 sets """
        intersected_set = Set()

        for key in new_set.set.keys():
            if key in self.set.keys():
                intersected_set.add(key)
        for key in self.set.keys():
            if key in new_set.set.keys():
                intersected_set.add(key)

        return intersected_set


    def difference(self, new_set):
        """ Returns a new set of items that are in one of the sets, but not the other """
        difference_set = Set()

        for key in new_set.set.keys():
            if key not in self.set.keys():
                difference_set.add(key)
        for key in self.set.keys():
            if key not in new_set.set.keys():
                difference_set.add(key)
        return difference_set

    def is_subset(self, new_set):
        """ Returns a boolean whether the new set is all contained inside of our original set """

        for key in new_set.set.keys():
            if not self.contains(key):
                return False

        return True

def main():
    s = Set()
    new_s = Set()
    new_s.add('Sunny')
    new_s.add('Bunny')
    new_s.add('Tiger')
    s.add('Sunny')
    s.add('poo')
    s.add('Eddy')

    print(s.set.items())
    print(s.size())
    # print(s.contains('Shut'))

if __name__ == '__main__':
    main()

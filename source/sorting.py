#!python
import pdb

def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check that all adjacent items are in order, return early if not
    # pdb.set_trace()
    if len(items) > 1:
        for index, item in enumerate(items):
            if index < len(items) - 1:
                if items[index] > items[index + 1]:
                    return False
    return True


def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Swap adjacent items that are out of order
    if is_sorted(items):
        return
    else:
        for index, item in enumerate(items):
            if index < len(items) - 1:
                if items[index] > items[index + 1]:
                    items[index], items[index + 1] = items[index + 1], items[index]
                    # larger = items[index]
                    # smaller = items[index + 1]
                    # items[index] = smaller
                    # items[index + 1] = larger
        if is_sorted(items):
            return
        else:
            bubble_sort(items)

def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Find minimum item in unsorted items
    # TODO: Swap it with first unsorted item
    if is_sorted(items):
        return
    else:
        count = 0
        while count < len(items):
            smallest = items[count]
            index = count
            for x in range(count, len(items)):
                if items[x] < smallest:
                    smallest = items[x]
                    index = x
            first = items[count]
            items[count] = smallest
            items[index] = first
            count += 1
        return items


def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Take first unsorted item
    # TODO: Insert it in sorted order in front of items
    if is_sorted(items):
        return items
    else:
        # Count is used to separate the sorted and the unsorted part of the list
        count = 0
        while count < len(items):
            current_item = items[count]
            for x in reversed(range(0, count)):
                if current_item < items[x]:
                    items[x+1], items[x] = items[x], current_item
            count += 1
        return items




def merge(items1, items2):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until one list is empty
    # TODO: Find minimum item in both lists and append it to new list
    # TODO: Append remaining items in non-empty list to new list
    result = []
    items1_index = 0
    items2_index = 0
    while items1_index < len(items1) and items2_index < len(items2):
        if items1[items1_index] < items2[items2_index]:
            result.append(items1[items1_index])
            items1_index += 1
        else:
            result.append(items2[items2_index])
            items2_index += 1
    if items1_index == len(items1):
        for x in range(items2_index, len(items2)):
            result.append(items2[x])
    else:
        for x in range(items1_index, len(items1)):
            result.append(items1[x])
    # pdb.set_trace()
    return result


def split_sort_merge(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each with an iterative sorting algorithm, and merging results into
    a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Split items list into approximately equal halves
    # TODO: Sort each half using any other sorting algorithm
    # TODO: Merge sorted halves into one list in sorted order
    first_half = items[:len(items)//2]
    second_half = items[len(items)//2:]
    # pdb.set_trace()
    first_half = selection_sort(first_half)
    second_half = selection_sort(second_half)
    items = merge(first_half, second_half)
    print(items)
    return items




def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check if list is so small it's already sorted (base case)
    # TODO: Split items list into approximately equal halves
    # TODO: Sort each half by recursively calling merge sort
    # TODO: Merge sorted halves into one list in sorted order
    if is_sorted(items):
        return items
    else:
        first_half = items[:len(items)//2]
        second_half = items[len(items)//2:]
        first_half = merge_sort(first_half)
        second_half = merge_sort(second_half)
        items = merge(first_half, second_half)
        return items


def random_ints(count=20, min=1, max=50):
    """Return a list of `count` integers sampled uniformly at random from
    given range [`min`...`max`] with replacement (duplicates are allowed)."""
    import random
    return [random.randint(min, max) for _ in range(count)]


def test_sorting(sort=merge_sort, num_items=20, max_value=50):
    """Test sorting algorithms with a small list of random items."""
    # Create a list of items randomly sampled from range [1...max_value]
    items = random_ints(num_items, 1, max_value)
    print('Initial items: {!r}'.format(items))
    print('Sorted order?  {!r}'.format(is_sorted(items)))

    # Change this sort variable to the sorting algorithm you want to test
    # sort = bubble_sort
    print('Sorting items with {}(items)'.format(sort.__name__))
    items = sort(items)
    print('Sorted items:  {!r}'.format(items))
    print('Sorted order?  {!r}'.format(is_sorted(items)))


def main():
    """Read command-line arguments and test sorting algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name

    if len(args) == 0:
        script = sys.argv[0]  # Get script file name
        print('Usage: {} sort num max'.format(script))
        print('Test sorting algorithm `sort` with a list of `num` integers')
        print('    randomly sampled from the range [1...`max`] (inclusive)')
        print('\nExample: {} bubble_sort 10 20'.format(script))
        print('Initial items: [3, 15, 4, 7, 20, 6, 18, 11, 9, 7]')
        print('Sorting items with bubble_sort(items)')
        print('Sorted items:  [3, 4, 6, 7, 7, 9, 11, 15, 18, 20]')
        return

    # Get sort function by name
    if len(args) >= 1:
        sort_name = args[0]
        # Terrible hack abusing globals
        if sort_name in globals():
            sort_function = globals()[sort_name]
        else:
            # Don't explode, just warn user and show list of sorting functions
            print('Sorting function {!r} does not exist'.format(sort_name))
            print('Available sorting functions:')
            for name in globals():
                if name.find('sort') >= 0:
                    print('    {}'.format(name))
            return

    # Get num_items and max_value, but don't explode if input is not an integer
    try:
        num_items = int(args[1]) if len(args) >= 2 else 20
        max_value = int(args[2]) if len(args) >= 3 else 50
        # print('Num items: {}, max value: {}'.format(num_items, max_value))
    except ValueError:
        print('Integer required for `num` and `max` command-line arguments')
        return

    # Test sort function
    test_sorting(merge_sort, num_items, max_value)


if __name__ == '__main__':
    main()

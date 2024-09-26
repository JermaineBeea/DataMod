While next() is the most common method used with an iterator, there are a few other methods and functions you can use to interact with iterators. Here's a list of what you can do with objects created by iter():
1. next():

This is used to get the next item from the iterator. If the iterator is exhausted, it raises a StopIteration exception.

python

my_list = [1, 2, 3]
it = iter(my_list)
print(next(it))  # Output: 1

2. for loop:

You can use an iterator directly in a for loop without calling next() manually. The loop automatically handles calling next() until the iterator is exhausted.

python

for item in iter(my_list):
    print(item)

3. __iter__():

This method is used to return the iterator object itself. If you call iter() on an iterable, it will return an iterator. You can call this method explicitly as well.

python

my_iter = iter([1, 2, 3])
print(my_iter.__iter__() is my_iter)  # Output: True

4. __next__():

This method is equivalent to next(), but it’s called directly on the iterator object. You generally don’t call this method directly; instead, you use the next() function.

python

my_iter = iter([1, 2, 3])
print(my_iter.__next__())  # Output: 1
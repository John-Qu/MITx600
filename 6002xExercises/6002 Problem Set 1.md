## Introduction

Space Cows Introduction

A colony of Aucks (super-intelligent alien bioengineers) has landed on Earth and has created new species of farm animals! The Aucks are performing their experiments on Earth, and plan on transporting the mutant animals back to their home planet of Aurock. In this problem set, you will implement algorithms to figure out how the aliens should shuttle their experimental animals back across space.

Transporting Cows Across Space!

The aliens have succeeded in breeding cows that jump over the moon! Now they want to take home their mutant cows. The aliens want to take all chosen cows back, but their spaceship has a weight limit and they want to minimize the number of trips they have to take across the universe. Somehow, the aliens have developed breeding technology to make cows with only integer weights.

The data for the cows to be transported is stored in ps1_cow_data.txt. All of your code for Part A should go into ps1.py.

You can expect the data to be formatted in pairs of x,y on each line, where x is the name of the cow and y is a number indicating how much the cow weighs in tons, and that all of the cows have unique names. Here are the first few lines of ps1_cow_data.txt:

Maggie,3
Herman,7
Betsy,9
...


## Part 1: Greedy Cow Transport
0.0/20.0 points (graded)

One way of transporting cows is to always pick the heaviest cow that will fit onto the spaceship first. This is an example of a greedy algorithm. So if there are only 2 tons of free space on your spaceship, with one cow that's 3 tons and another that's 1 ton, the 1 ton cow will get put onto the spaceship.

Implement a greedy algorithm for transporting the cows back across space in the function greedy_cow_transport. The function returns a list of lists, where each inner list represents a trip and contains the names of cows taken on that trip.

Note: Make sure not to mutate the dictionary of cows that is passed in!

### Assumptions:

- The order of the list of trips does not matter. That is, [[1,2],[3,4]] and [[3,4],[1,2]] are considered equivalent lists of trips.
- All the cows are between 0 and 100 tons in weight.
- All the cows have unique names.
- If multiple cows weigh the same amount, break ties arbitrarily.
_ The spaceship has a cargo weight limit (in tons), which is passed into the function as a parameter.

### Example:

Suppose the spaceship has a weight limit of 10 tons and the set of cows to transport is {"Jesse": 6, "Maybel": 3, "Callie": 2, "Maggie": 5}.

The greedy algorithm will first pick Jesse as the heaviest cow for the first trip. There is still space for 4 tons on the trip. Since Maggie will not fit on this trip, the greedy algorithm picks Maybel, the heaviest cow that will still fit. Now there is only 1 ton of space left, and none of the cows can fit in that space, so the first trip is [Jesse, Maybel].

For the second trip, the greedy algorithm first picks Maggie as the heaviest remaining cow, and then picks Callie as the last cow. Since they will both fit, this makes the second trip [[Maggie], [Callie]].

The final result then is [["Jesse", "Maybel"], ["Maggie", "Callie"]].

```python
def greedy_cow_transport(cows,limit=10):
    trips = []
    cow_list = []
    for k in cows.keys():
        cow_list.append([cows[k],k])
    cow_list.sort(reverse=True)
    print("sorted cow_list is", cow_list)
    while True:
        trip = []
        trip_limit = limit
        for cow in cow_list:
            if cow[0] <= trip_limit:
                trip.append(cow[1])
                trip_limit -= cow[0]
                cow_list.remove(cow)
                print(trip_limit, cow_list)
        if not trip:
            return trips
        trips.append(trip)
            
            
testcase_1 = {'Betsy': 39, 'Starlight': 54, 'Willow': 59, 'Abby': 28, 'Buttercup': 11, 'Luna': 41, 'Coco': 59, 'Rose': 42}
limit_1 = 120
print(greedy_cow_transport(testcase_1, limit_1))
```

输出：

```commandline
sorted cow_list is [[59, 'Willow'], [59, 'Coco'], [54, 'Starlight'], [42, 'Rose'], [41, 'Luna'], [39, 'Betsy'], [28, 'Abby'], [11, 'Buttercup']]
61 [[59, 'Coco'], [54, 'Starlight'], [42, 'Rose'], [41, 'Luna'], [39, 'Betsy'], [28, 'Abby'], [11, 'Buttercup']]
7 [[59, 'Coco'], [42, 'Rose'], [41, 'Luna'], [39, 'Betsy'], [28, 'Abby'], [11, 'Buttercup']]
61 [[42, 'Rose'], [41, 'Luna'], [39, 'Betsy'], [28, 'Abby'], [11, 'Buttercup']]
20 [[42, 'Rose'], [39, 'Betsy'], [28, 'Abby'], [11, 'Buttercup']]
9 [[42, 'Rose'], [39, 'Betsy'], [28, 'Abby']]
78 [[39, 'Betsy'], [28, 'Abby']]
50 [[39, 'Betsy']]
81 []
[['Willow', 'Starlight'], ['Coco', 'Luna', 'Buttercup'], ['Rose', 'Abby'], ['Betsy']]


```

正确的应该是：

```commandline
[['Willow', 'Coco'], ['Starlight', 'Rose', 'Buttercup'], ['Luna', 'Betsy', 'Abby']]
```

错在for循环。cow_list已经变了，第一个没有了，而for的指针仍然指向第二个，所以漏过了Coco。

修改程序，不改变for语句所使用的list，改为添加dict查询。

```python
def greedy_cow_transport(cows,limit=10):
    trips = []
    cow_list = []
    for k in cows.keys():
        cow_list.append([cows[k],k])
    cow_list.sort(reverse=True)
    taken_dict = {}
    while True:
        trip = []
        trip_limit = limit
        for cow in cow_list:
            if cow[1] not in taken_dict:
                if cow[0] <= trip_limit:
                    trip.append(cow[1])
                    trip_limit -= cow[0]
                    taken_dict[cow[1]] = '' # 只利用dict的查询便利，值无所谓。
        if not trip:
            return trips
        trips.append(trip)
```
### Part 2: Brute Force Cow Transport
20/20 points (graded)

Another way to transport the cows is to look at every possible combination of trips and pick the best one. This is an example of a brute force algorithm.

Implement a brute force algorithm to find the minimum number of trips needed to take all the cows across the universe in the function brute_force_cow_transport. The function returns a list of lists, where each inner list represents a trip and contains the names of cows taken on that trip.

Notes:

Make sure not to mutate the dictionary of cows!
In order to enumerate all possible combinations of trips, you will want to work with set partitions. We have provided you with a helper function called get_partitions that generates all the set partitions for a set of cows. More details on this function are provided below.
Assumptions:

Assume that order doesn't matter. (1) [[1,2],[3,4]] and [[3,4],[1,2]] are considered equivalent lists of trips. (2) [[1,2],[3,4]] and [[2,1],[3,4]] are considered the same partitions of [1,2,3,4].
You can assume that all the cows are between 0 and 100 tons in weight.
All the cows have unique names.
If multiple cows weigh the same amount, break ties arbitrarily.
The spaceship has a cargo weight limit (in tons), which is passed into the function as a parameter.
Helper function get_partitions in ps1_partitions.py:

To generate all the possibilities for the brute force method, you will want to work with set partitions.

For instance, all the possible 2-partitions of the list [1,2,3,4] are [[1,2],[3,4]], [[1,3],[2,4]], [[2,3],[1,4]], [[1],[2,3,4]], [[2],[1,3,4]], [[3],[1,2,4]], [[4],[1,2,3]].

To help you with creating partitions, we have included a helper function get_partitions(L) that takes as input a list and returns a generator that contains all the possible partitions of this list, from 0-partitions to n-partitions, where n is the length of this list.

You can review more on generators in the Lecture 2 Exercise 1. To use generators, you must iterate over the generator to retrieve the elements; you cannot index into a generator! For instance, the recommended way to call get_partitions on a list [1,2,3] is the following. Try it out in ps1_partitions.py to see what is printed!

for partition in get_partitions([1,2,3]):
    print(partition)
Example:

Suppose the spaceship has a cargo weight limit of 10 tons and the set of cows to transport is {"Jesse": 6, "Maybel": 3, "Callie": 2, "Maggie": 5}.

The brute force algorithm will first try to fit them on only one trip, ["Jesse", "Maybel", "Callie", "Maggie"]. Since this trip contains 16 tons of cows, it is over the weight limit and does not work. Then the algorithm will try fitting them on all combinations of two trips. Suppose it first tries [["Jesse", "Maggie"], ["Maybel", "Callie"]]. This solution will be rejected because Jesse and Maggie together are over the weight limit and cannot be on the same trip. The algorithm will continue trying two trip partitions until it finds one that works, such as [["Jesse", "Callie"], ["Maybel", "Maggie"]].

The final result is then [["Jesse", "Callie"], ["Maybel", "Maggie"]]. Note that depending on which cow it tries first, the algorithm may find a different, optimal solution. Another optimal result could be [["Jesse", "Maybel"],["Callie", "Maggie"]].

Code Editor

```python
def partitions(set_):
    if not set_:
        yield []
        return
    for i in range(2**len(set_)//2):
        parts = [set(), set()]
        for item in set_:
            parts[i&1].add(item)
            i >>= 1
        for b in partitions(parts[1]):
            yield [parts[0]]+b


def get_partitions(set_):
    for partition in partitions(set_):
        yield [list(elt) for elt in partition]


def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    min_num_trips = len(cows)
    for trips in get_partitions(cows.keys()):
        flag = True
        for trip in trips:
            trip_weight = 0
            for cow in trip:
                trip_weight += cows[cow]
            if trip_weight > limit:
                flag = False
                break
        if flag and len(trips) <= min_num_trips:
            min_num_trips = len(trips)
            min_trips = trips
    return min_trips
```

我原来在函数内写from ps1_partition import get_partitions，可以运行。但是edX的网页报错，说找不到这个文件。既然里面只有两个函数，那我不妨复制粘贴过来。

注意测试了三种情况，两种极端的。

CORRECT 

Test 1

Function call: brute_force_cow_transport({'Lotus': 40, 'Miss Bella': 25, 'Boo': 20, 'MooMoo': 50, 'Milkshake': 40, 'Horns': 25}, 100)

Output: [['Boo', 'Lotus', 'Milkshake'], ['MooMoo', 'Miss Bella', 'Horns']]

Test 2

Function call: brute_force_cow_transport({'Buttercup': 72, 'Betsy': 65, 'Daisy': 50}, 75)

Output: [['Betsy'], ['Daisy'], ['Buttercup']]

Test 3

Function call: brute_force_cow_transport({'Buttercup': 11, 'Luna': 41, 'Betsy': 39, 'Starlight': 54}, 145)

Output: [['Starlight', 'Buttercup', 'Betsy', 'Luna']]




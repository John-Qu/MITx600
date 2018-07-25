def greedy_cow_transport(cows, limit=10):
    trips = []
    cow_list = []
    for k in cows.keys():
        cow_list.append([cows[k], k])
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


testcase_1 = {'Betsy': 39, 'Starlight': 54, 'Willow': 59, 'Abby': 28, 'Buttercup': 11, 'Luna': 41, 'Coco': 59,
              'Rose': 42}
limit_1 = 120
print(greedy_cow_transport(testcase_1, limit_1))
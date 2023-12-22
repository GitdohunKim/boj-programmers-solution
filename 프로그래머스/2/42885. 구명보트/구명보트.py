def solution(people, limit):
    people.sort() 
    boat_count = 0  
    light = 0  
    heavy = len(people) - 1  

    while light <= heavy:
        if people[light] + people[heavy] <= limit:
            light += 1
            heavy -= 1
        else:
            heavy -= 1

        boat_count += 1

    return boat_count

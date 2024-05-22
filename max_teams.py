'''
QUESTION:
You are responsible to selecting a team of 3 members from different states with a few constraints as listed below:

1. Every team must have 3 members
2. No two teams can come from the same state

Write a python function to implement this with the test cases below:
I : [1,1,1]
O : 1

I : [1,3,4,2] 
O : 2

'''

'''
ANSWER:
Steps
1. Check that our list lenght is longer than 3, if not return 0
2. Sort our list from smallest to largest.
3. Deduct one each from the first 3 members of a state, and increment count by 1
4. Remove an item from the list once it gets to zero
5. Continue this until the lenght of our original list of states is less than 3
'''
def max_team(states):
    count = 0
    if len(states) < 3:
        return 0
    states.sort(reverse=True)

    while len(states) >= 3:
        for i in range(3):
            states[i] = states[i] - 1
        count += 1

        states = [state for state in states if state > 0]
            
    return count

if __name__ == '__main__':
    print(max_team([39999,23,23,345,2]))
    print(max_team([1, 3, 4, 2]))  

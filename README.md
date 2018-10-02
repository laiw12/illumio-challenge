# Illumio Coding Challenge

### Strategy and Design Decisions

I chose to use Python 3 for the implementation of this coding challenge due to its easy-to-use "ipaddress" and "csv" modules.

For testing, I used the "unittest" module and used the default edge/test cases given in the challenge specifications. 

In terms of strategy, I decided to implement the "naive" O(n) solution in which each packet iterates through the list of rules (with backtracking/early termination). The best-case scenario of the run-time can be as fast as O(1) depending on how early a match is found.

### Algorithmic Thought Process

Although I implemented the naive, iterative solution, I did consider other approaches but found that it would take up too much space as well as found obstacles that would require more time to think out. 

For example, in order to hash a firewall rule, it was difficult to think out how "ranges/ipaddresses" would be taken in to consideration. I couldn't simply compare a port like 1000 to a range like 0-2000; it would be a match but they are not equal. I could've had two different data structures that kept track of non-ranged ports and ranged ports and compared accordingly, and it would've sped up the run-time but space would suffer. So, I decided to go with the iterative approach in which I would individually test each rule and see if it's a range or not and compare accordingly. 

Another approach I thought of was separating off the list of rules into four different lists, dividing it based on the first two rules: direction and protocol. Because there are four different combinations of direction and ports, what I could have done was have four different lists and each packet could iterate through its respective list depending on which direction/port combination it had. In the best-case scenario, each list would be divided into perfect fourths and the worst-case run-time at that point would only be 25% of what it was beforehand. However, what if it wasn't split up into perfect fourths and the lists were separated into a ratio of 05/5/10/80? Seaching for rules within the 80% partition could still be very draining on the performance. It would still perform better than the implementation I had, but I was unable to due to time constraints. 

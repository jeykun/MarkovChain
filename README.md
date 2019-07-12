# MarkovChain
This class allows to make random sortition of any number of elements of a Markov Chain, just by setting the initial distribution and probability matrix and then executing the method "export( )".

Example:

dist = [4,5,6] # three states, named zero, one and two: the weights are the proportion among them
prob = [[4,4,8],
        [2,2,5],
        [1,1,4]] # three states: these are the wheights of probability of transition among them
                 # element prob[1,2] means the probability of transition between the state 1 to the state 2
                 
cm = MarkovChain(dist,prob)
print(cm.export(50)) # here we get 51 values of the Markov Chain: the first one is from the initial distribution
                     # the others are from the transition probabilities, given the previous distribution


To get the [dist] and [prob] correctly, just input [cm.get('dist') or cm.get('prob')].

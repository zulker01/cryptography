# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    
    
    
    #************************************************************************************
    
    "*** YOUR CODE HERE ***"
    
    """
    DFS algorithm searches for every possible node from any node, it pushes the initial node
    in the stack, then finds the adjacent node of the top of stack, then add those adjacent nodes to visit
    if the destination node is found, this is stopped. else if no node is stack, , destination is not reachable
    
    """
    
    
    nextHop = util.Stack()                      # nextHop stores the path which will be visited next
    nextHop.push(problem.getStartState())       # visit root node
    visited = []                                # visited list stores which nodes are already visited, those won't be visited again  ( to avoid infinite loop )
    pathFromRootToDst=[]                         # list which stores the ans, which path to follow for reaching destination
    
    pathToCurrent= util.Stack()                 # this stack stores the path to current node
    presentHop = problem.getStartState()        # this stores the present node
   
    while not nextHop.isEmpty():                # loop until stack is not empty i.e not all node visied
        presentHop = nextHop.pop()              # get the top of stack , which node to visit
        if problem.isGoalState(presentHop):     # if current node is destination node , path found, break & return path
            break
        if presentHop not in visited:            # if present node is not visited,
        
           visited.append(presentHop)            # we have to add it to visited, means this node is visited
           successors = problem.getSuccessors(presentHop)       # get the successors of this present node
           successors.sort(key = lambda x: x[2])                # sort the successors, according to theircost
           for node in successors:                              # loop to all successors
               nextHop.push(node[0])                            # push adjacent node to next hop stack
               tempPath =  pathFromRootToDst+ [node[1]]         # add the path of next hop with path of present node
               pathToCurrent.push(tempPath)                     # push the path also in another stack, next
                                                               # when the node will be popped, his path will be popped alongside
                                                               # as both stack ( node's stack & path's stack) are pushed & popped alongside
                                                                 # so they will maintain order
        pathFromRootToDst = pathToCurrent.pop()                 # get the next nodes path  for next loop
        
    return pathFromRootToDst                                 # when loop is broken, path from root to destination will be retuned
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    
    # the BFS search algorithm does the search will visiting every adjacent node at once
    # so the path from source to destination is found faster
    # first source node is pushed to queue, then it is popped & all of its adjacent one is pushed in
    # loop is looped untill queue is not empty, or destination reached
    from util import Queue
    nextHop = Queue()                           # nextHop stores the path which will be visited next
    nextHop.push(problem.getStartState())       # visit root node
    visited = []                                  # visited list stores which nodes are already visited, those won't be visited again  ( to avoid infinite loop )
    pathFromRootToDst=[]                         # list which stores the ans, which path to follow for reaching destination
    
    pathToCurrent=Queue()                       # this stack stores the path to current node
    presentHop = problem.getStartState()        # this stores the present node
     
    while not nextHop.isEmpty():                 # loop until stack is not empty i.e not all node visied
        presentHop = nextHop.pop()               # get the top of stack , which node to visit
        if problem.isGoalState(presentHop):      # if current node is destination node , path found, break & return path
           break
        if presentHop not in visited:            # if present node is not visited,
        
           visited.append(presentHop)            # we have to add it to visited, means this node is visited
           successors = problem.getSuccessors(presentHop)  # get the successors of this present node
           for node in successors:                         # loop to all successors
               if node[0] not in visited:                  # if this adjacent node is not visitd
                   nextHop.push(node[0])                   # push adjacent node to next hop stack
                   tempPath =  pathFromRootToDst+ [node[1]] # add the path of next hop with path of present node
                   pathToCurrent.push(tempPath)             # push the path also in another path, next
                                                           # when the node will be popped, his path will be popped alongside
        pathFromRootToDst = pathToCurrent.pop()            # pop the path for the node , for next loop
       
    return pathFromRootToDst                              # return the path from source to destination

    
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    """
    this uniform cost search function searches path with least cost, it maintains a priority queue
    which sorts the queue according to the priority of the cost value. least cost node is place top of the queue
    and discoverd faster
    """
    
    from util import PriorityQueue
    nextHop = PriorityQueue()                      # nextHop stores the path which will be visited next
    nextHop.push(problem.getStartState(),0)         # visit root node with cost 0
    visited = []                                    # visited list stores which nodes are already visited, those won't be visited again  ( to avoid infinite loop )
    pathFromRootToDst=[]                            # list which stores the ans, which path to follow for reaching destination
    
    pathToCurrent=PriorityQueue()                   # this stack stores the path to current node
    presentHop = (problem.getStartState(),0)        # this stores the present node
     
    while not nextHop.isEmpty():                    # loop until stack is not empty i.e not all node visied
        presentHop = nextHop.pop()                  # get the top of stack , which node to visit
        if problem.isGoalState(presentHop):         # if current node is destination node , path found, break & return path
            break
        if presentHop not in visited:                # if present node is not visited,
        
           visited.append(presentHop)                # we have to add it to visited, means this node is visited
           successors = problem.getSuccessors(presentHop)  # get the successors of this present node
           for node in successors:                     # loop to all successors
               if node[0] not in visited:              # if this adjacent node is not visitd
                   tempPath =  pathFromRootToDst+ [node[1]]         # add the path of next hop with path of present node
                   tempCost = problem.getCostOfActions(tempPath)    # get the cost of source from this new added node
                   nextHop.push(node[0],tempCost)                   # push adjacent node to next hop stack
                   
                   pathToCurrent.push(tempPath,tempCost)             # push the path also in another path, next
                                                                       # when the node will be popped, his path will be popped alongside
        pathFromRootToDst = pathToCurrent.pop()
       
    return pathFromRootToDst                                        # return the path from source to destination
        
    
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    
    """
    Astar search is muchly used in AI, here, least path from source to destination is searched. 
    here we will use heuristic cost, which is the estimated cost from a node to destination
    so we can estimate if choosing any node will be the lowest cost one , to reach destination
    """
    from util import PriorityQueue
    nextHop = PriorityQueue()                      # nextHop stores the path which will be visited next
    nextHop.push(problem.getStartState(),0)          # visit root node
    visited = []                                    # visited list stores which nodes are already visited, those won't be visited again  ( to avoid infinite loop )
    pathFromRootToDst=[]                            # list which stores the ans, which path to follow for reaching destination
    
    pathToCurrent=PriorityQueue()                    # this stack stores the path to current node
    presentHop = (problem.getStartState(),0)        # this stores the present node
     
    while not nextHop.isEmpty():                     # loop until stack is not empty i.e not all node visied
        presentHop = nextHop.pop()                      # get the top of stack , which node to visit
        if problem.isGoalState(presentHop):          # if current node is destination node , path found, break & return path
           break
        if presentHop not in visited:                    # if present node is not visited,
            
           visited.append(presentHop)                    # we have to add it to visited, means this node is visited
           successors = problem.getSuccessors(presentHop)  # get the successors of this present node
           for node in successors:                       # loop to all successors
               if node[0] not in visited:                # if this adjacent node is not visitd
                   tempPath =  pathFromRootToDst+ [node[1]]  # add the path of next hop with path of present node
                   tempCost = problem.getCostOfActions(tempPath)+ heuristic(node[0],problem)  # get the cost of source from this new added node
                                                                                               # here the heurisitic function uses the node[0], ( node ) & graph to estimate cost to destination
                                                                                               # so cost of reaching the adjacent node & cost to destination is added find cost for this node
                   nextHop.push(node[0],tempCost)                   # push adjacent node to next hop stack
                   
                   pathToCurrent.push(tempPath,tempCost)             # push the path also in another path, next
                                                               # when the node will be popped, his path will be popped alongside
        pathFromRootToDst = pathToCurrent.pop()
       
    return pathFromRootToDst                                # return the path from source to destination
    
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch

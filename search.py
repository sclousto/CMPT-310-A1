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

#####################################################
#####################################################
# Please enter the number of hours you spent on this
# assignment here
"""
num_hours_i_spent_on_this_assignment = 15
"""
#
#####################################################
#####################################################

#####################################################
#####################################################
# Give one short piece of feedback about the course so far. What
# have you found most interesting? Is there a topic that you had trouble
# understanding? Are there any changes that could improve the value of the
# course to you? (We will anonymize these before reading them.)
"""
<The course is going great so far. Everything we've covered is interesting to me.
My only suggestion is that 20+ hours for a homework assingment seems excessive,
however, the amount of work required in this assignment was fair.>

"""
#####################################################
#####################################################

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
    Q1.1
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    #print ( problem.getStartState() )
    You will get (5,5)

    #print (problem.isGoalState(problem.getStartState()) )
    You will get True

    #print ( problem.getSuccessors(problem.getStartState()) )
    You will get [((x1,y1),'South',1),((x2,y2),'West',1)]
    """
    "*** YOUR CODE HERE ***"

    fringe = util.Stack()
    actions = []
    explored = [problem.getStartState()]
    path = []
    expanded = problem.getSuccessors(problem.getStartState())
    node = problem.getStartState()
    for x in expanded:
         fringe.push(x)
         path.append([x, "Start"])
         #print("*", x)
    while (not fringe.isEmpty()):
        node = fringe.pop()
        #print(node)
        if problem.isGoalState(node[0]):
            #print("success")
            for i in range(len(path)):
                    if(node == path[i][0]):
                        node1 = path[i]
                        actions.append(node1[0][1])
                        #print(node1)
                        break
            while (node1[1] != "Start"):
                for i in range(len(path)):
                    if(node1[1] == path[i][0]):
                        node1 = path[i]
                        actions.append(node1[0][1])
                        #print(node1)
                        break
            actions.reverse()
            #print(actions)
            return actions
        explored.append(node[0])
        expanded = problem.getSuccessors(node[0])
        for x in expanded:
            if not (x[0] in explored):
                fringe.push(x)
                path.append([x, node])
                #print("*", x)
    #print("rip dude")
    return
        
        


def breadthFirstSearch(problem):
    """
    Q1.2
    Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"

    fringe = util.Queue()
    actions = []
    explored = [problem.getStartState()]
    path = []
    expanded = problem.getSuccessors(problem.getStartState())
    node = problem.getStartState()
    for x in expanded:
         fringe.push(x)
         path.append([x, "Start"])
         #print("*", x)
    while (not fringe.isEmpty()):
        node = fringe.pop()
        if not (node[0] in explored):
            #print(node)
            if problem.isGoalState(node[0]):
                #print("success")
                for i in range(len(path)):
                        if(node == path[i][0]):
                            node1 = path[i]
                            actions.append(node1[0][1])
                            #print(node1)
                            break
                while (node1[1] != "Start"):
                    for i in range(len(path)):
                        if(node1[1] == path[i][0]):
                            node1 = path[i]
                            actions.append(node1[0][1])
                            #print(node1)
                            break
                actions.reverse()
                #print(path)
                #print(actions)
                return actions 
            expanded = problem.getSuccessors(node[0])
            explored.append(node[0])
            for x in expanded:
                if not (x[0] in explored):
                    fringe.push(x)
                    path.append([x, node])
                    #print("*", x)
    #print("rip dude")
    return


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """
    Q1.3
    Search the node that has the lowest combined cost and heuristic first."""
    """Call heuristic(s,problem) to get h(s) value."""
    "*** YOUR CODE HERE ***"

    fringe = util.PriorityQueue()
    actions = []
    explored = [problem.getStartState()]
    path = []
    cost = 0
    expanded = problem.getSuccessors(problem.getStartState())
    node = "Start"
    for x in expanded:
         fringe.push(x, x[2] + heuristic(x[0], problem))
         path.append([[x, "Start"], x[2]])
         #print("-", x)
    while (not fringe.isEmpty()):
        node = fringe.pop()
        if not (node[0] in explored):
            #print(node)
            if problem.isGoalState(node[0]):
                ##print("success")
                for i in range(len(path)):
                        if(node == path[i][0][0]):
                            node1 = path[i]
                            actions.append(node1[0][0][1])
                            #print(node1)
                            break
                while (node1[0][1] != "Start"):
                    for i in range(len(path)):
                        if(node1[0][1] == path[i][0][0]):
                            node1 = path[i]
                            actions.append(node1[0][0][1])
                            #print(node1)
                            break
                actions.reverse()
                #print(actions)
                return actions
            expanded = problem.getSuccessors(node[0])
            explored.append(node[0])
            for x in expanded:
                if not (x[0] in explored):
                    #print("-",x)
                    for i in range(len(path)):
                        if(node == path[i][0][0]):
                            cost = path[i][1] + x[2]
                            #print("*", cost)
                            #print("!", heuristic(x[0], problem))
                            break
                    fringe.update(x, cost + heuristic(x[0], problem))
                    path.append([[x, node], cost])
                    #print("*", x)
    #print("rip dude")
    return



# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch

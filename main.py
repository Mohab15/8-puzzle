import collections
import node
import algorithm as algo
#Remark When Asked to enter board Configuration enter
#them without any spaces and 0 is eqivilant to space
#e.g 102345678 means    1   0   2
#                       3   4   5
#                       6   7   8
if __name__ == '__main__':
    solver = algo
    print("welcome to 8_puzzle solver")

    while True:

        while True:  # do while to check if correct
            initial_state = input("insert initial state: ")
            freq = collections.Counter(initial_state)  # check unique
            if len(initial_state) == len(freq) == 9 and initial_state.isdecimal():
                break
            print("wrong initial state")

        print("algorithms\n"
              "-----------\n"
              "[1] BFS\n"
              "[2] DFS\n"
              "[3] A*\n")
        while True:
            switch = int(input("=>"))
            if switch in range(0, 4):
                break
        if not solver.is_solvable(initial_state):
            print(initial_state + " Cannot be solved")
            continue

        if switch == 1 or switch == 2:
            solution = algo.solver(initial_state, switch)
        elif switch == 3:
            while True:
                h = int(input("choose heuristic:\n"
                              "-----------------\n"
                              "[1] Manhattan\n"
                              "[2] Euclidean\n"))
                if h == 1 or h == 2:
                    break
                print("invalid")

            if h == 1 or h == 2:
                solution = algo.solver(initial_state, switch, h)

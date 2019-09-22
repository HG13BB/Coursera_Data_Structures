#python3

from collections import deque

def calc_height(tree):
    '''Calculate the height of an arbitrary tree.
    list -> int'''
    tdict = {k: [] for k in set(tree)} #create dictionary

    {tdict[parent].append(index) for index, parent in enumerate(tree)} #build tree


    stack = deque()
    stack.append(tdict[-1][-1]) #Initialize walking stack
    height = deque()
    height.append(1) #Initialize height stack
    maxheight = 0 #Initialize max height tracker
    parent = tdict[-1][-1]
    
    while len(tdict[parent]) > 0:
        node = stack.pop()              #current node
        depth = height.pop()            #current level
        [stack.append(i) for i in tdict[parent]]   #add children to stack
        [height.append(depth + 1) for i in range(len(tdict[parent]))] #add to height stack
        if stack[-1] in tdict:                           #node has no children
            parent = tdict[node][-1]    #travel down 1 node
        else:
            while len(stack) > 0 and not stack[-1] in tdict:          #if children
                del stack[-1]                                         #remove node from stack            
                depth = height.pop()
                maxheight = max(maxheight, depth)
            if len(stack) > 0:
                parent = stack[-1]
            else:
                break

        
        maxheight = max(maxheight, depth) #track height                
            
    return maxheight


def main():
    n = int(input())
    tree = list(map(int, input().split()))
    print(calc_height(tree))

if __name__ == "__main__":
    main()

#calc_height(([9, 7, 5, 5, 2, 9, 9, 9, 2, -1]))

import itertools

def solution(num_buns, num_required):
    num_copies = num_buns - num_required + 1
    
    keys_to_buns = list(itertools.combinations(range(num_buns),num_copies))
    
    buns_to_keys = [[] for x in range(num_buns)]
    
    for i in range(len(keys_to_buns)):
      for j in keys_to_buns[i]:
        buns_to_keys[j].append(i)
        
    return buns_to_keys

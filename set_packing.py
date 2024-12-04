import os
import sys

def load_instance(input_file_name):
    with open(input_file_name, 'r') as file:
        lines = file.readlines()

    universe = set()
    sets = []
    t = int(lines[0].strip())
    for line in lines[1:]:
        subset = set(map(int, line.strip().split(' ')))
        sets.append(subset)
        universe.update(subset)
    
    return universe, sets, t

def encode(sets, t):
    cnf = []
    n = len(sets)
    variables = list(range(1, n + 1))

    for i in range(n):
        for j in range(i + 1, n):
            if sets[i].intersection(sets[j]):
                cnf.append([-variables[i], -variables[j]])

    if t > 0:
        for combination in combinations(variables, n-t+1):
            cnf.append([-x for x in combination])
                                        
    return cnf, variables


def combinations(variables, r):
    """
    Generate all possible combinations of r elements from the variables.
    Args:
        variables (list): Input list of variables
        r (int): Length of combinations to generate
    
    Returns:
        list: List of all unique combinations of the given size
    """
    pool = tuple(variables)
    n = len(pool)
    
    if r > n:
        return []
    
    if r == 1:
        return [i for i in variables] 
        
    indices = list(range(r))
    
    result = [tuple(pool[i] for i in indices)]
    
    while True:
        for i in reversed(range(r)):
            if indices[i] != n - r + i:
                break
        else:
            return result
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        result.append(tuple(pool[i] for i in indices))
    
    return result

def cnf_to_file(cnf, num_variables, output_file):
    with open(output_file, 'w') as file:
        file.write(f"CNF {num_variables} {len(cnf)}\n")
        for clause in cnf:
            file.write(" ".join(map(str, clause)) + " 0\n")


def call_solver(cnf_file):
    glucose_path = "glucose-syrup"
    result_file = cnf_file + ".result"
    os.system(f"{glucose_path} {cnf_file} > {result_file}")
    if not os.path.exists(result_file) or os.stat(result_file).st_size == 0:
        raise RuntimeError(f"Glucose failed to generate a valid result file: {result_file}")
    return result_file

def parse_glucose_output(result_file, variables):
    with open(result_file, 'r') as file:
        lines = file.readlines()

    if "UNSATISFIABLE" in lines[0]:
        return None  
    elif "SATISFIABLE" in lines[0]:
        for line in lines:
            if line.startswith("v "):  
                model = list(map(int, line[2:].strip().split()))
                return [v for v in variables if v in model]
    else:
        raise ValueError("Unexpected solver output.")
    

def main():
    if len(sys.argv) < 3:
        print("Usage: python set_packing_decision.py <input_instance> <output_cnf>")
        sys.exit(1)

    input_file = sys.argv[1]
    cnf_file = sys.argv[2]

    universe, sets, t = load_instance(input_file)

    clauses, variables = encode(sets, t)
    cnf_to_file(clauses, len(variables), cnf_file)

    print(f"Solving the instance using Glucose...")
    result_file = call_solver(cnf_file)

    try:
        solution = parse_glucose_output(result_file, variables)
        if solution is None:
            print("NO: It is not possible to select at least", t, "disjoint sets.")
        else:
            print("YES: Selected sets (indices):", solution)
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()

import os
import sys
from itertools import combinations

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
            if not sets[i].isdisjoint(sets[j]):
                cnf.append([-variables[i], -variables[j]])
    if t > 0:
        for combination in combinations(variables, n-t+1):
            cnf.append(list(combination))
                                        
    return cnf, variables


def cnf_to_file(cnf, num_variables, output_file):
    with open(output_file, 'w') as file:
        file.write(f"p cnf {num_variables} {len(cnf)}\n")
        for clause in cnf:
            file.write(" ".join(map(str, clause)) + " 0\n")


def call_solver(cnf_file):
    glucose_path = "glucose"
    result_file = cnf_file + ".result"
    os.system(f"./{glucose_path} {cnf_file} > {result_file}")
    return result_file

def parse_glucose_output(result_file, variables):
    with open(result_file, 'r') as file:
        lines = file.readlines()
    if str(lines[-1].split(' ')[1][:-1]) == "SATISFIABLE":
        return True
    elif lines[-1].split(' ')[1][:-1] == "UNSATISFIABLE":
        return False 
    else:
        raise ValueError("Unexpected solver output.")
    

def main():
    if len(sys.argv) < 3:
        print("Usage: python set_packing.py <input_instance> <output_cnf>")
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
        if solution:
            print("YES: It is possible to select at least", t, "disjoint sets.")
        else:
            print("NO: It is not possible to select at least", t, "disjoint sets.")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()

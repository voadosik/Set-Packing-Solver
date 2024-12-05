def generate_large_satisfiable_instance(universe_size, set_size, threshold, output_file):
    """Generates a large satisfiable Set Packing instance."""
    with open(output_file, 'w') as f:
        f.write(str(threshold) + "\n")
        for i in range(0, universe_size, set_size):
            subset = list(range(i + 1, min(i + set_size + 1, universe_size + 1)))
            f.write(" ".join(map(str, subset)) + "\n")
        
        

universe_size = 100  
set_size = 3          
threshold = 20       

output_file = "large_satisfiable_instance"

generate_large_satisfiable_instance(universe_size, set_size, threshold, output_file)
print(f"Instance written to {output_file}")

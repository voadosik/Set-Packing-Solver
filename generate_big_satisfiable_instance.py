import sys

def generate_large_satisfiable_instance(universe_size, set_size, threshold, output_file):
    """Generates a large satisfiable Set Packing instance."""
    with open(output_file, 'w') as f:
        f.write(str(threshold) + "\n")
        for i in range(0, universe_size, set_size):
            subset = list(range(i + 1, min(i + set_size + 1, universe_size + 1)))
            f.write(" ".join(map(str, subset)) + "\n")
    print(f"Instance written to {output_file}")

def main():
    universe_size = 30
    set_size = 3
    threshold = 5
    output_file = "large_satisfiable_instance"

    if len(sys.argv) == 5:
        universe_size = int(sys.argv[1])
        set_size = int(sys.argv[2])
        threshold = int(sys.argv[3])
        output_file = sys.argv[4]
    elif len(sys.argv) > 1:
        print("Usage: python generate_instance.py <universe_size> <set_size> <threshold> <output_file>")
        
    generate_large_satisfiable_instance(universe_size, set_size, threshold, output_file)

if __name__ == "__main__":
    main()

import argparse

def prepare_input_file(input_file_path, output_file_path):
    with open(input_file_path, "r") as input_file, open(output_file_path, "w") as output_file:
        for line in input_file:
            line = line.strip().lower() # remove leading/trailing whitespaces and convert to lowercase
            output_file.write(line + "\n")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", help="Path to the input file")
    parser.add_argument("output_file", help="Path to the output file")
    args = parser.parse_args()

    prepare_input_file(args.input_file, args.output_file)
    print("Done! Output file saved to:", args.output_file)

if __name__ == "__main__":
    main()
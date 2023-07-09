# Leave these lines untouched
__winc_id__ = "8c2e6882503c4baa9ce2e050497c3f2f"
__human_name__ = "stds"

# Your code here
import sys


def main():
    # TODO: read text from stdin
    read_text = sys.stdin.read()

    # TODO: Filter character given as an argument from the text
    filter_text = []
    error_text = []
    for letter in read_text:
        if letter == sys.argv[1]:
            error_text.append(letter)
        else:
            filter_text.append(letter)    

    # TODO: Print the result to stdout
    filter_text = ''.join(filter_text)
    sys.stdout.write(filter_text)

    # TODO: Print the total number of removed characters to stderr
    sys.stderr.write(str(len(error_text)))




if __name__ == "__main__":
    main()

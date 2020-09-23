def generate_fizzbuzz_terms(number_of_terms):
    terms = []
    for i in range(1, number_of_terms+1):
        s = ''
        if (i % 3) == 0:
            s = s + "Bizz"
        if (i % 5) == 0:
            s = s + "Fuzz"
        if s:
            terms.append(s)
        else:
            terms.append(str(i))
    return terms

def main():
    input_string = input("How many fizzbuzz terms would you like?")
    if(input_string.isdigit()):
        number_of_terms = int(input_string)
        if(number_of_terms < 0):
            print("Invalid input! The number of terms specified must be an integer greater than 0.\nInput was detected as less than zero.")
            return -1
        if(number_of_terms == 0):
            return 0
        generated_terms = generate_fizzbuzz_terms(number_of_terms)
        print("\n".join(generated_terms))
        return 0
    else:
        print("Invalid input! The number of terms must be a positive integer.\nUnable to convert input to numerical form.")
        return -1

if __name__ == "__main__":
    import sys
    sys.exit(main())

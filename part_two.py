from part_one import decode_strand, encode_strand

def driver():
    print("-------------------------")
    print("Encoding all sequences...")
    print("-------------------------")

    all_sequences = [
        "GGGGGAAAGGCCCCTTTAAAACCCCTTTTTAAAACCCCCGGGAAAATTTTAAA",
        "GGGGGAAAUUCCCCTTTAAAACCCCUUUUUAAAACCCCCGGGAAAATTTTAAA",
        "CCCAAAAATTTTCCCCGGGTTAAAATTTTTGGGGGAAACCCGGGGAAAACCCCC",
        "CCCAAAAAGGGGCCCCCGGGGAAAACCCCGGGGGAAACCCGGGGAAAACCCCC"
    ]
    encoded_sequences = []

    for sequence in all_sequences:
        encoded_strand = encode_strand(sequence)
        encoded_sequences.append(encoded_strand)

    print("-------------------------")
    print("Categorizing encoded sequences...")
    print("-------------------------")

    categorized_sequences = {}
    categorized_sequences[-1] = []  # strands that can't be determined
    categorized_sequences[0] = []  # dna strands
    categorized_sequences[1] = []  # rna strands

    for sequence in encoded_sequences:
        category = categorize_strand(sequence)
        categorized_sequences[category].append(sequence)

    print("-------------------------")
    print("Decoding and listing undetermined sequences for review...")
    print("-------------------------")

    for sequence in categorized_sequences[-1]:
        decoded = decode_strand(sequence)
        print(decoded)


# Returns 0 for DNA (Contains "T" bases)
# Returns 1 for RNA (Contains "U" bases)
# Returns -1 if the strand cannot be categorized:
#   - Contains both "T" and "U" in the same strand
#   - There are no "T" or "U" bases in the strand
def categorize_strand(strand):
    is_t_present = False
    is_u_present = False
    #test
    #print(strand)
    for index in range(0, len(strand) - 1, 2): #fix the step
        base = strand[index]
        #print(f"index={index}")
        #print(f"base = {base}")
        if base == "T":
            is_t_present = True

        if base == "U":
            is_u_present = True
    #test
    #print(f"is_t_present = {is_t_present}")
    #print(f"is_u_present = {is_u_present}")
    has_both_bases = is_t_present and is_u_present
    has_neither_base = (not is_t_present) and (not is_u_present)

    #test
    #print(f"has_both_bases = {has_both_bases}")
    #print(f"has_neither_base = {has_neither_base}")
    #looks like the logic of has_both_bases and has_neither_base are both correct
    if (has_both_bases or has_neither_base):
        #test return value
        #print("return -1")
        return -1
    #test
    #print(f"is_t_present = {is_t_present}")
    return 0 if is_t_present else 1

#test
#ENCODED_BOTH_BASES = "G5A3U2T3C4A4C4U5A4T4C5A4G3A3"
#print(categorize_strand(ENCODED_BOTH_BASES))
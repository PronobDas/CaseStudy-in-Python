import table


def read_seq(inputfile):
    """
    :param inputfile:
    :return seq:
    It takes input of filename and convert it to sequence
    excluding "\n" and "\r".
    """
    with open(inputfile, "r") as file:
        seq = file.read()
    seq = seq.replace("\n", "")
    seq = seq.replace("\r", "")
    return seq


def translation(seq):
    """
    :param seq:
    :return protein:
    This function takes a sequence of dna and translate it to protein seq.
    """
    protein = ""
    if len(seq) % 3 == 0:
        for i in range(0, len(seq), 3):
            codon = seq[i:i+3]
            protein += table.table[codon]
    return protein


dna = read_seq("dna.txt")
prt = read_seq("protein.txt")
# print(dna)
# print(len(dna))


print(translation(dna[20:938]))
print(prt)

print(prt == translation(dna[20:938])[:-1])
# ignoring the last 3. It denotes ending codon.
# help(translation)
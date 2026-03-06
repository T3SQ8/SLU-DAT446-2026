# Denna funktion fungerar endast för filer som får plats i minnet
def easy_gene_match(gene, genome):
    with open (genome, 'r') as file:
        data = file.read()

    for sequenceStart in range(len(data)):
        genome_part = data[sequenceStart : sequenceStart + len(gene)] 

        if gene in genome_part:
            print(sequenceStart)

def gene_match(gene, genome):
	"""
  	Searches for a genetic subsequence in a genome.
  
  	Args:
    gene (str): The gene string to search for (comprising only A, C, G, T).
    genome (str): The name of the file containing the genome sequence.
  
  	Prints the positions (indexed from 0) where the gene is found in the genome.
	"""
	index = 0
	gene_length = len(gene)
	with open(genome, 'r') as file:
		reference = file.read(gene_length)

		while True:
			if reference == gene:
				print(index)

			next_character = file.read(1)
	
			# An empty string return False -> Will only run when the file is empty
			if not next_character:
				return
			
			# Shifts the beginning of the "window" by one and adds the next character
			reference = reference[1:] + next_character
			index += 1
			

if __name__ == '__main__':
	gene_match("ACA", "genome.txt")
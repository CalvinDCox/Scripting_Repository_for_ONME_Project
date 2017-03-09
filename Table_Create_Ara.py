Table Reader For Biodepvis Network Creator
Calvin D. Cox
11/27/2016
*************
Table output from interactions can be found at:

#SAMPLE CODE (In Perl?)
#load the data into an array
#DO THIS
#make an array of gene ids
foreach $line (@filedata) {
        chomp $line;
        @elements = split (/\s+/, $line);
        $gene_id = $elements[3];
        push (@genes, $geneid)
        }
 
parse the nodes and print the gene names
 
foreach $line (@filedata) {
        chomp $line;
        @elements = split (/\s+/, $line);
        $col_count = len @elements;
        for ($i=4, $i <$col_count, $i++){
            @edge = split (/+/, $elements[$i];#maybe use an escape slash
            $left_pos = $edge[0];
            $right_pos = $edge[1];
            print "$genes[$left_pos]\t$genes[$left_pos]\n";
        }
}

#Python
#1. Make Edge Lists from HRR File

#used to parse the nodes and print gene names
file = open('/scratch1/calvinc/BioDep_Network_Data/Arabidopsis_T/ExpMatAra.hrr', 'r')
genes = ['Gene_ID']
for line in file:
		#Split by tabs, ignoring spaces in cells.
		elements = line.split("\t")
		#parse out gene names in column 2 (array starts from 0)
		gene_id = elements[1]
		#print gene name to list
		genes.append(gene_id)

#Generate Gene Interaction List
file = open('/scratch1/calvinc/BioDep_Network_Data/Arabidopsis_T/ExpMatAra.hrr', 'r')		
output = open('/scratch1/calvinc/BioDep_Network_Data/Arabidopsis_T/Output.hrr', 'w')
for line in file:
		#pull all values with + found in cell
		elements = line.split("\t")
		col_count = len(elements)
		for x in range (5, col_count):
				edge = elements[x].split("+")
				left_pos = int(edge[0])
				right_pos = int(edge[1])
				left_gene = str(genes[left_pos+1])
				right_gene = str(genes[right_pos+1])
				output.write(left_gene + '\t' + right_gene + '\n')
				
#2. Make Non-Redudndant Node List

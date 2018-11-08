from Bio import Phylo, SeqIO

def AssemblerGenome(InputPhylogeny,InputPG,InputIR,InputRG,InputRR,Output):

        #Reading the number of simulatd species
        
        tree= Phylo.read(str(InputPhylogeny),'newick')
        names=sorted([item.split(')')[0].replace('=','').replace("'",'') for item in str(tree).split('name')[1:]])
        #Reading simulated sequneces belonging to each species 
        simulated_seq_dict={}
        for specs in names:
            simulated_seq_dict[specs]=[]
            for simulationsPG in InputPG.split(','):
                with open ('%s/DB/%s_dna.fa'%(simulationsPG,specs),'r') as PGSeq:
                    for records in SeqIO.parse(PGSeq,'fasta'):
                        simulated_seq_dict[specs].append(str(records.seq).replace('-',''))
        for simulationsIR in InputIR.split(','):
                with open (simulationsIR,'r') as IRSeq:
                    for records in SeqIO.parse(IRSeq,'fasta'):
                            simulated_seq_dict[records.id].append(str(records.seq).replace('-',''))
        for simulationsRG in InputRG.split(','):
                with open (simulationsRG,'r') as RGSeq:
                    for records in SeqIO.parse(RGSeq,'fasta'):
                            simulated_seq_dict[records.id].append(str(records.seq).replace('-',''))
        for simulationsRR in InputRR.split(','):
                with open (simulationsRR,'r') as RRSeq:
                    for records in SeqIO.parse(RRSeq,'fasta'):
                            simulated_seq_dict[records.id].append(str(records.seq).replace('-',''))

            #Writting outputs in the assembly
        for specs in names:
            assembly=os.path.join(str(Output),specs+'.fsa')
            txt=open(assembly,'w')
            Iter=1
            for coords in simulated_seq_dict[specs]:
                txt.write('>%s\n%s\n'%(Iter,coords))
                Iter+=1
            txt.close()
            
            
from optparse import OptionParser
import os,sys
parser = OptionParser()
parser.add_option('-F','--InputPhylogeny', dest='InputPhylogeny',help= 'Absolute path to the PhylogenyInput [required]')
parser.add_option('-P','--InputPG', dest='InputPG',help= 'Absolute path to the ProteinCodingGeneSimulationInput [required]')
parser.add_option('-I','--InputIR', dest='InputIR',help='Absolute path to the InterGenicRegionSimulationInput [required]')
parser.add_option('-N','--InputRG', dest='InputRG',help= 'Absolute path to the RNAgeneSimulationInput [required]')
parser.add_option('-R','--InputRR', dest='InputRR',help= 'Absolute path to the RepeatRegionSimulationInput [required]')
parser.add_option('-O','--Output', dest='Output',help= 'Absolute path to the Output directory [required]')

(options,args)=parser.parse_args()
InputPhylogeny=options.InputPhylogeny
InputPG=options.InputPG
InputIR=options.InputIR
InputRG=options.InputRG
InputRR=options.InputRR
Output=options.Output

if InputPhylogeny==True and InputPG==True and InputRR==True and InputRG==True and InputIR==True and Output==True :
	print ("\nAssembling Simulated DNA sequences into genome\n")
	parser.print_help()
	sys.exit(1)
if (InputPhylogeny==None or InputPG==None or InputRR==None or InputRG==None or InputIR==None or Output==None) :
	print ('\nAssembling Simulated DNA sequences into genome \nRequired filed(s) not supplied\n')
	parser.print_help()
	sys.exit(1)
import ast
input_option_dict=ast.literal_eval(options.__str__())
print ('Entered arguments are...')
for one in input_option_dict:
	print (one,input_option_dict[one])
print ('')

AssemblerGenome(InputPhylogeny,InputPG,InputIR,InputRG,InputRR,Output)
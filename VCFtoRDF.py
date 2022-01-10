###### Input expected #######
#26      93      2010-08-MT-981  A       G       .       .       PR      GT      0/0	1/1	./.
#############################
###### Output expected ######
#>NUU1A ;1;;;;;;;
#00000000000000000000000000
#>NUU1B ;1;;;;;;;
#00000000000000000000000000
#>NUU1C ;1;;;;;;;
#N0000000001000001000000100
#############################

#############################
####Description:

####--vcf : vcf file name
####--weight: A file with two tab separated columns, in the first column the position,
####in the second the weight, this is file is not necessary, the default value is 10 if not provided.
####--labels: a tab separated file, in the first column the sample ID, you can add 6 labels per sample
#### --frequency: tab separated file, in the first column sample ID, second column frequency. Default value=1

import re
from collections import defaultdict
import argparse

parser = argparse.ArgumentParser()



parser.add_argument("-vcf", "--vcf", help="vcf name")
parser.add_argument("-w", "--weight", help= "a file that contents the weight assigned to the different variants")
parser.add_argument("-l", "--labels", help= "a table that contents the different labels assigned to each sample")
parser.add_argument("-f", "--frequency", help= "a file with the frequency of each sequence")

args = parser.parse_args()
def __unicode__(self):
   return self.some_field or u'None'

ind_column={}
vcf_name=args.vcf
rdf=open(vcf_name +".rdf","w")
ind_var=defaultdict(str)
label_2=defaultdict(str)
label_3=defaultdict(str)
label_4=defaultdict(str)
label_5=defaultdict(str)
label_6=defaultdict(str)
label_7=defaultdict(str)
label_8=defaultdict(str)
weights=defaultdict(lambda: 10)
frequency=defaultdict(lambda:1)
sample_list=[]
variant_order=[]
row=0


rdf.write("  ;1.0\n")

with open (vcf_name,"r") as vcf:
	for line in vcf:
		l=line.split()
		if re.match(r'^#CHROM', l[0]):
			header=line
			sample_size=len(header.split("\t"))-9
			sample_list=header.split("\t")[9:sample_size+9]
			for index,id in enumerate(sample_list):
				ind_column[index+9]=id.split("_")[1].rstrip()
		elif not re.match(r'^##',l[0]):
			variant_order.append(l[1].rstrip())
			for genotype in range(9,sample_size+9,1):
				if l[genotype].rstrip()=="1/1":
					ind_var[ind_column[genotype]]=ind_var[ind_column[genotype]]+"1"
					#ind_var[ind_column[genotype]]=ind_var[ind_column[genotype]]+l[4].rstrip()
				else:
					if l[genotype].rstrip()=="0/0":
						ind_var[ind_column[genotype]]=ind_var[ind_column[genotype]]+"0"
						#ind_var[ind_column[genotype]]=ind_var[ind_column[genotype]]+l[3].rstrip()
					else:
						ind_var[ind_column[genotype]]=ind_var[ind_column[genotype]]+"N"


if args.weight is not None:
	weight=args.weight
	with open(weight,"r") as var_weight:
		for line in var_weight:
			l=line.split("\t")
			weights[l[0].rstrip()]=l[1].rstrip()
if args.frequency is not None:
	freq= args.frequency
	with open(freq, "r") as sample_freq:
		for line in sample_freq:
			l=line.split("\t")
			frequency[l[0].rstrip()]=l[1].rstrip()

labels_file=args.labels
if args.labels is not None:
	with open(labels_file,"r") as sample_labels:
		first_line = sample_labels.readline()
		n_label=len(first_line.split("\t"))-1
		for line in sample_labels:
			l=line.split("\t")
			if n_label >= 1:
				label_2[l[0].rstrip()]=l[1].rstrip()
			if n_label >=2:
				label_3[l[0].rstrip()]=l[2].rstrip()
			if n_label >=3:
				label_4[l[0].rstrip()]=l[3].rstrip()
			if n_label >=4:
				label_5[l[0].rstrip()]=l[4].rstrip()
			if n_label >=5:
				label_6[l[0].rstrip()]=l[5].rstrip()
			if n_label>=6:
				label_7[l[0].rstrip()]=l[6].rstrip()
			if n_label==7:
				label_8[l[0].rstrip()]=l[7].rstrip()


for variant in variant_order:
	rdf.write(variant)
	rdf.write(" ;")
rdf.write("\n")
for variant in variant_order:
	rdf.write(str(weights[variant]))
	rdf.write(";")
rdf.write("\n")
for key, value in ind_var.items():
	rdf.write(">"+key+" ")
	rdf.write(";")
	rdf.write(str(frequency[key]))
	rdf.write(";")
	rdf.write(label_2[key])
	rdf.write(";")
	rdf.write(label_3[key])
	rdf.write(";")
	rdf.write(label_4[key])
	rdf.write(";")
	rdf.write(label_5[key])
	rdf.write(";")
	rdf.write(label_6[key])
	rdf.write(";")
	rdf.write(label_7[key])
	rdf.write(";")
	rdf.write(label_8[key])
	rdf.write("\n")
	rdf.write(value)
	rdf.write("\n")


rdf.close()


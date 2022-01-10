wgs={}
wgs_q={}
geno={}
geno_q={}
mega={}
mega_q={}
geno_2={}
geno_q_2={}


with open ("ALL.chrMT.phase3_callmom-v0_4.20130502.genotypes.haplogrep.NoQuote", "r") as kg_snp:
	for line in kg_snp:
		l=line.split("\t")
		geno[l[0]]=l[1]
		geno_q[l[0]]=l[2].rstrip()


with open ("1000G_haps_vcf_phylotree17.txt", "r") as kg_snp_2:
        for line in kg_snp_2:
                l=line.split("\t")
                geno_2[l[0]]=l[1]
                geno_q_2[l[0]]=l[2].rstrip()


with open ("ALL.chrMT.phase3_callmom-v0_4.20130502.genotypes.mega_pos.vcf.recode.onlySNP.hsd.haplogrep.unquote", "r") as kg_mega:
	for line in kg_mega:
		l=line.split("\t")
		mega[l[0]]=l[1]
		mega_q[l[0]]=l[2].rstrip()

with open ("Haplogrep_1KG_comparison_3rdPhase_quality_v2", "w") as result:
	for key in geno.keys():
		result.write(key)
		result.write("\t")
		if key in geno.keys():
			result.write(geno[key])
			result.write("\t")
			result.write(geno_q[key])
		else:
			result.write("NA")
			result.write("\t")
			result.write("NA")
		result.write("\t")
		if key in geno_2.keys():
			result.write(geno_2[key])
			result.write("\t")
			result.write(geno_q_2[key])
		else:
			result.write("NA")
			result.write("\t")
			result.write("NA")
		result.write("\t")
		if key in mega.keys():
			result.write(mega[key])
			result.write("\t")
			result.write(mega_q[key])
		else:
			result.write("NA")
			result.write("\t")
			result.write("NA")
		result.write("\n")


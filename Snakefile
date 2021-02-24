
configfile: "configfile.yaml"
from time import strftime, localtime
import os

rule all:
     input:
             # expand("{outputDIR}/phylogeny/phylogeny.nwk",outputDIR=config["outputDIR"]), simulate phylogeny
             expand("{outputDIR}/simulations/phenSim/{replication_index}/sim{replication_index}.png",outputDIR=config["outputDIR"],replication_index=range(config['phenReplication'])),
             expand("{outputDIR}/simulations/ld/ldPlot.LD.PNG",outputDIR=config["outputDIR"]),
             expand("{outputDIR}/simulations/genSim/sims.pickle",outputDIR=config["outputDIR"]),

#step1) genome simulator
include: os.path.join('modules','genSim','genSim.smk')

#step2) variant caller
include: os.path.join('modules','varCall','snpSites.smk')
include: os.path.join('modules','varCall','vcfRefiner.smk')

#step3) phenotype simulator
include: os.path.join('modules','phenSim','phenPermutor.smk')
include: os.path.join('modules','phenSim','phenSim.smk')

#step 4) LD visualization
include: os.path.join('modules','ld','ldPlotter.smk')

#step 5) Population structure visualization
include: os.path.join('modules','visualizers','simVis.smk')
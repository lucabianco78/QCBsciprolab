"""
NAME:
SURNAME:
Matricola: 

exercise1.py
"""




def loadTSV(datafile):
    """gets the filename of the tsv file and returns a pandas dataframe with all the loaded information"""
    
def computestats(data):
    """gets the data structure loaded with loadTSV and prints the total number of sequences, 
    the total number of LGs, and for each LG the total number of contigs, total size and total sum of gaps. 
    Finally, the total size of the genome should be printed (i.e. the sum of all the total sizes)"""
    
def computeN50(data, lg):
    """given the input data, and an LG (if unspecified all data should be considered) and returns the N50. 
    If the LG does not exist a warning message should be returned."""

def plotN50(data,lg):
    """given the input data, an lg (optional, if unspecified all data should be considered),  
    plots the contig sizes from the biggest to the smallest and the N50 as vertical line"""

if __name__ == "__main__":
    
    dataFile = "ctg_data.tsv"
    data = loadTSV(dataFile)

    computestats(data)

    computeN50(data)

    computeN50(data, "LG1")

    computeN50(data, "LG2")

    computeN50(data, "LG10")

    computeN50(data, "LG16")

    computeN50(data, "LG22")



import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'
import kipoi
import pandas as pd
import matplotlib.pyplot as pyplot
from matplotlib import style


BedFile = []
st = 0
en = 101
"""while st < 10000:
    BedFile.append("chr9" + "	" + str(st)+ "	" + str(en))
    st = st + 101
    en = en + 101"""

#print(BedFile[0])

Fasta = "/Users/timreeves/Desktop/Python Stuff/Zea_mays.AGPv4.dna.chromosome.9.fa"
BedFile = "/Users/timreeves/Desktop/Python Stuff/Intervals.bed.txt"
Model = kipoi.get_model('DeepBind/Arabidopsis_thaliana/RBP/D00283.001_RNAcompete_At_0284')
#Model = kipoi.get_model('pwm_HOCOMOCO/human/AHR')
Prob = Model.pipeline.predict(dict(fasta_file = Fasta, intervals_file = BedFile))

data = {'Location' : Bed, 'Probability' : Prob}
df = pd.DataFrame(data)
df = df["Probability"].apply(lambda x: (x - df["Probability"].min()) / (df["Probability"].max() - df["Probability"].min()))

style.use("ggplot")
pyplot.plot(range(len(df.values)), df.values)
pyplot.xlabel("Read #")
pyplot.ylabel("Binding Probability")
pyplot.show()

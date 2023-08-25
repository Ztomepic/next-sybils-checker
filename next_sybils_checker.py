import pandas as pd
import numpy as np

f1 = "arbSybilAttackers.csv"
f2 = "hopSybilAttackers.csv"
f3 = "connextAllocations.csv"

arb_sybils = pd.read_csv(f1, sep=",")
for i in range(len(arb_sybils)):
    arb_sybils.loc[i, "blacklisted_address"] = "0" + arb_sybils.loc[i, "blacklisted_address"][1:]

    
hop_sybils = pd.read_csv(f2, sep=",")

connext = pd.read_csv(f3, sep=",")

arb_sybils_addr = list(arb_sybils.blacklisted_address)
hop_sybils_addr = list(hop_sybils.address)
connext_addr = list(connext.address)

sybils = set(connext_addr).intersection(set(arb_sybils_addr + hop_sybils_addr))
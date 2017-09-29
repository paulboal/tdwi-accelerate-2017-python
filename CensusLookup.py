import pandas as pd

class CensusLookup:
    def __init__(self, file='DEC_10_DP_DPDP1_with_ann.csv'):
        self._file = 'DEC_10_DP_DPDP1_with_ann.csv'
        df = pd.read_csv(file, skiprows=1)
        df = df.set_index(df.Geography.apply(lambda x: x[6:]))
        self._df = df

    def get_data(self):
        return self._df

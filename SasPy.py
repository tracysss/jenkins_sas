import saspy
import pandas as pd
import unittest
sas=saspy.SASsession(cfgname='winlocal')

f = open('C:/Users/trsong/Documents/SGF2020/P0.sas','r')
f_text = f.read()
f_text = f_text.replace('\\','/')

# run SAS program
ps = sas.submit(f_text)
print(ps['LOG'])

# convert SAS dataset to pandas dataframe
df = pd.read_sas(r'C:\Users\trsong\Documents\SGF2020\Programs\output\output.sas7bdat') 
value1_list = df['value1'].tolist()
value2_list = df['value2'].tolist()
total_list = df['total'].tolist()
print(df)

# unit test cases
class TestSAS_dataset(unittest.TestCase):
    def setUp(self):
        self.value1 = [100, 100, 120]
        self.value2 = [110, 150, 80]

    # test if values are populated
    def test_value(self):
        for i in range(len(self.value1)):
            self.assertEqual(value1_list[i], self.value1[i]) 
            self.assertEqual(value2_list[i], self.value2[i])  
            
    # test column total
    def test_total(self):
        for i in range(len(self.value1)):
            self.assertEqual(total_list[i], self.value1[i] + self.value2[i])

# run unit test
if __name__ == '__main__':
    unittest.main()

#saspy.SAScfg

#print("########### SAS text ##############")
#print(f_text)

## import csv file
#ds = sas.read_csv("C:/Users/trsong/Documents/SGF2020/input.csv")
#ps = sas.submit("""
#libname  outlib 'C:\\Users\\trsong\\Documents\\SGF2020';
#data outlib.output;
#	informat date $10. number 8. value1 8. value2 8.;
#	INPUT date number value1 value2;
#	total = value1 + value2;
#	datalines;
#01/01/2020   1    100      	110
#01/02/2020   2    100    	150
#01/03/2020	 3    120        80
#;

#run;

#""")
#print(ps['LOG'])

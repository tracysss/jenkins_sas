import pandas as pd
import unittest
import xmlrunner

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
    def test_value1(self):
        for i in range(len(self.value1)):
            self.assertEqual(value1_list[i], self.value1[i]) 

    # test if values are populated
    def test_value2(self):
        for i in range(len(self.value1)):
            self.assertEqual(value2_list[i], self.value2[i]) 

    # test column total
    def test_total(self):
        for i in range(len(self.value1)):
            self.assertEqual(total_list[i], self.value1[i] + self.value2[i])

# run unit test
if __name__=='__main__':
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestSAS_dataset))
    runner = xmlrunner.XMLTestRunner(output=r'C:\Program Files (x86)\Jenkins\workspace\SAS project test\reports')
    runner.run(test_suite)

print("######## End of Python ############")

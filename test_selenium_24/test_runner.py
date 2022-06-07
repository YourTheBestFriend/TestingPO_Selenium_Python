import unittest 
import calc_test
 
calcTestSuite = unittest.TestSuite() 
calcTestSuite.addTest(unittest.makeSuite(calc_test.CalcTest)) 

runner = unittest.TextTestRunner(verbosity=2) # 2 : отображается строка справки каждого теста и результат
runner.run(calcTestSuite)
import unittest 
import calc_test_2
 
calcTestSuite = unittest.TestSuite() 
calcTestSuite.addTest(unittest.makeSuite(calc_test_2.CalcBasicTests)) 
calcTestSuite.addTest(unittest.makeSuite(calc_test_2.CalcExTests))
print("Количество тестов: " + str(calcTestSuite.countTestCases()) + "\n") 
# print(f'Количество тестов: {str(calcTestSuite.countTestCases())}\n')

runner = unittest.TextTestRunner(verbosity=2) # 2 : отображается строка справки каждого теста и результат
runner.run(calcTestSuite)
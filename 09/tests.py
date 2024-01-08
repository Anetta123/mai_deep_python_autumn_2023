import unittest
import cjson




class JsonTest(unittest.TestCase):
    def setUp(self):
        self.json_str = '{"name": "AdeelSolangi", "language": "Sindhi", "id": "V59OF92YF627HFY0", "bio": "V59O0V59OF92YF627HFY0V59OF92YF627HFY0V59OF92YF627HFY0V59OF9F92YF627HFY0V59OF92YF627HFY0V59OF92YF627HFY0V59O0V59OF92YF627HFY0V59OF92YF627HFY0V59OF92YF627HFY0V59OF9F92YF627HFY0V59OF92YF627HFY0V59OF92YF627HFY0V59O0V59OF92YF627HFY0V59OF92YF627HFY0V59OF92YF627HFY0V59OF9F92YF627HFY0V59OF92YF627HFY0V59OF92YF627HFY0V59O0V59OF92YF627HFY0V59OF92YF627HFY0V59OF92YF627HFY0V59OF9F92YF627HFY0V59OF92YF627HFY0V59OF92YF627HFY0", "version": 5}'
        self.json_str2 = '{"name": "AfzalGhaffar", "language": "Sindhi", "id": "ENTOCR13RSCLZ6KU", "bio": "fjl;kdsajflk;asdjflksaj;fjl;kdsajflk;asdjflksaj;fjl;kd;asdjflksajk;asdjflksaj;fjl;kdsajflk;asdjflksaj;V59O0V59OF92YF627HFY0V59OF92YF627HFY0V59OF92YF627HFY0V59OF9F92YF627HFY0V59OF92YF627HFY0V59OF92YF627HFY0V59O0V59OF92YF627HFY0V59OF92YF627HFY0V59OF92YF627HFY0V59OF9F92YF627HFY0V59OF92YF627HFY0V59OF92YF627HFY0", "version": 1}'
        self.json_str3 = '{"name": "AamirSolangi", "language": "Sindhi", "id": "IAKPO3R4761JDRVG", "bio": "VestibulumpharetraliberoetvelitgravidaeuismodQuisquemaurisligulaefficiturporttitorsodalesaclacinianonexFusceeuultriceselitvelposuereneque.", "version": 7}'

    def test_case_1(self):
        dict_obj = cjson.loads(self.json_str)
        cjson_str_res = cjson.dumps(dict_obj)
        self.assertEqual(cjson_str_res, self.json_str)

    def test_case_2(self):
        dict_obj = cjson.loads(self.json_str2)
        json_str_res = cjson.dumps(dict_obj)
        self.assertEqual(json_str_res, self.json_str2)

    def test_case_3(self):
        dict_obj = cjson.loads(self.json_str3)
        json_str_res = cjson.dumps(dict_obj)
        self.assertEqual(json_str_res, self.json_str3)


if __name__ == '__main__':
    unittest.main()

import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    def test_comment_1(self):
        """test comment 1"""
        self.assertTrue(TestLexer.checkLexeme(""" "/* abc */" ""","""/* abc */,<EOF>""" ,1))
    def test_comment_2(self):
        """test comment 2"""
        self.assertTrue(TestLexer.checkLexeme(""" "/* def// */" ""","""/* def// */,<EOF>""" ,2))
    def test_comment_3(self):
        """test comment 3"""
        self.assertTrue(TestLexer.checkLexeme("""/* //aaaaaaaa */""","<EOF>",3))
    def test_comment_4(self):
        """test comment 4"""
        self.assertTrue(TestLexer.checkLexeme("""/* minhde// */""","<EOF>",4))
    def test_comment_5(self):
        """test comment 5"""
        self.assertTrue(TestLexer.checkLexeme("""/* linhtam\m\ab */""","<EOF>",5))
    def test_comment_6(self):
        """test comment 6"""
        self.assertTrue(TestLexer.checkLexeme("""// abcd""","<EOF>",6))
    def test_line_comment_7(self):
        """test comment 7"""
        self.assertTrue(TestLexer.checkLexeme("""//abcdef  /* asadasdas */""","<EOF>",7))
    def test_line_comment_8(self):
        """test comment 8"""
        self.assertTrue(TestLexer.checkLexeme(""" //abc \\n bef ""","<EOF>",8))
    def test_line_comment_9(self):
        """test comment 9"""
        self.assertTrue(TestLexer.checkLexeme(""" //abcdef/12f ""","<EOF>",9))
    def test_line_comment_10(self):
        """test comment 10"""
        self.assertTrue(TestLexer.checkLexeme(""" //abc /*abcdef*/ ""","<EOF>",10))    
    def test_separators_11(self):
        """test separators 11"""
        self.assertTrue(TestLexer.checkLexeme(""" [ba[b]a[ba][a]b[ab][a {12312}{123{}{}{ (abv12)(())(Aasd) ""","[,ba,[,b,],a,[,ba,],[,a,],b,[,ab,],[,a,{,12312,},{,123,{,},{,},{,(,abv12,),(,(,),),(,Aasd,),<EOF>",11))
    def test_separators_12(self):
        """test separators 12"""
        self.assertTrue(TestLexer.checkLexeme(""" ..minh...de.... ""","Error Token .",12))
    def test_separators_13(self):
        """test separators 13"""
        self.assertTrue(TestLexer.checkLexeme(""" abc;def,chung ""","abc,;,def,,,chung,<EOF>",13))
    def test_separators_14 (self):
        """test separators 14 """
        self.assertTrue(TestLexer.checkLexeme(""" { ] ( ; . , ""","{,],(,;,Error Token .",14))
    def test_separators_15(self):
        """test separators 15"""
        self.assertTrue(TestLexer.checkLexeme(""" [b] ""","[,b,],<EOF>",15))
    def test_operators_16(self):
        """test operators 16"""
        self.assertTrue(TestLexer.checkLexeme(""" a = b + c ""","a,=,b,+,c,<EOF>",16))
    def test_operators_17(self):
        """test operators 17"""
        self.assertTrue(TestLexer.checkLexeme(""" d < e ""","d,<,e,<EOF>",17))
    def test_operators_18(self):
        """test operators 18 """
        self.assertTrue(TestLexer.checkLexeme(""" abc*def - gh ""","abc,*,def,-,gh,<EOF>",18))
    def test_operators_19(self):
        """test operators 19"""
        self.assertTrue(TestLexer.checkLexeme(""" ab!=cd  ""","ab,!=,cd,<EOF>",19))
    def test_operators_20(self):
        """test operators 20"""
        self.assertTrue(TestLexer.checkLexeme(""" abc<=def 5/10 ""","abc,<=,def,5,/,10,<EOF>",20))
    def test_operators_21(self):
        """test operators 21"""
        self.assertTrue(TestLexer.checkLexeme(""" a||b||c! ""","a,||,b,||,c,!,<EOF>",21))
    def test_operators_22(self):
        """test operators 22"""
        self.assertTrue(TestLexer.checkLexeme(""" abc&&de gh%ef ""","abc,&&,de,gh,%,ef,<EOF>",22))
    def test_operators_23(self):
        """test operators 23"""
        self.assertTrue(TestLexer.checkLexeme(""" a>b c<e f>=g ""","a,>,b,c,<,e,f,>=,g,<EOF>",23))
    def test_operators_24(self):
        """test operators 24"""
        self.assertTrue(TestLexer.checkLexeme(""" 2*5 = 7+3 ""","2,*,5,=,7,+,3,<EOF>",24))
    def test_operators_25(self):
        """test operators 25"""
        self.assertTrue(TestLexer.checkLexeme(""" 10/2=5 4%a!=0 ""","10,/,2,=,5,4,%,a,!=,0,<EOF>",25))
    def test_integer_26(self):
        """test integers 26"""
        self.assertTrue(TestLexer.checkLexeme(""" 123 ""","123,<EOF>",26))
    def test_integer_27(self):
        """test integers 27"""
        self.assertTrue(TestLexer.checkLexeme(""" 0 5 10 ""","0,5,10,<EOF>",27))
    def test_integer_28(self):
        """test integers 28"""
        self.assertTrue(TestLexer.checkLexeme(""" 123_123 ""","123,_123,<EOF>",28))
    def test_integer_29(self):
        """test integers 29"""
        self.assertTrue(TestLexer.checkLexeme(""" 3200 ""","3200,<EOF>",29))
    def test_integer_30(self):
        """test integers 30"""
        self.assertTrue(TestLexer.checkLexeme(""" 100*200=20000 ""","100,*,200,=,20000,<EOF>",30))
    def test_integer_31(self):
        """test integers 31"""
        self.assertTrue(TestLexer.checkLexeme(""" 123 + 456 = 579 ""","123,+,456,=,579,<EOF>",31))
    def test_integer_32(self):
        """test integers 32"""
        self.assertTrue(TestLexer.checkLexeme(""" 123___456 ""","123,___456,<EOF>",32))
    def test_integer_33(self):
        """test integers 33"""
        self.assertTrue(TestLexer.checkLexeme(""" 1000000000000000 ""","1000000000000000,<EOF>",33))
    def test_integer_34(self):
        """test integers 34"""
        self.assertTrue(TestLexer.checkLexeme(""" _123 456_ 7_59 ""","_123,456,_,7,_59,<EOF>",34))
    def test_integer_35(self):
        """test integers 35"""
        self.assertTrue(TestLexer.checkLexeme(""" 123 + b123 ""","123,+,b123,<EOF>",35))
    def test_float_36(self):
        """test float 36"""
        self.assertTrue(TestLexer.checkLexeme(""" 1.2 ""","""1.2,<EOF>""",36))
    def test_float_37(self):
        """test float 37"""
        self.assertTrue(TestLexer.checkLexeme(""" 1.2.3 ""","""1.2,.3,<EOF>""",37))
    def test_float_38(self):
        """test float 38"""
        self.assertTrue(TestLexer.checkLexeme(""" 1. ""","""1.,<EOF>""",38))
    def test_float_39(self):
        """test float 39"""
        self.assertTrue(TestLexer.checkLexeme(""" 1e2 ""","""1e2,<EOF>""",39))
    def test_float_40(self):
        """test float 40"""
        self.assertTrue(TestLexer.checkLexeme(""" 1.2E-2 ""","""1.2E-2,<EOF>""",40))
    def test_float_41(self):
        """test float 41"""
        self.assertTrue(TestLexer.checkLexeme(""" 1E2 ""","""1E2,<EOF>""",41))
    def test_float_42(self):
        """test float 42"""
        self.assertTrue(TestLexer.checkLexeme(""" 9.0 ""","""9.0,<EOF>""",42))
    def test_float_43(self):
        """test float 43"""
        self.assertTrue(TestLexer.checkLexeme(""" 12E8 ""","""12E8,<EOF>""",43))
    def test_float_44(self):
        """test float 44"""
        self.assertTrue(TestLexer.checkLexeme(""" 0.33E-3 ""","""0.33E-3,<EOF>""",44))
    def test_float_45(self):
        """test float 45"""
        self.assertTrue(TestLexer.checkLexeme(""" 128E-42""","""128E-42,<EOF>""",45))
    def test_float_46(self):
        """test float 46"""
        self.assertTrue(TestLexer.checkLexeme(""" 1.2 + 3.4 = 4.6 ""","""1.2,+,3.4,=,4.6,<EOF>""",46))
    def test_float_47(self):
        """test float 47"""
        self.assertTrue(TestLexer.checkLexeme(""" .1E2 """,""".1E2,<EOF>""",47))
    def test_float_48(self):
        """test float 48"""
        self.assertTrue(TestLexer.checkLexeme(""" _1.2 ""","""_1,.2,<EOF>""",48))
    def test_float_49(self):
        """test float 49"""
        self.assertTrue(TestLexer.checkLexeme(""" 12. 1e98 ""","""12.,1e98,<EOF>""",49))
    def test_float_50(self):
        """test float 50"""
        self.assertTrue(TestLexer.checkLexeme(""" abc3.45 ""","""abc3,.45,<EOF>""",50))
    def test_string_51(self):
        """test float 51"""
        self.assertTrue(TestLexer.checkLexeme(""" "" """,""",<EOF>""",51))
    def test_string_52(self):
        """test float 52"""
        self.assertTrue(TestLexer.checkLexeme(""" "abcde" ""","""abcde,<EOF>""",52))
    def test_string_53(self):
        """test float 53"""
        self.assertTrue(TestLexer.checkLexeme(""" "abcd\\b \\f" ""","""abcd\\b \\f,<EOF>""",53))
    def test_string_54(self):
        """test float 54"""
        self.assertTrue(TestLexer.checkLexeme(""" "abcd\\r\\n" ""","""abcd\\r\\n,<EOF>""",54))
    def test_string_55(self):
        """test float 55"""
        self.assertTrue(TestLexer.checkLexeme(""" "abcd\\t" ""","""abcd\\t,<EOF>""",55))
    def test_unclose_string_56(self):
        """test unclose string"""
        self.assertTrue(TestLexer.checkLexeme(""" "123a\\n123 ""","""Unclosed String: 123a\\n123 """,56))
    def test_unclose_string_57(self):
        """test unclose string"""
        self.assertTrue(TestLexer.checkLexeme(""" "abcd ""","""Unclosed String: abcd """,57))
    def test_illegal_escape_58(self):
        """test illegal escape"""
        self.assertTrue(TestLexer.checkLexeme(""" 123 "12\\k" ""","""123,Illegal Escape In String: 12\\k""",58))
    def test_double_slash_59(self):
        """test double slash"""
        self.assertTrue(TestLexer.checkLexeme(""" "abc\\\nabc" ""","""Illegal Escape In String: abc\\\n""",59))
    def test_string_60(self):
        """test string"""
        self.assertTrue(TestLexer.checkLexeme(""" "\\\\fabc\\\\rabc" ""","""\\\\fabc\\\\rabc,<EOF>""",60))
    def test_string_61(self):
        """test string"""
        self.assertTrue(TestLexer.checkLexeme(""" "abc\\bcd\\fghe\\t" ""","""abc\\bcd\\fghe\\t,<EOF>""",61))
    def test_string_62(self):
        """test string"""
        self.assertTrue(TestLexer.checkLexeme(""" "abcd" "ef" ""","""abcd,ef,<EOF>""",62))
    def test_string_63(self):
        """test string"""
        self.assertTrue(TestLexer.checkLexeme(""" "abc"abc" ""","""abc,abc,Unclosed String:  """,63))
    def test_string_64(self):
        """test string"""
        self.assertTrue(TestLexer.checkLexeme(""" "abc\\" ""","""Unclosed String: abc\\" """,64))
    def test_string_65(self):
        """test string"""
        self.assertTrue(TestLexer.checkLexeme(""" "abc\\rabc" ""","""abc\\rabc,<EOF>""",65))
    def test_string_66(self):
        """test Unclosed string"""
        self.assertTrue(TestLexer.checkLexeme(""" abc "abc ""","""abc,Unclosed String: abc """,66))
    def test_string_67(self):
        """test Illegal String"""
        self.assertTrue(TestLexer.checkLexeme(""" "abcd\\m" ""","""Illegal Escape In String: abcd\\m""",67))
    def test_string_68(self):
        """test Unclosed String"""
        self.assertTrue(TestLexer.checkLexeme(""" "abc\nabc" ""","""Unclosed String: abc""",68))
    def test_string_69(self):
        """test Illegal String"""
        self.assertTrue(TestLexer.checkLexeme(""" 123 "12\\t3\\am123" ""","""123,Illegal Escape In String: 12\\t3\\a""",69))
    def test_string_70(self):
        """test Illegal String"""
        self.assertTrue(TestLexer.checkLexeme(""" abc "abc\\a" abc ""","""abc,Illegal Escape In String: abc\\a""",70))
    # def test_string_71(self):
    #     """test Illegal String"""
    #     self.assertTrue(TestLexer.checkLexeme(""" int main () {
    #          inPut(4);
    #      }
    #      } ""","""<EOF>""",71))


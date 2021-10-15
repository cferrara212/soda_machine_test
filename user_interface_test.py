import unittest
from cans import Cola, OrangeSoda, RootBeer
import coins
from user_interface import try_parse_int, validate_main_menu, get_unique_can_names,display_payment_value, validate_coin_selection



class TestValidateMainMenue(unittest.TestCase):
    
    def test_validate_main_menue_1(self):
        
        is_valid = validate_main_menu(1)
        self.assertEqual((True,1),is_valid)

    def test_validate_main_menue_2(self):
        
        is_valid = validate_main_menu(2)
        self.assertEqual((True,2),is_valid)

    def test_validate_main_menue_3(self):
        
        is_valid = validate_main_menu(3)
        self.assertEqual((True,3),is_valid)

    def test_validate_main_menue_4(self):
        
        is_valid = validate_main_menu(4)
        self.assertEqual((True,4),is_valid)

    def test_validate_main_menue_5(self):
        
        is_valid = validate_main_menu(5)
        self.assertEqual((False,None),is_valid)
    
class TestTryParse(unittest.TestCase):

    def test_try_parse_10(self):
        check = try_parse_int(10)
        self.assertEqual(10,check)
    
    def test_try_parse_0(self):
        check = try_parse_int(0)
        self.assertEqual(0,check)


class TestGetUniqueCanNames (unittest.TestCase):

    def setUp(self):
        self.cola1= Cola()
        self.cola2= Cola()
        self.orange1= OrangeSoda()
        self.orange2= OrangeSoda()
        self.root1= RootBeer()
        self.root2= RootBeer()

    def test_get_unique_can_names(self):
        can_list= []
        can_list.append(self.cola1)
        can_list.append(self.cola2)
        can_list.append(self.orange1)
        can_list.append(self.orange2)
        can_list.append(self.root1)
        can_list.append(self.root2)

        names_list = get_unique_can_names(can_list)
        self.assertEqual(3,len(names_list))

    def test_get_unique_can_names_empty(self):
        can_list = []
        names_list = get_unique_can_names(can_list)
        self.assertEqual(0,len(names_list))

   
class TestDisplayPaymentValue(unittest.TestCase):    

    def test_display_payment_value(self):
        self.quarter = coins.Quarter()
        self.dime = coins.Dime()
        self.nickel = coins.Nickel()
        self.penny = coins.Penny()
        
        money_list = []
        money_list.append(self.quarter)
        money_list.append(self.dime)
        money_list.append(self.nickel)
        money_list.append(self.penny)

        pay_value = display_payment_value(money_list)
        self.assertEqual(.41,pay_value)

    def test_display_payment_value_0(self):
        money_list= []
        pay_value = display_payment_value(money_list)
        self.assertEqual(0,pay_value)

class TestValidateCoinSelection(unittest.TestCase):

    def test_validate_coin_selection_quarter(self):
        validation = validate_coin_selection(1)
        self.assertEqual((True,'Quarter'),validation)

    def test_validate_coin_selection_dime(self):
        validation = validate_coin_selection(2)
        self.assertEqual((True,'Dime'),validation)

    def test_validate_coin_selection_nickel(self):
        validation = validate_coin_selection(3)
        self.assertEqual((True,'Nickel'),validation)

    def test_validate_coin_selection_penny(self):
        validation = validate_coin_selection(4)
        self.assertEqual((True,'Penny'),validation)

    def test_validate_coin_selection_done(self):
        validation = validate_coin_selection(5)
        self.assertEqual((True,'Done'),validation)

    def test_validate_coin_selection_none(self):
        validation = validate_coin_selection(6)
        self.assertEqual((False,None),validation)

if __name__ == '__main__':
    unittest.main()
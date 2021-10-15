import unittest
from cans import Cola, OrangeSoda
import coins
from soda_machine import SodaMachine


class TestFillRegister(unittest.TestCase):

    def setUp(self):
        self.soda_machine = SodaMachine()

    def test_machine_fill(self):
        self.assertEqual(88, len(self.soda_machine.register))


class TestFillInventory(unittest.TestCase):
    
    def setUp(self):
        self.soda_machine = SodaMachine()
    def test_fill_inventory(self):
        self.assertEqual(30, len(self.soda_machine.inventory))


class TestGetCoinFromRegister(unittest.TestCase):

    def setUp(self):
        self.soda_machine = SodaMachine()

    def test_get_coin_from_register_quarter(self):
        coin = self.soda_machine.get_coin_from_register('Quarter')
        self.assertEqual('Quarter',coin.name)

    def test_get_coin_from_register_dime(self):
        coin = self.soda_machine.get_coin_from_register('Dime')
        self.assertEqual('Dime',coin.name)

    def test_get_coin_from_register_nickel(self):
        coin = self.soda_machine.get_coin_from_register('Nickel')
        self.assertEqual('Nickel',coin.name)

    def test_get_coin_from_register_penny(self):
        coin = self.soda_machine.get_coin_from_register('Penny')
        self.assertEqual('Penny',coin.name)

    def test_get_coin_from_register_none(self):
        coin = self.soda_machine.get_coin_from_register('chickens')
        self.assertIsNone(coin)

class TestRegisterHasCoin(unittest.TestCase):

    def setUp(self):
        self.soda_machine = SodaMachine()

    def test_register_has_coin_quarter(self):
        coin = self.soda_machine.register_has_coin('Quarter')
        self.assertTrue(coin)

    def test_register_has_coin_dime(self):
        coin = self.soda_machine.register_has_coin('Dime')
        self.assertTrue(coin)

    def test_register_has_coin_nickel(self):
        coin = self.soda_machine.register_has_coin('Nickel')
        self.assertTrue(coin)

    def test_register_has_coin_penny(self):
        coin = self.soda_machine.register_has_coin('Penny')
        self.assertTrue(coin)

    def test_register_has_coin_false(self):
        coin = self.soda_machine.register_has_coin('Half Dollar')
        self.assertFalse(coin)

class TestChangeValue(unittest.TestCase):

    def setUp(self):
        self.soda_machine = SodaMachine()

    def test_determine_change_value_more(self):
        change = self.soda_machine.determine_change_value(.5,.4)
        self.assertEqual(.10,change)
    
    def test_determine_change_value_less(self):
        change = self.soda_machine.determine_change_value(.5,.6)
        self.assertEqual(-.1,change)

    def test_determine_change_value(self):
        change = self.soda_machine.determine_change_value(.5,.5)
        self.assertEqual(0, change)

class TestCalculateCoinValue(unittest.TestCase):

    def setUp(self):
        self.soda_machine = SodaMachine()
        self.quarter = coins.Quarter()
        self.dime = coins.Dime()
        self.nickel = coins.Nickel()
        self.penny = coins.Penny()
        

    def test_calculate_coin_value(self):
        all_my_money = []
        all_my_money.append(coins.Quarter())
        all_my_money.append(coins.Dime())
        all_my_money.append(coins.Nickel())
        all_my_money.append(coins.Penny())

        coin_value = self.soda_machine.calculate_coin_value(all_my_money)
        self.assertEqual(.41,coin_value)

    def test_calculate_coin_value(self):
        all_my_money = []
        
        coin_value = self.soda_machine.calculate_coin_value(all_my_money)
        self.assertEqual(0,coin_value)

class TestGetInventorySoda(unittest.TestCase):

    def setUp(self):
        self.soda_machine = SodaMachine()

    def test_get_inventory_soda_cola(self):
        soda = self.soda_machine.get_inventory_soda('Cola')
        self.assertEqual('Cola',soda.name)

    def test_get_inventory_soda_orange(self):
        soda = self.soda_machine.get_inventory_soda('Orange Soda')
        self.assertEqual('Orange Soda',soda.name)

    def test_get_inventory_soda_root(self):
        soda = self.soda_machine.get_inventory_soda('Root Beer')
        self.assertEqual('Root Beer',soda.name)

    def test_get_inventory_soda_none(self):
        soda = self.soda_machine.get_inventory_soda('Mountain Dew')
        self.assertIsNone(soda)

class TestReturnInventory(unittest.TestCase):
    def setUp(self):
        self.soda_machine = SodaMachine()
        self.cola = Cola()
    
    def test_return_inventory(self):
        self.soda_machine.return_inventory(self.cola)
        self.assertEqual(31,len(self.soda_machine.inventory))

class TestDepositCoins(unittest.TestCase):
    
    def setUp(self):
        self.soda_machine = SodaMachine()
        self.quarter = coins.Quarter()
        self.dime = coins.Dime()
        self.nickel = coins.Nickel()
        self.penny = coins.Penny()

    def test_deposit_coins_into_register(self):
        coins_list = []
        coins_list.append(coins.Quarter())
        coins_list.append(coins.Dime())
        coins_list.append(coins.Nickel())
        coins_list.append(coins.Penny())

        self.soda_machine.deposit_coins_into_register(coins_list)
        self.assertEqual(92,len(self.soda_machine.register))


if __name__ == '__main__':
    unittest.main()
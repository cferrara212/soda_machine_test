import unittest
from customer import Customer
import coins
import cans




class TestGetWalletCoin(unittest.TestCase):
    def setUp(self):
        self.customer= Customer()

    def test_get_wallet_coin_quarter(self):
        coin = self.customer.get_wallet_coin('Quarter')
        self.assertEqual('Quarter',coin.name)
    
    def test_get_wallet_coin_dime(self):
        coin = self.customer.get_wallet_coin('Dime')
        self.assertEqual('Dime',coin.name)
    
    def test_get_wallet_coin_nickel(self):
        coin = self.customer.get_wallet_coin('Nickel')
        self.assertEqual('Nickel',coin.name)
    
    def test_get_wallet_coin_penny(self):
        coin = self.customer.get_wallet_coin('Penny')
        self.assertEqual('Penny',coin.name)

    def test_get__wallet_coin_string(self):
        isnone = self.customer.get_wallet_coin('chicken')
        self.assertIsNone(isnone)





class TestAddCoinsToWallet(unittest.TestCase):
    def setUp(self):
        self.customer=Customer()


    def test_add_coins_to_wallet_quarter(self):
        coin_original_qty = 0
        for coin in self.customer.wallet.money:
            if coin.name == "Quarter":
                coin_original_qty += 1
        self.customer.add_coins_to_wallet([coins.Quarter()])
        coin_updated_qty = 0
        for coin in self.customer.wallet.money:
            if coin.name == "Quarter":
                coin_updated_qty += 1

        self.assertEqual((coin_original_qty +1),coin_updated_qty)
    
    def test_add_coins_to_wallet_list(self):
        wallet_length = len(self.customer.wallet.money)
        self.customer.add_coins_to_wallet([coins.Dime(),coins.Quarter(),coins.Penny()])
        self.assertEqual((wallet_length + 3),len(self.customer.wallet.money))
        
    def test_add_empty_list(self):
        self.customer.add_coins_to_wallet([])
        self.assertEqual(len(self.customer.wallet.money),len(self.customer.wallet.money))
    


class TestAddCanToBackpack(unittest.TestCase):
    def setUp(self):
        self.customer = Customer()


    def test_add_can_to_backpack_cola(self):
        self.customer.add_can_to_backpack("Cola")
        print(self.customer.backpack.purchased_cans[0])
        self.assertEqual('Cola', self.customer.backpack.purchased_cans[0])
    def test_add_can_to_backpack_orange(self):
        self.customer.add_can_to_backpack_root('Orange Soda')
        self.assertEqual('Orange Soda',self.customer.backpack.purchased_cans[0])
    def test_add_can_to_backpack_orange(self):
        self.customer.add_can_to_backpack('Root Beer')
        self.assertEqual('Root Beer', self.customer.backpack.purchased_cans[0])



if __name__ == '__main__':
    unittest.main()
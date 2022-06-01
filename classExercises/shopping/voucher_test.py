import unittest
from . import basket_voucher


class BasketVoucherTest(unittest.TestCase):
    def setUp(self) -> None:
        self.cart = basket_voucher.BasketVoucher()

    def test_that_BasketVoucher_class_exists(self):
        self.assertIsNotNone(self.cart)

    def test_that_voucher_can_be_set(self):
        self.cart.cart_can_take_only(3)
        self.assertEqual(3, self.cart.voucher)

    def test_that_items_can_be_added_to_basket(self):
        self.cart.cart_can_take_only(3)
        self.cart.add("Kilishi")
        self.assertEqual(1, self.cart.number_of_items())
        self.cart.add("Suya")
        self.assertEqual(2, self.cart.number_of_items())

    def test_that_items_cannot_exceed_set_voucher(self):
        self.cart.cart_can_take_only(2)
        self.cart.add("Kilishi")
        self.cart.add("Sugar")
        self.cart.add("Maggi")
        self.assertEqual(2, self.cart.number_of_items())

    def test_that_items_in_basket_replaces_automatically(self):
        self.cart.cart_can_take_only(2)
        self.cart.add("Kilishi")
        self.cart.add("Sugar")
        self.cart.add("Milk")
        self.assertEqual(["Sugar", "Milk"], self.cart.items)

    def test_that_items_in_basket_can_be_replaced(self):
        self.cart.cart_can_take_only(3)
        self.cart.add("Kilishi")
        self.cart.add("Sugar")
        self.cart.add("Plantain")
        self.cart.replace("Sugar", "Milk")
        self.assertEqual(["Kilishi", "Milk", "Plantain"], self.cart.items)

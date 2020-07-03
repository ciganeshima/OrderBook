from unittest import TestCase
from main import OrderBook


class TestOrderBook(TestCase):
    def test_update_level_add(self):
        book1 = OrderBook()
        book1.update_level(2, 4, True)
        assert book1.levels_buy == [[(2,4)]]

    def test_update_level_add_to_buy_list(self):
        book1 = OrderBook()
        book1.update_level(2, 4, True)
        assert book1.levels_buy == [[(2, 4)]]
        assert book1.levels_sell == []

    def test_update_level_add_to_sell_list(self):
        book1 = OrderBook()
        book1.update_level(2, 4, False)
        assert book1.levels_buy == []
        assert book1.levels_sell == [[(2, 4)]]

    def test_update_level_add_zero_volume(self):
        book1 = OrderBook()
        book1.update_level(2, 0, True)
        assert book1.levels_buy == []

    def test_update_level_change(self):
        book1 = OrderBook()
        book1.update_level(2, 4, True)
        book1.update_level(2, 3, True)
        assert book1.levels_buy == [[(2,3)]]

    def test_update_level_delete(self):
        book1 = OrderBook()
        book1.update_level(3, 1, True)
        book1.update_level(2, 4, True)
        book1.update_level(2, 0, True)
        assert book1.levels_buy == [[(3,1)]]

    def test_get_best_bbo_general(self):
        book1 = OrderBook()
        book1.update_level(2, 4, True)
        book1.update_level(3, 5, False)
        assert book1.get_best_bbo() == (2, 4, 3, 5)

    def test_get_best_bbo_general_extended(self):
        book1 = OrderBook()
        book1.update_level(2, 4, True)
        book1.update_level(8, 6, True)
        book1.update_level(3, 5, False)
        book1.update_level(1, 2, False)
        assert book1.get_best_bbo() == (8, 6, 3, 5)

    def test_get_best_bbo_empty_lists(self):
        book1 = OrderBook()
        book1.update_level(2, 0, True)
        book1.update_level(3, 0, False)
        assert book1.get_best_bbo() == (None, None, None, None)

    def test_get_best_bbo_empty_sell_list(self):
        book1 = OrderBook()
        book1.update_level(2, 4, True)
        assert book1.get_best_bbo() == (2, 4, None, None)

    def test_get_best_bbo_empty_buy_list(self):
        book1 = OrderBook()
        book1.update_level(2, 4, False)
        assert book1.get_best_bbo() == (None, None, 2, 4)

    def test_get_levels_general(self):
        book1 = OrderBook()
        book1.update_level(2, 4, True)
        book1.update_level(3, 4, True)
        book1.update_level(5, 2, False)
        book1.update_level(3, 1, False)
        assert book1.get_levels() == (([(3,4)], [(2, 4)]),([(3,1)],[(5, 2)]))

    def test_get_levels_general_empty_sell_list(self):
        book1 = OrderBook()
        book1.update_level(2, 4, True)
        book1.update_level(3, 4, True)
        assert book1.get_levels() == (([(3, 4)],[(2, 4)]), ())

    def test_get_levels_general_empty_buy_list(self):
        book1 = OrderBook()
        book1.update_level(2, 4, False)
        book1.update_level(3, 4, False)
        assert book1.get_levels() == ((), ([(2, 4)],[(3, 4)]))


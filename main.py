from operator import itemgetter
from typing import List, Tuple, Union


class OrderBook:
    def __init__(self):
        self.levels_buy: List = []
        self.levels_sell: List = []

    def update_level(self, level_price: float, level_vol: float, is_buy: bool):
        """
        Updates order book level.

        :param level_price: Price of level.
        :param level_vol: Volume of level.
            If 'volume' == 0 then it means that
            level corresponding to 'price' must
            be deleted.
            If 'volume' > 0 then it means that
            level corresponding to 'price' has
            new volume equal to 'volume'.
        :param is_buy: Indicates whether
            the level corresponds to buy level or
            sell level.
        :return:
        """
        self.level_price = level_price
        self.level_vol = level_vol
        self.is_buy = is_buy
        flag = 0  # flag, that indicates about adding or changing levels; if flag = 0 then change param in level, if flag = 1 then add level

        if is_buy:  # if is_buy field True then work with buy list
            if not self.levels_buy and self.level_vol:  # if there's empty list and not '0' volume, then add new level
                self.levels_buy.append([(self.level_price, self.level_vol)])
            else:
                if not level_vol:
                    for i in self.levels_buy:
                        if level_price == i[0][0]:  # i - > list(tuple(float1,float2)) , i[0] -> tuple(float1,float2), i[0][0] -> float1
                            self.levels_buy.remove(i)
                else:
                    for i in self.levels_buy:
                        if level_price == i[0][0]:  # i - > list(tuple(float1,float2)) , i[0] -> tuple(float1,float2), i[0][0] -> float1
                            self.levels_buy[self.levels_buy.index(i)] = [(self.level_price, self.level_vol)]
                            flag = 0
                            #  replacing old tuple containing old data with the new data
                            break
                        else:
                            flag = 1
                if flag == 1:
                    self.levels_buy.append([(self.level_price, self.level_vol)])

        else:  # if is_buy filed False then work with sell list
            if not self.levels_sell and self.level_vol:  # if there's empty list and not '0' volume, then add new level
                self.levels_sell.append([(self.level_price, self.level_vol)])
            else:
                if not level_vol:
                    for j in self.levels_sell:
                        if level_price == j[0][0]:  # j - > list(tuple(float1,float2)) , j[0] -> tuple(float1,float2), j[0][0] -> float1
                            self.levels_sell.remove(j)
                else:
                    for j in self.levels_sell:
                        if level_price == j[0][0]:  # i - > list(tuple(float1,float2)) , i[0] -> tuple(float1,float2), i[0][0] -> float1
                            self.levels_sell[self.levels_sell.index(j)] = [(self.level_price, self.level_vol)]
                            flag = 0
                            break
                        else:
                            flag = 1
                    if flag == 1:
                        self.levels_sell.append([(self.level_price, self.level_vol)])

    def get_best_bbo(self) -> Tuple[Union[float, None], Union[float, None], Union[float, None], Union[float, None]]:
        """
        Return best buy level price, volume and
        best sell level price, volume.

        If buy side is empty then best buy level
        price and volume equal None. The same goes
        for empty sell side.

        :return Tuple[float, float, float, float]:
            Best buy level price, best buy level volume,
            best sell level price, best sell level volume.
        """

        if self.levels_buy:
            if self.levels_sell:
                bests = (max(self.levels_buy, key=itemgetter(0))[0][0], max(self.levels_buy, key=itemgetter(0))[0][1],
                         max(self.levels_sell, key=itemgetter(0))[0][0], max(self.levels_sell, key=itemgetter(0))[0][1])
                # max...[0] -> tuple(float1,float2), max...[0][0] -> float1, max...[0][1] -> float2
            else:
                bests = (max(self.levels_buy, key=itemgetter(0))[0][0], max(self.levels_buy, key=itemgetter(0))[0][1],
                         None, None)
        else:
            if self.levels_sell:
                bests = (None, None, max(self.levels_sell, key=itemgetter(0))[0][0], max(self.levels_sell,
                                                                                         key=itemgetter(0))[0][1])
            else:
                bests = (None, None, None, None)
        return bests

    def get_levels(self) -> Tuple[List[Tuple[float, float]], List[Tuple[float, float]]]:
        """
        Returns all current buy levels in descending
        order and all current sell levels in ascending order.

        Each level is described as List[Tuple[float, float]]. Where
        each tuple corresponds to level and the first value in each
        tuple corresponds price of level and the second value to
        volume the level

        The method should not return levels with 0 volume.

        :return Tuple[List[Tuple[float, float]], List[Tuple[float, float]]]:
            The first tuple is buy levels, the second tuple sell levels.
        """

        self.levels_buy.sort(reverse=True)
        self.levels_sell.sort()

        return tuple(self.levels_buy), tuple(self.levels_sell)

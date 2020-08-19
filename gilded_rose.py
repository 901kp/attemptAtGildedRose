# -*- coding: utf-8 -*-

class GildedRose(object):

    def whatTypeItem(self, src):
        if ("Conjured" in src):
            return 4
        types={
            "Aged Brie": 1,
            "Sulfuras, Hand of Ragnaros": 2,
            "Backstage passes to a TAFKAL80ETC concert": 3}
        return types.get(src, 5)

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            itemName = item.name
            n = self.whatTypeItem(itemName)

            # 1 is Aged Brie's type: quality only raises
            if n == 1:
                item.quality += 1

            # 2 is the Sulfur's hand type: quality and sell in date don't change

            # 3 is the backstage pass: quality changes, depending how many days are left
            if n == 3:
                # if 0 - quality is 0
                if item.sell_in <= 0:
                    item.quality = 0
                #if 5 or less - quality raises by 
                elif item.sell_in <= 5:
                    item.quality *= 3
                #if 10 or less - quality raises by
                elif item.sell_in <= 10:
                    item.quality *= 2
                else:
                    item.quality += 1

            # 4 is conjured items' type: these degrade twice as fast
            if n == 4:
                item.quality -= 2
            # 5 is type of everything else: quality degrades by 1 daily
            if n == 5:
                item.quality -= 1

            # change the sell in date; except for the hand
            if n != 2:
                item.sell_in -= 1

            #make sure the quality isn't above 50 or below 0
            if item.quality < 0:
                item.quality = 0
            if item.quality > 50:
                item.quality = 50

    

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
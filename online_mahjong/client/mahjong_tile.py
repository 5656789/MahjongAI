# -*- coding: utf-8 -*-

__author__ = "Jianyang Tang"
__email__ = "jian4yang2.tang1@gmail.com"

class Tile:

    tile_dict = {11: 0, 12: 1, 13: 2, 14: 3, 15: 4, 16: 5, 17: 6, 18: 7, 19: 8,
                 21: 9, 22: 10, 23: 11, 24: 12, 25: 13, 26: 14, 27: 15, 28: 16, 29: 17,
                 31: 18, 32: 19, 33: 20, 34: 21, 35: 22, 36: 23, 37: 24, 38: 25, 39: 26,
                 41: 27, 42: 28, 43: 29, 44: 30, 45: 31, 46: 32, 47: 33,
                 51: 4, 52: 13, 53: 22}
    tile_graph_dict = [
        "🀇", "🀈", "🀉", "🀊", "🀋", "🀌", "🀍", "🀎", "🀏", "🀙", "🀚", "🀛", "🀜", "🀝", "🀞", "🀟", "🀠", "🀡",
        "🀐", "🀑", "🀒", "🀓", "🀔", "🀕", "🀖", "🀗", "🀘", "🀀", "🀁", "🀂", "🀃", "🀆", "🀅", "🀄", "[🀋]", "[🀝]",
        "[🀔]"
    ]
    bonus_dict = {8: 0, 17: 9, 26: 18, 30: 27, 33: 31}

    EAST, SOUTH, WEST, NORTH = 27, 28, 29, 30
    BLANK, FORTUNE, CENTER = 31, 32, 33
    WINDS = [27, 28, 29, 30]
    THREES = [31, 32, 33]
    HONORS = [27, 28, 29, 30, 31, 32, 33]

    ONES, NINES = [0, 9, 18], [8, 17, 26]
    TERMINALS = [0, 8, 9, 17, 18, 26]
    ONENINE = [0, 8, 9, 17, 18, 26, 27, 28, 29, 30, 31, 32, 33]
    GREENS = [19, 20, 21, 23, 25, 32]
    GOOD_PAIR = ONENINE + [1, 7, 10, 16, 19, 25]

    RED_MAN, RED_PIN, RED_SOU = 16, 52, 88
    RED_BONUS = [16, 52, 88]

    index_to_chow = [[0, 1, 2], [1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 6, 7], [6, 7, 8],
                     [9, 10, 11], [10, 11, 12], [11, 12, 13], [12, 13, 14], [13, 14, 15], [14, 15, 16], [15, 16, 17],
                     [18, 19, 20], [19, 20, 21], [20, 21, 22], [21, 22, 23], [22, 23, 24], [23, 24, 25], [24, 25, 26]]

    desc = ['1m', '2m', '3m', '4m', '5m', '6m', '7m', '8m', '9m',
            '1p', '2p', '3p', '4p', '5p', '6p', '7p', '8p', '9p',
            '1s', '2s', '3s', '4s', '5s', '6s', '7s', '8s', '9s',
            'east', 'south', 'west', 'north', 'blank', 'fortune', 'center']

    @staticmethod
    def cal_bonus_tiles(bonus_indicators_34):
        p1_dict = {8: 0, 17: 9, 26: 18, 30: 27, 33: 31}
        if isinstance(bonus_indicators_34, int):
            return [p1_dict.get(bonus_indicators_34, bonus_indicators_34 + 1)]
        if isinstance(bonus_indicators_34, list):
            res = []
            for b in bonus_indicators_34:
                res.append(p1_dict.get(b, b + 1))
            return res

    @staticmethod
    def has_chow(tiles, chow):
        return all(t in tiles and t//9 == chow[0]//9 and t < 27 for t in chow)

    @staticmethod
    def tiles34_to_string(tiles):
        tiles.sort()
        man = [t for t in tiles if t < 9]
        pin = [t - 9 for t in tiles if 9 <= t < 18]
        suo = [t - 18 for t in tiles if 18 <= t < 27]
        chr = [t - 27 for t in tiles if t >= 27]
        m = man and ''.join([str(m + 1) for m in man]) + 'm' or ''
        p = pin and ''.join([str(p + 1) for p in pin]) + 'p' or ''
        s = suo and ''.join([str(b + 1) for b in suo]) + 's' or ''
        z = chr and ''.join([str(ch + 1) for ch in chr]) + 'z' or ''
        return m + p + s + z

    @staticmethod
    def t34_to_g(tiles):
        if isinstance(tiles, int):
            if tiles >= 0:
                return Tile.tile_graph_dict[tiles]
        if isinstance(tiles, list):
            if len(tiles) > 0 and isinstance(tiles[0], list):
                graphs = ""
                for meld in tiles:
                    graphs += ''.join([Tile.tile_graph_dict[t] for t in meld if t >= 0]) + " "
                return graphs
            else:
                graphs = [Tile.tile_graph_dict[t] for t in tiles if t >= 0]
                return ''.join(graphs)

    @staticmethod
    def tile136_to_string(tiles):
        tiles34 = [t//4 for t in tiles]
        return Tile.tiles34_to_string(tiles34)

    @staticmethod
    def t136_to_g(tiles):
        tiles34 = None
        if isinstance(tiles, int):
            tiles34 = tiles // 4
        if isinstance(tiles, list):
            if len(tiles) > 0 and isinstance(tiles[0], list):
                tiles34 = [[t // 4 for t in m] for m in tiles]
            else:
                tiles34 = [t // 4 for t in tiles]
        if tiles34:
            return Tile.t34_to_g(tiles34)
        else:
            return ""

    @staticmethod
    def print_partition(melds):
        res = ""
        for m in melds:
            res += Tile.t34_to_g(m) + " "
        print(res)

    @staticmethod
    def partition_graph(melds):
        res = ""
        for m in melds:
            res += Tile.t34_to_g(m) + " "
        return res

    @staticmethod
    def to_34(tiles):
        if isinstance(tiles, int):
            return Tile.tile_dict[tiles]
        elif isinstance(tiles, list):
            return [Tile.tile_dict[t] for t in tiles]
        else:
            print("Wrong parameters: Tile.to_34()")

    @staticmethod
    def indicator60_to_bonus(tiles60):
        if isinstance(tiles60, int):
            return Tile.bonus_dict.get(Tile.to_34(tiles60), Tile.to_34(tiles60) + 1)
        elif isinstance(tiles60, list):
            return [Tile.bonus_dict.get(t, t + 1) for t in Tile.to_34(tiles60)]
        else:
            print("Wrong parameters: Tile.indicator_to_bonus(tiles60)")

    @staticmethod
    def self_winds(dealer):
        return Tile.WINDS[(4 - dealer):] + Tile.WINDS[0:(4 - dealer)]

    @staticmethod
    def same_type(a, b):
        return a // 9 == b // 9


"""
MAN_KANS_SYM = ['🀇🀇🀇🀇', '🀈🀈🀈🀈', '🀉🀉🀉🀉', '🀊🀊🀊🀊', '🀋🀋🀋🀋', '🀌🀌🀌🀌', '🀍🀍🀍🀍', '🀎🀎🀎🀎',
                    '🀏🀏🀏🀏']
    PIN_KANS_SYM = ['🀙🀙🀙🀙', '🀚🀚🀚🀚', '🀛🀛🀛🀛', '🀜🀜🀜🀜', '🀝🀝🀝🀝', '🀞🀞🀞🀞', '🀟🀟🀟🀟', '🀠🀠🀠🀠',
                    '🀡🀡🀡🀡']
    SUO_KANS_SYM = ['🀐🀐🀐🀐', '🀑🀑🀑🀑', '🀒🀒🀒🀒', '🀓🀓🀓🀓', '🀔🀔🀔🀔', '🀕🀕🀕🀕', '🀖🀖🀖🀖', '🀗🀗🀗🀗',
                    '🀘🀘🀘🀘']
    CHR_KANS_SYM = ['🀀🀀🀀🀀', '🀁🀁🀁🀁', '🀂🀂🀂🀂', '🀃🀃🀃🀃', '🀆🀆🀆🀆', '🀅🀅🀅🀅', '🀄🀄🀄🀄']
    KANS_SYM = ['🀇🀇🀇🀇', '🀈🀈🀈🀈', '🀉🀉🀉🀉', '🀊🀊🀊🀊', '🀋🀋🀋🀋', '🀌🀌🀌🀌', '🀍🀍🀍🀍', '🀎🀎🀎🀎',
                '🀏🀏🀏🀏',
                '🀙🀙🀙🀙', '🀚🀚🀚🀚', '🀛🀛🀛🀛', '🀜🀜🀜🀜', '🀝🀝🀝🀝', '🀞🀞🀞🀞', '🀟🀟🀟🀟', '🀠🀠🀠🀠',
                '🀡🀡🀡🀡',
                '🀐🀐🀐🀐', '🀑🀑🀑🀑', '🀒🀒🀒🀒', '🀓🀓🀓🀓', '🀔🀔🀔🀔', '🀕🀕🀕🀕', '🀖🀖🀖🀖', '🀗🀗🀗🀗',
                '🀘🀘🀘🀘',
                '🀀🀀🀀🀀', '🀁🀁🀁🀁', '🀂🀂🀂🀂', '🀃🀃🀃🀃', '🀆🀆🀆🀆', '🀅🀅🀅🀅', '🀄🀄🀄🀄']

    MAN_KANS_NUM = [[0, 0, 0, 0], [1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4], [5, 5, 5, 5], [6, 6, 6, 6],
                    [7, 7, 7, 7], [8, 8, 8, 8]]
    PIN_KANS_NUM = [[9, 9, 9, 9], [10, 10, 10, 10], [11, 11, 11, 11], [12, 12, 12, 12], [13, 13, 13, 13],
                    [14, 14, 14, 14], [15, 15, 15, 15], [16, 16, 16, 16], [17, 17, 17, 17]]
    SUO_KANS_NUM = [[18, 18, 18, 18], [19, 19, 19, 19], [20, 20, 20, 20], [21, 21, 21, 21], [22, 22, 22, 22],
                    [23, 23, 23, 23], [24, 24, 24, 24], [25, 25, 25, 25], [26, 26, 26, 26]]
    CHR_KANS_NUM = [[27, 27, 27, 27], [28, 28, 28, 28], [29, 29, 29, 29], [30, 30, 30, 30], [31, 31, 31, 31],
                    [32, 32, 32, 32], [33, 33, 33, 33]]
    KANS_NUM = [[0, 0, 0, 0], [1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4], [5, 5, 5, 5], [6, 6, 6, 6],
                [7, 7, 7, 7], [8, 8, 8, 8],
                [9, 9, 9, 9], [10, 10, 10, 10], [11, 11, 11, 11], [12, 12, 12, 12], [13, 13, 13, 13], [14, 14, 14, 14],
                [15, 15, 15, 15], [16, 16, 16, 16], [17, 17, 17, 17],
                [18, 18, 18, 18], [19, 19, 19, 19], [20, 20, 20, 20], [21, 21, 21, 21], [22, 22, 22, 22],
                [23, 23, 23, 23], [24, 24, 24, 24], [25, 25, 25, 25], [26, 26, 26, 26],
                [27, 27, 27, 27], [28, 28, 28, 28], [29, 29, 29, 29], [30, 30, 30, 30], [31, 31, 31, 31],
                [32, 32, 32, 32], [33, 33, 33, 33]]

    MAN_PONS_SYM = ['🀇🀇🀇', '🀈🀈🀈', '🀉🀉🀉', '🀊🀊🀊', '🀋🀋🀋', '🀌🀌🀌', '🀍🀍🀍', '🀎🀎🀎', '🀏🀏🀏']
    PIN_PONS_SYM = ['🀙🀙🀙', '🀚🀚🀚', '🀛🀛🀛', '🀜🀜🀜', '🀝🀝🀝', '🀞🀞🀞', '🀟🀟🀟', '🀠🀠🀠', '🀡🀡🀡']
    SUO_PONS_SYM = ['🀐🀐🀐', '🀑🀑🀑', '🀒🀒🀒', '🀓🀓🀓', '🀔🀔🀔', '🀕🀕🀕', '🀖🀖🀖', '🀗🀗🀗', '🀘🀘🀘']
    CHR_PONS_SYM = ['🀀🀀🀀', '🀁🀁🀁', '🀂🀂🀂', '🀃🀃🀃', '🀆🀆🀆', '🀅🀅🀅', '🀄🀄🀄']
    PONS_SYM = ['🀇🀇🀇', '🀈🀈🀈', '🀉🀉🀉', '🀊🀊🀊', '🀋🀋🀋', '🀌🀌🀌', '🀍🀍🀍', '🀎🀎🀎', '🀏🀏🀏',
                '🀙🀙🀙', '🀚🀚🀚', '🀛🀛🀛', '🀜🀜🀜', '🀝🀝🀝', '🀞🀞🀞', '🀟🀟🀟', '🀠🀠🀠', '🀡🀡🀡',
                '🀐🀐🀐', '🀑🀑🀑', '🀒🀒🀒', '🀓🀓🀓', '🀔🀔🀔', '🀕🀕🀕', '🀖🀖🀖', '🀗🀗🀗', '🀘🀘🀘',
                '🀀🀀🀀', '🀁🀁🀁', '🀂🀂🀂', '🀃🀃🀃', '🀆🀆🀆', '🀅🀅🀅', '🀄🀄🀄']

    MAN_PONS_NUM = [[0, 0, 0], [1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4], [5, 5, 5], [6, 6, 6], [7, 7, 7], [8, 8, 8]]
    PIN_PONS_NUM = [[9, 9, 9], [10, 10, 10], [11, 11, 11], [12, 12, 12], [13, 13, 13], [14, 14, 14], [15, 15, 15],
                    [16, 16, 16], [17, 17, 17]]
    SUO_PONS_NUM = [[18, 18, 18], [19, 19, 19], [20, 20, 20], [21, 21, 21], [22, 22, 22], [23, 23, 23], [24, 24, 24],
                    [25, 25, 25], [26, 26, 26]]
    CHR_PONS_NUM = [[27, 27, 27], [28, 28, 28], [29, 29, 29], [30, 30, 30], [31, 31, 31], [32, 32, 32], [33, 33, 33]]
    PONS_NUM = [[0, 0, 0], [1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4], [5, 5, 5], [6, 6, 6], [7, 7, 7], [8, 8, 8],
                [9, 9, 9], [10, 10, 10], [11, 11, 11], [12, 12, 12], [13, 13, 13], [14, 14, 14], [15, 15, 15],
                [16, 16, 16], [17, 17, 17],
                [18, 18, 18], [19, 19, 19], [20, 20, 20], [21, 21, 21], [22, 22, 22], [23, 23, 23], [24, 24, 24],
                [25, 25, 25], [26, 26, 26],
                [27, 27, 27], [28, 28, 28], [29, 29, 29], [30, 30, 30], [31, 31, 31], [32, 32, 32], [33, 33, 33]]

    MAN_PAIR_SYM = ['🀇🀇', '🀈🀈', '🀉🀉', '🀊🀊', '🀋🀋', '🀌🀌', '🀍🀍', '🀎🀎', '🀏🀏']
    PIN_PAIR_SYM = ['🀙🀙', '🀚🀚', '🀛🀛', '🀜🀜', '🀝🀝', '🀞🀞', '🀟🀟', '🀠🀠', '🀡🀡']
    SUO_PAIR_SYM = ['🀐🀐', '🀑🀑', '🀒🀒', '🀓🀓', '🀔🀔', '🀕🀕', '🀖🀖', '🀗🀗', '🀘🀘']
    CHR_PAIR_SYM = ['🀀🀀', '🀁🀁', '🀂🀂', '🀃🀃', '🀆🀆', '🀅🀅', '🀄🀄']
    PAIRS_SYM = ['🀇🀇', '🀈🀈', '🀉🀉', '🀊🀊', '🀋🀋', '🀌🀌', '🀍🀍', '🀎🀎', '🀏🀏',
                 '🀙🀙', '🀚🀚', '🀛🀛', '🀜🀜', '🀝🀝', '🀞🀞', '🀟🀟', '🀠🀠', '🀡🀡',
                 '🀐🀐', '🀑🀑', '🀒🀒', '🀓🀓', '🀔🀔', '🀕🀕', '🀖🀖', '🀗🀗', '🀘🀘',
                 '🀀🀀', '🀁🀁', '🀂🀂', '🀃🀃', '🀆🀆', '🀅🀅', '🀄🀄']

    MAN_PAIR_NUM = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8]]
    PIN_PAIR_NUM = [[9, 9], [10, 10], [11, 11], [12, 12], [13, 13], [14, 14], [15, 15], [16, 16], [17, 17]]
    SUO_PAIR_NUM = [[18, 18], [19, 19], [20, 20], [21, 21], [22, 22], [23, 23], [24, 24], [25, 25], [26, 26]]
    CHR_PAIR_NUM = [[27, 27], [28, 28], [29, 29], [30, 30], [31, 31], [32, 32], [33, 33]]
    PAIRS_NUM = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8],
                 [9, 9], [10, 10], [11, 11], [12, 12], [13, 13], [14, 14], [15, 15], [16, 16], [17, 17],
                 [18, 18], [19, 19], [20, 20], [21, 21], [22, 22], [23, 23], [24, 24], [25, 25], [26, 26],
                 [27, 27], [28, 28], [29, 29], [30, 30], [31, 31], [32, 32], [33, 33]]

    MAN_SGL_SYM = ['🀇', '🀈', '🀉', '🀊', '🀋', '🀌', '🀍', '🀎', '🀏']
    PIN_SGL_SYM = ['🀙', '🀚', '🀛', '🀜', '🀝', '🀞', '🀟', '🀠', '🀡']
    SUO_SGL_SYM = ['🀐', '🀑', '🀒', '🀓', '🀔', '🀕', '🀖', '🀗', '🀘']
    SGL_CHAR_SYM = ['🀀', '🀁', '🀂', '🀃', '🀆', '🀅', '🀄']
    SGL_NUM_SYM = ['🀇', '🀈', '🀉', '🀊', '🀋', '🀌', '🀍', '🀎', '🀏',
                   '🀙', '🀚', '🀛', '🀜', '🀝', '🀞', '🀟', '🀠', '🀡',
                   '🀐', '🀑', '🀒', '🀓', '🀔', '🀕', '🀖', '🀗', '🀘']
    SGL_SYM = ["🀇", "🀈", "🀉", "🀊", "🀋", "🀌", "🀍", "🀎", "🀏",
               "🀙", "🀚", "🀛", "🀜", "🀝", "🀞", "🀟", "🀠", "🀡",
               "🀐", "🀑", "🀒", "🀓", "🀔", "🀕", "🀖", "🀗", "🀘",
               "🀀", "🀁", "🀂", "🀃", "🀆", "🀅", "🀄"]

    MAN_SGL_NUM = [[0], [1], [2], [3], [4], [5], [6], [7], [8]]
    PIN_SGL_NUM = [[9], [10], [11], [12], [13], [14], [15], [16], [17]]
    SUO_SGL_NUM = [[18], [19], [20], [21], [22], [23], [24], [25], [26]]
    CHR_SGL_NUM = [[27], [28], [29], [30], [31], [32], [33]]
    SGL_NUM_NUM = [[0], [1], [2], [3], [4], [5], [6], [7], [8],
                   [9], [10], [11], [12], [13], [14], [15], [16], [17],
                   [18], [19], [20], [21], [22], [23], [24], [25], [26]]
    SGL_NUM = [[0], [1], [2], [3], [4], [5], [6], [7], [8],
               [9], [10], [11], [12], [13], [14], [15], [16], [17],
               [18], [19], [20], [21], [22], [23], [24], [25], [26],
               [27], [28], [29], [30], [31], [32], [33]]

    MAN_O2_SYM = ['🀇🀈', '🀇🀉', '🀈🀊', '🀉🀋', '🀊🀌', '🀋🀍', '🀌🀎', '🀍🀏', '🀎🀏']
    PIN_O2_SYM = ['🀙🀚', '🀙🀛', '🀚🀜', '🀛🀝', '🀜🀞', '🀝🀟', '🀞🀠', '🀟🀡', '🀠🀡']
    SUO_O2_SYM = ['🀐🀑', '🀐🀒', '🀑🀓', '🀒🀔', '🀓🀕', '🀔🀖', '🀕🀗', '🀖🀘', '🀗🀘']
    O2_SYM = ['🀇🀈', '🀇🀉', '🀈🀊', '🀉🀋', '🀊🀌', '🀋🀍', '🀌🀎', '🀍🀏', '🀎🀏',
              '🀙🀚', '🀙🀛', '🀚🀜', '🀛🀝', '🀜🀞', '🀝🀟', '🀞🀠', '🀟🀡', '🀠🀡',
              '🀐🀑', '🀐🀒', '🀑🀓', '🀒🀔', '🀓🀕', '🀔🀖', '🀕🀗', '🀖🀘', '🀗🀘']

    MAN_O2_NUM = [[0, 1], [0, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 8]]
    PIN_O2_NUM = [[9, 10], [9, 11], [10, 12], [11, 13], [12, 14], [13, 15], [14, 16], [15, 17], [16, 17]]
    SUO_O2_NUM = [[18, 19], [18, 20], [19, 21], [20, 22], [21, 23], [22, 24], [23, 25], [24, 26], [25, 26]]
    O2_NUM = [[0, 1], [0, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 8],
              [9, 10], [9, 11], [10, 12], [11, 13], [12, 14], [13, 15], [14, 16], [15, 17], [16, 17],
              [18, 19], [18, 20], [19, 21], [20, 22], [21, 23], [22, 24], [23, 25], [24, 26], [25, 26]]

    MAN_O1_SYM = ['🀈🀉', '🀉🀊', '🀊🀋', '🀋🀌', '🀌🀍', '🀍🀎']
    PIN_O1_SYM = ['🀚🀛', '🀛🀜', '🀜🀝', '🀝🀞', '🀞🀟', '🀟🀠']
    SUO_O1_SYM = ['🀑🀒', '🀒🀓', '🀓🀔', '🀔🀕', '🀕🀖', '🀖🀗']
    O1_SYM = ['🀈🀉', '🀉🀊', '🀊🀋', '🀋🀌', '🀌🀍', '🀍🀎',
              '🀚🀛', '🀛🀜', '🀜🀝', '🀝🀞', '🀞🀟', '🀟🀠',
              '🀑🀒', '🀒🀓', '🀓🀔', '🀔🀕', '🀕🀖', '🀖🀗']

    MAN_O1_NUM = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]
    PIN_O1_NUM = [[10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16]]
    SUO_O1_NUM = [[19, 20], [20, 21], [21, 22], [22, 23], [23, 24], [24, 25]]
    O1_NUM = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7],
              [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16],
              [19, 20], [20, 21], [21, 22], [22, 23], [23, 24], [24, 25]]

    MAN_CHOW_SYM = ['🀇🀈🀉', '🀈🀉🀊', '🀉🀊🀋', '🀊🀋🀌', '🀋🀌🀍', '🀌🀍🀎', '🀍🀎🀏']
    PIN_CHOW_SYM = ['🀙🀚🀛', '🀚🀛🀜', '🀛🀜🀝', '🀜🀝🀞', '🀝🀞🀟', '🀞🀟🀠', '🀟🀠🀡']
    CHOWS_SYM = ['🀇🀈🀉', '🀈🀉🀊', '🀉🀊🀋', '🀊🀋🀌', '🀋🀌🀍', '🀌🀍🀎', '🀍🀎🀏',
                 '🀙🀚🀛', '🀚🀛🀜', '🀛🀜🀝', '🀜🀝🀞', '🀝🀞🀟', '🀞🀟🀠', '🀟🀠🀡',
                 '🀐🀑🀒', '🀑🀒🀓', '🀒🀓🀔', '🀓🀔🀕', '🀔🀕🀖', '🀕🀖🀗', '🀖🀗🀘']

    COLORS_SYM = ['man', 'pin', 'suo']

    MIX_COLOR_SYM = ['mix man', 'mix pin', 'mix suo']

    PURE_COLOR_SYM = ['pure man', 'pure pin', 'pure suo', 'pure char']

    PON_NUM_SYM = ['111', '222', '333', '444', '555', '666', '777', '888', '999']

    CHOW_NUM_SYM = ['123', '234', '345', '456', '567', '678', '789']

    RED_FIVES_SYM = ['\033[91m🀋\033[0m', '\033[91m🀝\033[0m', '\033[91m🀔\033[0m']

    DORA_SYM = ['🀆', '🀅', '🀄', 'player-wind', 'round-wind']
"""
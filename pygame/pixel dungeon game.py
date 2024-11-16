import pygame
import math

X, Y = 500, 500
win = pygame.display.set_mode((X, Y))
fps = 60

pygame.display.set_caption("name")

doc = open("C:/Users/Pbaby/PycharmProjects/pythonProject/level1.txt", "r")
doc = doc.read()
doc = doc.split("\n")

i = 0
floor_def = []
for item in doc:
    i += 1
    if "floor_size:" in item:
        text = item[11:-1]
        floor_size = text.split(",")
    if "floor_coords:" in item:
        text = item[13:-1]
        floor_coords = text.split(",")
    if "$$" in item:
        floor_def.append(i)

floor_def = [floor_def[0] + 1, floor_def[1] - 1]
floor = []
top_floor = []
player = []
enemy = []
top_player = []
box_coords = []

floor_str = "004, 041, 042, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150"
top_floor_str = "000, 001, 002, 003, 005, 031, 032, 033, 034, 035, 036, 037, 038, 039, 040, 043, 044, 045, 046, 047, 048, 049, 050, 051, 052, 093, 094, 095, 096, 097, 098, 099, 100, 101, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 152"
player_str = "006, 007, 008, 009, 010, 011, 012, 013, 014, 015, 016, 017, 018, 019, 020, 021, 022, 023, 024, 025, 026, 027, 028, 029, 030, 102, 103, 104, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135"
enemy_str = "058, 059, 060, 061, 062, 063, 064, 065, 066, 067, 068, 069, 070, 071, 072, 073, 074, 075, 076, 077, 078, 079, 080, 081, 082, 083, 084, 085, 086, 087, 088, 089, 090, 091, 092"
top_player_str = "053, 054, 055, 056"
box_coords_str = "151"


i = 0
for item in doc:
    i += 1
    try:
        if floor_def[0] <= i <= floor_def[1]:
            text = item.split(",")
            if text[0] in box_coords_str:
                box_coords.append([text[1], text[2]])
            elif text[0] in floor_str:
                floor.append(text)
            elif text[0] in top_floor_str:
                top_floor.append(text)
            elif text[0] in player_str:
                player.append(text)
            elif text[0] in enemy_str:
                enemy.append(text)
            elif text[0] in top_player_str:
                top_player.append(text)
            else:
                print(str(item) + " undefined")
    except:
        pass


shift = [-25, 25]
player_coords = [250, 250]

#  images
scale_size = 1
if True:
    i_000 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/000.png")
    i_000 = pygame.transform.scale(i_000, (i_000.get_width() * scale_size, i_000.get_height() * scale_size))
    i_001 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/001.png")
    i_001 = pygame.transform.scale(i_001, (i_001.get_width() * scale_size, i_001.get_height() * scale_size))
    i_002 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/002.png")
    i_002 = pygame.transform.scale(i_002, (i_002.get_width() * scale_size, i_002.get_height() * scale_size))
    i_003 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/003.png")
    i_003 = pygame.transform.scale(i_003, (i_003.get_width() * scale_size, i_003.get_height() * scale_size))
    i_004 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/004.png")
    i_004 = pygame.transform.scale(i_004, (i_004.get_width() * scale_size, i_004.get_height() * scale_size))
    i_005 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/005.png")
    i_005 = pygame.transform.scale(i_005, (i_005.get_width() * scale_size, i_005.get_height() * scale_size))
    i_006 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/006.png")
    i_006 = pygame.transform.scale(i_006, (i_006.get_width() * scale_size, i_006.get_height() * scale_size))
    i_007 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/007.png")
    i_007 = pygame.transform.scale(i_007, (i_007.get_width() * scale_size, i_007.get_height() * scale_size))
    i_008 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/008.png")
    i_008 = pygame.transform.scale(i_008, (i_008.get_width() * scale_size, i_008.get_height() * scale_size))
    i_009 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/009.png")
    i_009 = pygame.transform.scale(i_009, (i_009.get_width() * scale_size, i_009.get_height() * scale_size))
    i_010 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/010.png")
    i_010 = pygame.transform.scale(i_010, (i_010.get_width() * scale_size, i_010.get_height() * scale_size))
    i_011 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/011.png")
    i_011 = pygame.transform.scale(i_011, (i_011.get_width() * scale_size, i_011.get_height() * scale_size))
    i_012 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/012.png")
    i_012 = pygame.transform.scale(i_012, (i_012.get_width() * scale_size, i_012.get_height() * scale_size))
    i_013 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/013.png")
    i_013 = pygame.transform.scale(i_013, (i_013.get_width() * scale_size, i_013.get_height() * scale_size))
    i_014 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/014.png")
    i_014 = pygame.transform.scale(i_014, (i_014.get_width() * scale_size, i_014.get_height() * scale_size))
    i_015 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/015.png")
    i_015 = pygame.transform.scale(i_015, (i_015.get_width() * scale_size, i_015.get_height() * scale_size))
    i_016 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/016.png")
    i_016 = pygame.transform.scale(i_016, (i_016.get_width() * scale_size, i_016.get_height() * scale_size))
    i_017 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/017.png")
    i_017 = pygame.transform.scale(i_017, (i_017.get_width() * scale_size, i_017.get_height() * scale_size))
    i_018 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/018.png")
    i_018 = pygame.transform.scale(i_018, (i_018.get_width() * scale_size, i_018.get_height() * scale_size))
    i_019 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/019.png")
    i_019 = pygame.transform.scale(i_019, (i_019.get_width() * scale_size, i_019.get_height() * scale_size))
    i_020 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/020.png")
    i_020 = pygame.transform.scale(i_020, (i_020.get_width() * scale_size, i_020.get_height() * scale_size))
    i_021 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/021.png")
    i_021 = pygame.transform.scale(i_021, (i_021.get_width() * scale_size, i_021.get_height() * scale_size))
    i_022 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/022.png")
    i_022 = pygame.transform.scale(i_022, (i_022.get_width() * scale_size, i_022.get_height() * scale_size))
    i_023 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/023.png")
    i_023 = pygame.transform.scale(i_023, (i_023.get_width() * scale_size, i_023.get_height() * scale_size))
    i_024 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/024.png")
    i_024 = pygame.transform.scale(i_024, (i_024.get_width() * scale_size, i_024.get_height() * scale_size))
    i_025 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/025.png")
    i_025 = pygame.transform.scale(i_025, (i_025.get_width() * scale_size, i_025.get_height() * scale_size))
    i_026 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/026.png")
    i_026 = pygame.transform.scale(i_026, (i_026.get_width() * scale_size, i_026.get_height() * scale_size))
    i_027 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/027.png")
    i_027 = pygame.transform.scale(i_027, (i_027.get_width() * scale_size, i_027.get_height() * scale_size))
    i_028 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/028.png")
    i_028 = pygame.transform.scale(i_028, (i_028.get_width() * scale_size, i_028.get_height() * scale_size))
    i_029 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/029.png")
    i_029 = pygame.transform.scale(i_029, (i_029.get_width() * scale_size, i_029.get_height() * scale_size))
    i_030 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/030.png")
    i_030 = pygame.transform.scale(i_030, (i_030.get_width() * scale_size, i_030.get_height() * scale_size))
    i_031 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/031.png")
    i_031 = pygame.transform.scale(i_031, (i_031.get_width() * scale_size, i_031.get_height() * scale_size))
    i_032 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/032.png")
    i_032 = pygame.transform.scale(i_032, (i_032.get_width() * scale_size, i_032.get_height() * scale_size))
    i_033 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/033.png")
    i_033 = pygame.transform.scale(i_033, (i_033.get_width() * scale_size, i_033.get_height() * scale_size))
    i_034 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/034.png")
    i_034 = pygame.transform.scale(i_034, (i_034.get_width() * scale_size, i_034.get_height() * scale_size))
    i_035 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/035.png")
    i_035 = pygame.transform.scale(i_035, (i_035.get_width() * scale_size, i_035.get_height() * scale_size))
    i_036 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/036.png")
    i_036 = pygame.transform.scale(i_036, (i_036.get_width() * scale_size, i_036.get_height() * scale_size))
    i_037 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/037.png")
    i_037 = pygame.transform.scale(i_037, (i_037.get_width() * scale_size, i_037.get_height() * scale_size))
    i_038 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/038.png")
    i_038 = pygame.transform.scale(i_038, (i_038.get_width() * scale_size, i_038.get_height() * scale_size))
    i_039 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/039.png")
    i_039 = pygame.transform.scale(i_039, (i_039.get_width() * scale_size, i_039.get_height() * scale_size))
    i_040 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/040.png")
    i_040 = pygame.transform.scale(i_040, (i_040.get_width() * scale_size, i_040.get_height() * scale_size))
    i_041 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/041.png")
    i_041 = pygame.transform.scale(i_041, (i_041.get_width() * scale_size, i_041.get_height() * scale_size))
    i_042 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/042.png")
    i_042 = pygame.transform.scale(i_042, (i_042.get_width() * scale_size, i_042.get_height() * scale_size))
    i_043 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/043.png")
    i_043 = pygame.transform.scale(i_043, (i_043.get_width() * scale_size, i_043.get_height() * scale_size))
    i_044 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/044.png")
    i_044 = pygame.transform.scale(i_044, (i_044.get_width() * scale_size, i_044.get_height() * scale_size))
    i_045 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/045.png")
    i_045 = pygame.transform.scale(i_045, (i_045.get_width() * scale_size, i_045.get_height() * scale_size))
    i_046 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/046.png")
    i_046 = pygame.transform.scale(i_046, (i_046.get_width() * scale_size, i_046.get_height() * scale_size))
    i_047 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/047.png")
    i_047 = pygame.transform.scale(i_047, (i_047.get_width() * scale_size, i_047.get_height() * scale_size))
    i_048 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/048.png")
    i_048 = pygame.transform.scale(i_048, (i_048.get_width() * scale_size, i_048.get_height() * scale_size))
    i_049 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/049.png")
    i_049 = pygame.transform.scale(i_049, (i_049.get_width() * scale_size, i_049.get_height() * scale_size))
    i_050 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/050.png")
    i_050 = pygame.transform.scale(i_050, (i_050.get_width() * scale_size, i_050.get_height() * scale_size))
    i_051 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/051.png")
    i_051 = pygame.transform.scale(i_051, (i_051.get_width() * scale_size, i_051.get_height() * scale_size))
    i_052 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/052.png")
    i_052 = pygame.transform.scale(i_052, (i_052.get_width() * scale_size, i_052.get_height() * scale_size))
    i_053 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/053.png")
    i_053 = pygame.transform.scale(i_053, (i_053.get_width() * scale_size, i_053.get_height() * scale_size))
    i_054 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/054.png")
    i_054 = pygame.transform.scale(i_054, (i_054.get_width() * scale_size, i_054.get_height() * scale_size))
    i_055 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/055.png")
    i_055 = pygame.transform.scale(i_055, (i_055.get_width() * scale_size, i_055.get_height() * scale_size))
    i_056 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/056.png")
    i_056 = pygame.transform.scale(i_056, (i_056.get_width() * scale_size, i_056.get_height() * scale_size))
    i_057 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/057.png")
    i_057 = pygame.transform.scale(i_057, (i_057.get_width() * scale_size, i_057.get_height() * scale_size))
    i_058 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/058.png")
    i_058 = pygame.transform.scale(i_058, (i_058.get_width() * scale_size, i_058.get_height() * scale_size))
    i_059 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/059.png")
    i_059 = pygame.transform.scale(i_059, (i_059.get_width() * scale_size, i_059.get_height() * scale_size))
    i_060 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/060.png")
    i_060 = pygame.transform.scale(i_060, (i_060.get_width() * scale_size, i_060.get_height() * scale_size))
    i_061 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/061.png")
    i_061 = pygame.transform.scale(i_061, (i_061.get_width() * scale_size, i_061.get_height() * scale_size))
    i_062 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/062.png")
    i_062 = pygame.transform.scale(i_062, (i_062.get_width() * scale_size, i_062.get_height() * scale_size))
    i_063 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/063.png")
    i_063 = pygame.transform.scale(i_063, (i_063.get_width() * scale_size, i_063.get_height() * scale_size))
    i_064 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/064.png")
    i_064 = pygame.transform.scale(i_064, (i_064.get_width() * scale_size, i_064.get_height() * scale_size))
    i_065 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/065.png")
    i_065 = pygame.transform.scale(i_065, (i_065.get_width() * scale_size, i_065.get_height() * scale_size))
    i_066 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/066.png")
    i_066 = pygame.transform.scale(i_066, (i_066.get_width() * scale_size, i_066.get_height() * scale_size))
    i_067 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/067.png")
    i_067 = pygame.transform.scale(i_067, (i_067.get_width() * scale_size, i_067.get_height() * scale_size))
    i_068 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/068.png")
    i_068 = pygame.transform.scale(i_068, (i_068.get_width() * scale_size, i_068.get_height() * scale_size))
    i_069 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/069.png")
    i_069 = pygame.transform.scale(i_069, (i_069.get_width() * scale_size, i_069.get_height() * scale_size))
    i_070 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/070.png")
    i_070 = pygame.transform.scale(i_070, (i_070.get_width() * scale_size, i_070.get_height() * scale_size))
    i_071 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/071.png")
    i_071 = pygame.transform.scale(i_071, (i_071.get_width() * scale_size, i_071.get_height() * scale_size))
    i_072 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/072.png")
    i_072 = pygame.transform.scale(i_072, (i_072.get_width() * scale_size, i_072.get_height() * scale_size))
    i_073 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/073.png")
    i_073 = pygame.transform.scale(i_073, (i_073.get_width() * scale_size, i_073.get_height() * scale_size))
    i_074 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/074.png")
    i_074 = pygame.transform.scale(i_074, (i_074.get_width() * scale_size, i_074.get_height() * scale_size))
    i_075 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/075.png")
    i_075 = pygame.transform.scale(i_075, (i_075.get_width() * scale_size, i_075.get_height() * scale_size))
    i_076 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/076.png")
    i_076 = pygame.transform.scale(i_076, (i_076.get_width() * scale_size, i_076.get_height() * scale_size))
    i_077 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/077.png")
    i_077 = pygame.transform.scale(i_077, (i_077.get_width() * scale_size, i_077.get_height() * scale_size))
    i_078 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/078.png")
    i_078 = pygame.transform.scale(i_078, (i_078.get_width() * scale_size, i_078.get_height() * scale_size))
    i_079 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/079.png")
    i_079 = pygame.transform.scale(i_079, (i_079.get_width() * scale_size, i_079.get_height() * scale_size))
    i_080 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/080.png")
    i_080 = pygame.transform.scale(i_080, (i_080.get_width() * scale_size, i_080.get_height() * scale_size))
    i_081 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/081.png")
    i_081 = pygame.transform.scale(i_081, (i_081.get_width() * scale_size, i_081.get_height() * scale_size))
    i_082 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/082.png")
    i_082 = pygame.transform.scale(i_082, (i_082.get_width() * scale_size, i_082.get_height() * scale_size))
    i_083 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/083.png")
    i_083 = pygame.transform.scale(i_083, (i_083.get_width() * scale_size, i_083.get_height() * scale_size))
    i_084 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/084.png")
    i_084 = pygame.transform.scale(i_084, (i_084.get_width() * scale_size, i_084.get_height() * scale_size))
    i_085 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/085.png")
    i_085 = pygame.transform.scale(i_085, (i_085.get_width() * scale_size, i_085.get_height() * scale_size))
    i_086 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/086.png")
    i_086 = pygame.transform.scale(i_086, (i_086.get_width() * scale_size, i_086.get_height() * scale_size))
    i_087 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/087.png")
    i_087 = pygame.transform.scale(i_087, (i_087.get_width() * scale_size, i_087.get_height() * scale_size))
    i_088 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/088.png")
    i_088 = pygame.transform.scale(i_088, (i_088.get_width() * scale_size, i_088.get_height() * scale_size))
    i_089 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/089.png")
    i_089 = pygame.transform.scale(i_089, (i_089.get_width() * scale_size, i_089.get_height() * scale_size))
    i_090 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/090.png")
    i_090 = pygame.transform.scale(i_090, (i_090.get_width() * scale_size, i_090.get_height() * scale_size))
    i_091 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/091.png")
    i_091 = pygame.transform.scale(i_091, (i_091.get_width() * scale_size, i_091.get_height() * scale_size))
    i_092 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/092.png")
    i_092 = pygame.transform.scale(i_092, (i_092.get_width() * scale_size, i_092.get_height() * scale_size))
    i_093 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/093.png")
    i_093 = pygame.transform.scale(i_093, (i_093.get_width() * scale_size, i_093.get_height() * scale_size))
    i_094 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/094.png")
    i_094 = pygame.transform.scale(i_094, (i_094.get_width() * scale_size, i_094.get_height() * scale_size))
    i_095 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/095.png")
    i_095 = pygame.transform.scale(i_095, (i_095.get_width() * scale_size, i_095.get_height() * scale_size))
    i_096 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/096.png")
    i_096 = pygame.transform.scale(i_096, (i_096.get_width() * scale_size, i_096.get_height() * scale_size))
    i_097 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/097.png")
    i_097 = pygame.transform.scale(i_097, (i_097.get_width() * scale_size, i_097.get_height() * scale_size))
    i_098 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/098.png")
    i_098 = pygame.transform.scale(i_098, (i_098.get_width() * scale_size, i_098.get_height() * scale_size))
    i_099 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/099.png")
    i_099 = pygame.transform.scale(i_099, (i_099.get_width() * scale_size, i_099.get_height() * scale_size))
    i_100 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/100.png")
    i_100 = pygame.transform.scale(i_100, (i_100.get_width() * scale_size, i_100.get_height() * scale_size))
    i_101 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/101.png")
    i_101 = pygame.transform.scale(i_101, (i_101.get_width() * scale_size, i_101.get_height() * scale_size))
    i_102 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/102.png")
    i_102 = pygame.transform.scale(i_102, (i_102.get_width() * scale_size, i_102.get_height() * scale_size))
    i_103 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/103.png")
    i_103 = pygame.transform.scale(i_103, (i_103.get_width() * scale_size, i_103.get_height() * scale_size))
    i_104 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/104.png")
    i_104 = pygame.transform.scale(i_104, (i_104.get_width() * scale_size, i_104.get_height() * scale_size))
    i_105 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/105.png")
    i_105 = pygame.transform.scale(i_105, (i_105.get_width() * scale_size, i_105.get_height() * scale_size))
    i_106 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/106.png")
    i_106 = pygame.transform.scale(i_106, (i_106.get_width() * scale_size, i_106.get_height() * scale_size))
    i_107 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/107.png")
    i_107 = pygame.transform.scale(i_107, (i_107.get_width() * scale_size, i_107.get_height() * scale_size))
    i_108 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/108.png")
    i_108 = pygame.transform.scale(i_108, (i_108.get_width() * scale_size, i_108.get_height() * scale_size))
    i_109 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/109.png")
    i_109 = pygame.transform.scale(i_109, (i_109.get_width() * scale_size, i_109.get_height() * scale_size))
    i_110 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/110.png")
    i_110 = pygame.transform.scale(i_110, (i_110.get_width() * scale_size, i_110.get_height() * scale_size))
    i_111 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/111.png")
    i_111 = pygame.transform.scale(i_111, (i_111.get_width() * scale_size, i_111.get_height() * scale_size))
    i_112 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/112.png")
    i_112 = pygame.transform.scale(i_112, (i_112.get_width() * scale_size, i_112.get_height() * scale_size))
    i_113 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/113.png")
    i_113 = pygame.transform.scale(i_113, (i_113.get_width() * scale_size, i_113.get_height() * scale_size))
    i_114 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/114.png")
    i_114 = pygame.transform.scale(i_114, (i_114.get_width() * scale_size, i_114.get_height() * scale_size))
    i_115 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/115.png")
    i_115 = pygame.transform.scale(i_115, (i_115.get_width() * scale_size, i_115.get_height() * scale_size))
    i_116 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/116.png")
    i_116 = pygame.transform.scale(i_116, (i_116.get_width() * scale_size, i_116.get_height() * scale_size))
    i_117 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/117.png")
    i_117 = pygame.transform.scale(i_117, (i_117.get_width() * scale_size, i_117.get_height() * scale_size))
    i_118 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/118.png")
    i_118 = pygame.transform.scale(i_118, (i_118.get_width() * scale_size, i_118.get_height() * scale_size))
    i_119 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/119.png")
    i_119 = pygame.transform.scale(i_119, (i_119.get_width() * scale_size, i_119.get_height() * scale_size))
    i_120 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/120.png")
    i_120 = pygame.transform.scale(i_120, (i_120.get_width() * scale_size, i_120.get_height() * scale_size))
    i_121 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/121.png")
    i_121 = pygame.transform.scale(i_121, (i_121.get_width() * scale_size, i_121.get_height() * scale_size))
    i_122 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/122.png")
    i_122 = pygame.transform.scale(i_122, (i_122.get_width() * scale_size, i_122.get_height() * scale_size))
    i_123 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/123.png")
    i_123 = pygame.transform.scale(i_123, (i_123.get_width() * scale_size, i_123.get_height() * scale_size))
    i_124 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/124.png")
    i_124 = pygame.transform.scale(i_124, (i_124.get_width() * scale_size, i_124.get_height() * scale_size))
    i_125 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/125.png")
    i_125 = pygame.transform.scale(i_125, (i_125.get_width() * scale_size, i_125.get_height() * scale_size))
    i_126 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/126.png")
    i_126 = pygame.transform.scale(i_126, (i_126.get_width() * scale_size, i_126.get_height() * scale_size))
    i_127 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/127.png")
    i_127 = pygame.transform.scale(i_127, (i_127.get_width() * scale_size, i_127.get_height() * scale_size))
    i_128 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/128.png")
    i_128 = pygame.transform.scale(i_128, (i_128.get_width() * scale_size, i_128.get_height() * scale_size))
    i_129 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/129.png")
    i_129 = pygame.transform.scale(i_129, (i_129.get_width() * scale_size, i_129.get_height() * scale_size))
    i_130 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/130.png")
    i_130 = pygame.transform.scale(i_130, (i_130.get_width() * scale_size, i_130.get_height() * scale_size))
    i_131 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/131.png")
    i_131 = pygame.transform.scale(i_131, (i_131.get_width() * scale_size, i_131.get_height() * scale_size))
    i_132 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/132.png")
    i_132 = pygame.transform.scale(i_132, (i_132.get_width() * scale_size, i_132.get_height() * scale_size))
    i_133 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/133.png")
    i_133 = pygame.transform.scale(i_133, (i_133.get_width() * scale_size, i_133.get_height() * scale_size))
    i_134 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/134.png")
    i_134 = pygame.transform.scale(i_134, (i_134.get_width() * scale_size, i_134.get_height() * scale_size))
    i_135 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/135.png")
    i_135 = pygame.transform.scale(i_135, (i_135.get_width() * scale_size, i_135.get_height() * scale_size))
    i_136 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/136.png")
    i_136 = pygame.transform.scale(i_136, (i_136.get_width() * scale_size, i_136.get_height() * scale_size))
    i_137 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/137.png")
    i_137 = pygame.transform.scale(i_137, (i_137.get_width() * scale_size, i_137.get_height() * scale_size))
    i_138 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/138.png")
    i_138 = pygame.transform.scale(i_138, (i_138.get_width() * scale_size, i_138.get_height() * scale_size))
    i_139 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/139.png")
    i_139 = pygame.transform.scale(i_139, (i_139.get_width() * scale_size, i_139.get_height() * scale_size))
    i_140 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/140.png")
    i_140 = pygame.transform.scale(i_140, (i_140.get_width() * scale_size, i_140.get_height() * scale_size))
    i_141 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/141.png")
    i_141 = pygame.transform.scale(i_141, (i_141.get_width() * scale_size, i_141.get_height() * scale_size))
    i_142 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/142.png")
    i_142 = pygame.transform.scale(i_142, (i_142.get_width() * scale_size, i_142.get_height() * scale_size))
    i_143 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/143.png")
    i_143 = pygame.transform.scale(i_143, (i_143.get_width() * scale_size, i_143.get_height() * scale_size))
    i_144 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/144.png")
    i_144 = pygame.transform.scale(i_144, (i_144.get_width() * scale_size, i_144.get_height() * scale_size))
    i_145 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/145.png")
    i_145 = pygame.transform.scale(i_145, (i_145.get_width() * scale_size, i_145.get_height() * scale_size))
    i_146 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/146.png")
    i_146 = pygame.transform.scale(i_146, (i_146.get_width() * scale_size, i_146.get_height() * scale_size))
    i_147 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/147.png")
    i_147 = pygame.transform.scale(i_147, (i_147.get_width() * scale_size, i_147.get_height() * scale_size))
    i_148 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/148.png")
    i_148 = pygame.transform.scale(i_148, (i_148.get_width() * scale_size, i_148.get_height() * scale_size))
    i_149 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/149.png")
    i_149 = pygame.transform.scale(i_149, (i_149.get_width() * scale_size, i_149.get_height() * scale_size))
    i_150 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/150.png")
    i_150 = pygame.transform.scale(i_150, (i_150.get_width() * scale_size, i_150.get_height() * scale_size))
    i_151 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/151.png")
    i_151 = pygame.transform.scale(i_151, (i_151.get_width() * scale_size, i_151.get_height() * scale_size))
    i_152 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/152.png")
    i_152 = pygame.transform.scale(i_152, (i_152.get_width() * scale_size, i_152.get_height() * scale_size))
    i_153 = pygame.image.load("C:/Users/Pbaby/PycharmProjects/pythonProject/new game project/153.png")
    i_153 = pygame.transform.scale(i_153, (i_153.get_width() * scale_size, i_153.get_height() * scale_size))

player_speed = 2
dash_speed = 4
dash_time = 20
attack_time = 4
attack_cooldown = 20
player_iid = "057"
player_box = pygame.Rect(100, 400, 1, 1)  #
command = "player_box = pygame.Rect(" + str(player_coords[0]) + " - i_" + player_iid + ".get_width()//2, " + str(player_coords[1]) + " - i_" + player_iid + ".get_height()//2, i_" + player_iid + ".get_height(), i_" + player_iid + ".get_width())"
exec(command)
player_i = i_000  #
command = "player_i = i_" + player_iid
exec(command)

weapon_dist = 25
weapon_iid = "008"
weapon_i = i_000  #
command = "weapon_i = i_" + weapon_iid
exec(command)

tick_speed = 12


def colour(surface, scale):
    gradient = min(255, max(0, round(255 * (1-scale))))
    surface.fill((255, gradient, gradient), special_flags=pygame.BLEND_MULT)


def enemy_move():
    pass


def player_move(player, accel, dash):
    m_up = -1
    m_down = -1
    m_left = -1
    m_right = -1

    for item in box_coords:
        if player_box.y <= (int(item[1]) - shift[1]) + 50 <= player_box.y + player_speed+(dash*dash_speed) and player_box.x + player_box.height >= (int(item[0]) - shift[0]) and player_box.x <= (int(item[0]) - shift[0]) + 50:
            m_up = 1
        elif player_box.y + player_box.width < (int(item[1]) - shift[1]) < player_box.y + player_box.width + player_speed+(dash*dash_speed) and player_box.x + player_box.height > (int(item[0]) - shift[0]) and player_box.x < (int(item[0]) - shift[0]) + 50:
            m_down = 1
        elif player_box.x > (int(item[0]) - shift[0]) + 50 > player_box.x - (player_speed+(dash*dash_speed)) and player_box.y < (int(item[1]) - shift[1]) + 50 and player_box.y + player_box.width > (int(item[1]) - shift[1]):
            m_left = 1
        elif player_box.x + player_box.height < (int(item[0]) - shift[0]) < player_box.x + player_box.height + player_speed+(dash*dash_speed) and player_box.y < (int(item[1]) - shift[1]) + 50 and player_box.y + player_box.width > (int(item[1]) - shift[1]):
            m_right = 1

    if accel[0] == -1 and m_left == -1:
        shift[0] -= player_speed+(dash*dash_speed)
    if accel[0] == 1 and m_right == -1:
        shift[0] += player_speed+(dash*dash_speed)
    if accel[1] == -1 and m_up == -1:
        shift[1] -= player_speed+(dash*dash_speed)
    if accel[1] == 1 and m_down == -1:
        shift[1] += player_speed+(dash*dash_speed)


def draw_win(player, f, tf, p, tp, mouse, tick, attack, attack_ticks):
    mouse_x, mouse_y = mouse
    bg = pygame.Rect(0, 0, X, Y)
    pygame.draw.rect(win, (0, 0, 0), bg)

    # display order: f, tf, p, tp
    for item in f:
        command = "win.blit(i_" + item[0] + ", (" + item[1] + " - shift[0], " + item[2] + " - shift[1]))"
        exec(command)
    for item in tf:
        if item[0] == "093":
            if int(item[0]) + ((tick/tick_speed)//1)%8 >= 100:
                command = "win.blit(i_" + str(int(item[0]) + int((tick/tick_speed)//1%8)) + ", (" + item[1] + " - shift[0], " + item[2] + " - shift[1]))"
                exec(command)
            else:
                command = "win.blit(i_" + "0" + str(int(item[0]) + int((tick/tick_speed)//1%8)) + ", (" + item[1] + " - shift[0], " + item[2] + " - shift[1]))"
                exec(command)
        else:
            command = "win.blit(i_" + item[0] + ", (" + item[1] + " - shift[0], " + item[2] + " - shift[1]))"
            exec(command)
    if mouse_x < 250:
        win.blit(pygame.transform.flip(player_i, True, False), (player.x, player.y))
    else:
        win.blit(pygame.transform.flip(player_i, False, False), (player.x, player.y))

    if attack == 0:
        if (player.x + player_i.get_width() // 2) - mouse_x == 0:
            angle = 0
        elif (player.x + player_i.get_width() // 2) - mouse_x > 0:
            angle = 90 - math.atan((mouse_y - (player.y + player_i.get_height() // 2)) / (mouse_x - (player.x + player_i.get_width() // 2))) * 57.2957795
        elif (player.x + player_i.get_width() // 2) - mouse_x < 0:
            angle = 270 - math.atan((mouse_y - (player.y + player_i.get_height() // 2)) / (mouse_x - (player.x + player_i.get_width() // 2))) * 57.2957795

        weapon_draw = pygame.transform.rotate(weapon_i, angle)
        if (player.x + player_i.get_width() // 2) - mouse_x <= 0 and (player.y + player_i.get_height() // 2) - mouse_y <= 0:  # quadrant 4
            win.blit(weapon_draw, (player_box.x + player_i.get_width() // 2 - (math.sin((270 - angle) / 57.2957795) * weapon_i.get_width()) / 2 - (math.sin(angle / 57.2957795) * weapon_dist), player_box.y + player_i.get_height() // 2 - (math.cos((270 - angle) / 57.2957795) * weapon_i.get_width()) / 2 - (math.cos(angle / 57.2957795) * weapon_dist)))
        if (player.x + player_i.get_width() // 2) - mouse_x < 0 and (player.y + player_i.get_height() // 2) - mouse_y > 0:  # quadrant 1
            win.blit(weapon_draw, (player_box.x + player_i.get_width() // 2 + (math.sin((270 - angle) / 57.2957795) * weapon_i.get_width()) / 2 - (math.sin(angle / 57.2957795) * weapon_dist),player_box.y + player_i.get_height() // 2 - weapon_draw.get_height() + (math.cos((270 - angle) / 57.2957795) * weapon_i.get_width()) / 2 - (math.cos(angle / 57.2957795) * weapon_dist)))
        if (player.x + player_i.get_width() // 2) - mouse_x > 0 and (player.y + player_i.get_height() // 2) - mouse_y > 0:  # quadrant 2
            win.blit(weapon_draw, (player_box.x + player_i.get_width() // 2 - weapon_draw.get_width() - (math.sin((270 - angle) / 57.2957795) * weapon_i.get_width()) / 2 - (math.sin(angle / 57.2957795) * weapon_dist),player_box.y + player_i.get_height() // 2 - weapon_draw.get_height() - (math.cos((270 - angle) / 57.2957795) * weapon_i.get_width()) / 2 - (math.cos(angle / 57.2957795) * weapon_dist)))
        if (player.x + player_i.get_width() // 2) - mouse_x > 0 and (player.y + player_i.get_height() // 2) - mouse_y < 0:  # quadrant 3
            win.blit(weapon_draw, (player_box.x + player_i.get_width() // 2 - weapon_draw.get_width() + (math.sin((270 - angle) / 57.2957795) * weapon_i.get_width()) / 2 - (math.sin(angle / 57.2957795) * weapon_dist),player_box.y + player_i.get_height() // 2 + (math.cos((270 - angle) / 57.2957795) * weapon_i.get_width()) / 2 - (math.cos(angle / 57.2957795) * weapon_dist)))
    elif attack == 1:
        if (player.x + player_i.get_width() // 2) - mouse_x == 0:
            angle = 0
        elif (player.x + player_i.get_width() // 2) - mouse_x > 0:
            angle = 90 - math.atan((mouse_y - (player.y + player_i.get_height() // 2)) / (mouse_x - (player.x + player_i.get_width() // 2))) * 57.2957795
        elif (player.x + player_i.get_width() // 2) - mouse_x < 0:
            angle = 270 - math.atan((mouse_y - (player.y + player_i.get_height() // 2)) / (mouse_x - (player.x + player_i.get_width() // 2))) * 57.2957795
        swing_draw = pygame.transform.rotate(i_153, angle+90)
        if (player.x + player_i.get_width() // 2) - mouse_x <= 0 and (player.y + player_i.get_height() // 2) - mouse_y <= 0:  # quadrant 4
            win.blit(swing_draw, (player_box.x + player_i.get_width() // 2 - (math.sin((270 - angle) / 57.2957795) * i_153.get_width()) / 2 - (math.sin(angle / 57.2957795) * weapon_dist), player_box.y + player_i.get_height() // 2 - (math.cos((270 - angle) / 57.2957795) * i_153.get_width()) / 2 - (math.cos(angle / 57.2957795) * weapon_dist)))
        if (player.x + player_i.get_width() // 2) - mouse_x < 0 and (player.y + player_i.get_height() // 2) - mouse_y > 0:  # quadrant 1
            win.blit(swing_draw, (player_box.x + player_i.get_width() // 2 + (math.sin((270 - angle) / 57.2957795) * i_153.get_width()) / 2 - (math.sin(angle / 57.2957795) * weapon_dist),player_box.y + player_i.get_height() // 2 - swing_draw.get_height() + (math.cos((270 - angle) / 57.2957795) * i_153.get_width()) / 2 - (math.cos(angle / 57.2957795) * weapon_dist)))
        if (player.x + player_i.get_width() // 2) - mouse_x > 0 and (player.y + player_i.get_height() // 2) - mouse_y > 0:  # quadrant 2
            win.blit(swing_draw, (player_box.x + player_i.get_width() // 2 - swing_draw.get_width() - (math.sin((270 - angle) / 57.2957795) * i_153.get_width()) / 2 - (math.sin(angle / 57.2957795) * weapon_dist),player_box.y + player_i.get_height() // 2 - swing_draw.get_height() - (math.cos((270 - angle) / 57.2957795) * i_153.get_width()) / 2 - (math.cos(angle / 57.2957795) * weapon_dist)))
        if (player.x + player_i.get_width() // 2) - mouse_x > 0 and (player.y + player_i.get_height() // 2) - mouse_y < 0:  # quadrant 3
            win.blit(swing_draw, (player_box.x + player_i.get_width() // 2 - swing_draw.get_width() + (math.sin((270 - angle) / 57.2957795) * i_153.get_width()) / 2 - (math.sin(angle / 57.2957795) * weapon_dist),player_box.y + player_i.get_height() // 2 + (math.cos((270 - angle) / 57.2957795) * i_153.get_width()) / 2 - (math.cos(angle / 57.2957795) * weapon_dist)))
        a = (5 - attack_ticks)*10
        weapon_draw = pygame.transform.rotate(weapon_i, (angle+a))
        if 180 <= ((angle+a)%360) <= 270:
            win.blit(weapon_draw, (player_box.x + player_i.get_width() // 2 - (math.sin((270 - ((angle+a)%360)) / 57.2957795) * weapon_i.get_width()) / 2 - (math.sin(((angle+a)%360) / 57.2957795) * weapon_dist), player_box.y + player_i.get_height() // 2 - (math.cos((270 - ((angle+a)%360)) / 57.2957795) * weapon_i.get_width()) / 2 - (math.cos(((angle+a)%360) / 57.2957795) * weapon_dist)))
        if 270 <= ((angle+a)%360) <= 360:
            win.blit(weapon_draw, (player_box.x + player_i.get_width() // 2 + (math.sin((270 - ((angle+a)%360)) / 57.2957795) * weapon_i.get_width()) / 2 - (math.sin(((angle+a)%360) / 57.2957795) * weapon_dist),player_box.y + player_i.get_height() // 2 - weapon_draw.get_height() + (math.cos((270 - ((angle+a)%360)) / 57.2957795) * weapon_i.get_width()) / 2 - (math.cos(((angle+a)%360) / 57.2957795) * weapon_dist)))
        if 0 <= ((angle+a)%360) <= 90:
            win.blit(weapon_draw, (player_box.x + player_i.get_width() // 2 - weapon_draw.get_width() - (math.sin((270 - ((angle+a)%360)) / 57.2957795) * weapon_i.get_width()) / 2 - (math.sin(((angle+a)%360) / 57.2957795) * weapon_dist),player_box.y + player_i.get_height() // 2 - weapon_draw.get_height() - (math.cos((270 - ((angle+a)%360)) / 57.2957795) * weapon_i.get_width()) / 2 - (math.cos(((angle+a)%360) / 57.2957795) * weapon_dist)))
        if 90 <= ((angle+a)%360) <= 180:
            win.blit(weapon_draw, (player_box.x + player_i.get_width() // 2 - weapon_draw.get_width() + (math.sin((270 - ((angle+a)%360)) / 57.2957795) * weapon_i.get_width()) / 2 - (math.sin(((angle+a)%360) / 57.2957795) * weapon_dist),player_box.y + player_i.get_height() // 2 + (math.cos((270 - ((angle+a)%360)) / 57.2957795) * weapon_i.get_width()) / 2 - (math.cos(((angle+a)%360) / 57.2957795) * weapon_dist)))

    for item in p:
        command = "win.blit(i_" + item[0] + ", (" + item[1] + " - shift[0], " + item[2] + " - shift[1]))"
        exec(command)

    for item in tp:
        command = "win.blit(i_" + item[0] + ", (" + item[1] + " - shift[0], " + item[2] + " - shift[1]))"
        exec(command)

    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    run = 1
    tick = 0
    dash = 0
    dash_timer = 0
    attack = 0
    attack_timer = 0
    cooldown = 0
    while run:
        tick += 1
        if dash == 1:
            dash_timer -= 1
        if dash_timer <= 0:
            dash = 0
        if attack > 0:
            attack_timer -= 1
        if attack_timer <= 0:
            attack = 0
        if cooldown > 0:
            cooldown -= 1

        clock.tick(fps)

        player_accel = [0, 0]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    dash = 1
                    dash_timer = dash_time
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_presses = pygame.mouse.get_pressed()
                if mouse_presses[0] and cooldown <= 0:
                    attack = 1
                    attack_timer = attack_time
                    cooldown = attack_cooldown

        mouse_coords = pygame.mouse.get_pos()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            player_accel[1] = -1
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            player_accel[0] = -1
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            player_accel[1] = 1
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            player_accel[0] = 1

        enemy_move()
        player_move(player_coords, player_accel, dash)
        draw_win(player_box, floor, top_floor, player, top_player, mouse_coords, tick, attack, attack_timer)


if __name__ == "__main__":
    main()

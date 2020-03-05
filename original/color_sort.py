import colorsys

def get_hsv(hexrgb):
    hexrgb = hexrgb.lstrip("#")   # in case you have Web color specs
    r, g, b = (int(hexrgb[i:i+2], 16) / 255.0 for i in range(0,5,2))
    return colorsys.rgb_to_hsv(r, g, b)

# color_list = ["000050", "005000", "500000"]  # GBR
color_list = ['000000', '0074D9','FF4136','2ECC40','FFDC00',
	 			'AAAAAA', 'F012BE', 'FF851B', '7FDBFF', '870C25']

color_list.sort(key=get_hsv)
print(color_list)
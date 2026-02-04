import matplotlib.font_manager

# List all available fonts
font_list = matplotlib.font_manager.findSystemFonts(fontpaths=None, fontext='ttf')
for font in font_list:
    print(font)

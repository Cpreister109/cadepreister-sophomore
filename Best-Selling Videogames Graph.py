import matplotlib.pyplot as plt

vg_names  = ['Minecraft', 'GTAV', 'Tetris', 'Wii Sports', 'Pub G', 'Mario Kart 8', 'Super Mario Bros.', 'RDR2', 'Pokemon R/G/Y', 'Terraria(The Best One)', '']
vg_values = ['238.0', '175.0', '100.0', '82.9', '75.0', '60.5', '58.0', '50.0', '47.5', '44.5', '0']
vg_values.reverse()
vg_names.reverse()

barcolors = ['green', 'goldenrod', 'violet', 'aquamarine', 'olivedrab', 'blue', 'orange', 'red', 'royalblue', 'brown']

plt.xlabel('Copies Sold (In Millions)')
plt.ylabel('Video Game')

plt.title('Best-Selling Games of All Time')

plt.barh(vg_names, vg_values, color=barcolors, alpha = 0.8)

plt.show()
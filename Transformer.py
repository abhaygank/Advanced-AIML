import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw_box(ax, xy, width, height, label, color='lightblue'):
    rect = patches.FancyBboxPatch(xy, width, height, boxstyle="round,pad=0.02", edgecolor='black',
                                  facecolor=color, linewidth=1.5)
    ax.add_patch(rect)
    ax.text(xy[0] + width/2, xy[1] + height/2, label, ha='center', va='center', fontsize=8)

def draw_arrow(ax, start, end, label=None):
    ax.annotate('', xy=end, xytext=start, arrowprops=dict(arrowstyle='->', lw=1.5))
    if label:
        ax.text((start[0]+end[0])/2, (start[1]+end[1])/2 + 0.1, label, ha='center', fontsize=7)

fig, ax = plt.subplots(figsize=(14, 10))
ax.set_xlim(0, 20)
ax.set_ylim(0, 20)
ax.axis('off')

# Encoder
draw_box(ax, (1, 16), 3, 1, 'Input Embedding')
draw_box(ax, (1, 14.5), 3, 1, 'Positional Encoding')
draw_box(ax, (1, 13), 3, 1, 'Multi-Head\nSelf-Attention')
draw_box(ax, (1, 11.5), 3, 1, 'Feed Forward')
draw_box(ax, (1, 10), 3, 1, 'Encoder Output')

# Decoder
draw_box(ax, (10, 16), 3, 1, 'Output Embedding')
draw_box(ax, (10, 14.5), 3, 1, 'Positional Encoding')
draw_box(ax, (10, 13), 3, 1, 'Masked Multi-Head\nSelf-Attention')
draw_box(ax, (10, 11.5), 3, 1, 'Encoder-Decoder\nAttention')
draw_box(ax, (10, 10), 3, 1, 'Feed Forward')
draw_box(ax, (10, 8.5), 3, 1, 'Decoder Output')
draw_box(ax, (10, 7), 3, 1, 'Linear + Softmax')

# Attention mechanism
draw_box(ax, (6, 4), 2, 1, 'Query')
draw_box(ax, (4, 2.5), 2, 1, 'Key')
draw_box(ax, (8, 2.5), 2, 1, 'Value')
draw_box(ax, (6, 1), 2, 1, 'Attention\nScores')

# Arrows Encoder
draw_arrow(ax, (2.5, 16), (2.5, 15))
draw_arrow(ax, (2.5, 14.5), (2.5, 13.5))
draw_arrow(ax, (2.5, 13), (2.5, 12))
draw_arrow(ax, (2.5, 11.5), (2.5, 10.5))

# Arrows Decoder
draw_arrow(ax, (11.5, 16), (11.5, 15))
draw_arrow(ax, (11.5, 14.5), (11.5, 13.5))
draw_arrow(ax, (11.5, 13), (11.5, 12))
draw_arrow(ax, (11.5, 11.5), (11.5, 10.5))
draw_arrow(ax, (11.5, 10), (11.5, 9))
draw_arrow(ax, (11.5, 8.5), (11.5, 7.5))

# Encoder to Decoder Attention
draw_arrow(ax, (4, 10.5), (10, 11.5), label='Context')

# Attention mechanism arrows
draw_arrow(ax, (7, 4), (5, 3.5))
draw_arrow(ax, (7, 4), (9, 3.5))
draw_arrow(ax, (6, 2.5), (7, 1.5))
draw_arrow(ax, (10, 2.5), (7, 1.5))

plt.tight_layout()
plt.show()
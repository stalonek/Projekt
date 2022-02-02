from deck import DeckOfCards
import matplotlip
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from pathlib import Path

deck_of_cards = DeckOfCards()
deck_of_cards.shuffle()

path = Path('.').joinpath('card_images')

figure, axes_list = plt.subplots(nrows=2, ncols=5)
print(figure)
print(axes_list)

image_name = deck_of_cards.deal_card().image_name
print(image_name)


for axes in axes_list.ravel():
    axes.get_xaxis().set_visible(False)
    axes.get_yaxis().set_visible(False)
    image_name = deck_of_cards.deal_card().image_name
    img = mpimg.imread(str(path.joinpath(image_name).resolve()))
    axes.imshow(img)

figure.tight_layout()

plt.show()

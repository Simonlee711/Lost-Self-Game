import imageio

from pathlib import Path
image_path = Path('/Users/simonlee/Lost-Self-Game/artwork/title page/title')
images = list(image_path.glob('*.png'))
image_list = []
for file_name in images:
    image_list.append(imageio.imread(file_name))
    imageio.mimwrite('animated_from_images.gif', image_list)
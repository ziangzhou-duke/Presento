import cv2
import numpy as np

from pose.estimation_example.config import get_default_configuration
from pose.estimation_example.coordinates import get_coordinates
from pose.estimation_example.connections import get_connections
from pose.estimation_example.estimators import estimate
from pose.estimation_example.renderers import draw


if __name__ == '__main__':
    heatmaps_path = './resources/heatmaps.npy'
    paf_path = './resources/pafs.npy'    
    example_img_path = 'resources/ski.jpg'
    output_img_path = 'output.jpg'

    example_image = cv2.imread(example_img_path)

    heatmaps = np.load(heatmaps_path)
    paf = np.load(paf_path)

    cfg = get_default_configuration()

    coordinates = get_coordinates(cfg, heatmaps)

    connections = get_connections(cfg, coordinates, paf)

    skeletons = estimate(cfg, connections)

    output = draw(cfg, example_image, coordinates, skeletons)

    cv2.imwrite(output_img_path, output)

    print(f"Output image: {output_img_path}")

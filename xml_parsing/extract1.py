import xml.etree.ElementTree as ET
from math import sqrt

pixel_spacing = 0.1


def calculate_distance(x1, y1, x2, y2):
    distance = sqrt(
        ((x2 - x1) * pixel_spacing) ** 2 + ((y2 - y1) * pixel_spacing) ** 2
        )
    return distance


def find_point_distances(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    for measure in root.iter('measure'):
        points = measure.findall('Point')
        if len(points) == 2:
            point1 = points[0]
            point2 = points[1]
            x1 = float(point1.get('x'))
            y1 = float(point1.get('y'))
            x2 = float(point2.get('x'))
            y2 = float(point2.get('y'))
            distance = calculate_distance(x1, y1, x2, y2)
            return distance


find_point_distances('dental.xml')

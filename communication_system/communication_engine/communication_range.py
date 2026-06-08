import math

EARTH_RADIUS = 6371  # km


def to_cartesian(lat, lon, alt):

    lat = math.radians(lat)
    lon = math.radians(lon)

    r = EARTH_RADIUS + alt

    x = r * math.cos(lat) * math.cos(lon)
    y = r * math.cos(lat) * math.sin(lon)
    z = r * math.sin(lat)

    return x, y, z


def calculate_distance(node1, node2):

    x1, y1, z1 = to_cartesian(
        node1.latitude,
        node1.longitude,
        node1.altitude_km
    )

    x2, y2, z2 = to_cartesian(
        node2.latitude,
        node2.longitude,
        node2.altitude_km
    )

    distance = math.sqrt(
        (x2 - x1) ** 2 +
        (y2 - y1) ** 2 +
        (z2 - z1) ** 2
    )

    return distance
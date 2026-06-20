# test_coverage_radius.py

from communication_system.coverage_analysis.coverage_radius import (
    calculate_coverage_radius
)


def test_coverage_radius():

    radius = calculate_coverage_radius(
        satellite_altitude=550,
        min_elevation_angle=25
    )

    assert radius > 1000
    assert radius < 5000


if __name__ == "__main__":
    test_coverage_radius()
    print("✅ test_coverage_radius passed")
from communication_system.coverage_analysis.footprint_calculator import (
    calculate_footprint
)


def test_footprint():

    footprint = calculate_footprint(
        satellite_altitude=550,
        min_elevation_angle=25
    )

    assert footprint["radius_km"] > 1000
    assert footprint["area_km2"] > 0


if __name__ == "__main__":
    test_footprint()
    print("✅ test_footprint passed")
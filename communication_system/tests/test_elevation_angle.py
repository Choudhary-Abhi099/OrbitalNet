from communication_system.coverage_analysis.elevation_angle import (
    calculate_elevation_angle
)

def test_satellite_overhead():

    sat = (7000, 0, 0)
    gs = (6371, 0, 0)

    elevation = calculate_elevation_angle(
        sat,
        gs
    )

    assert elevation > 89


if __name__ == "__main__":
    test_satellite_overhead()
    print("✅ test_satellite_overhead passed")
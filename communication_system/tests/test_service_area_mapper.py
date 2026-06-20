from communication_system.coverage_analysis.service_area_mapper import (
    generate_service_area
)


def test_service_area():

    service_area = generate_service_area(
        satellite_id="SAT-001",
        latitude=28.61,
        longitude=77.20,
        altitude=550
    )

    assert service_area["coverage_radius_km"] > 1000
    assert service_area["coverage_area_km2"] > 0


if __name__ == "__main__":
    test_service_area()
    print("✅ test_service_area passed")
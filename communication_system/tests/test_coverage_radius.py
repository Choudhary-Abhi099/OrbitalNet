from communication_system.coverage_analysis.coverage_radius import (
    calculate_coverage_radius
)

altitude = 550

radius = calculate_coverage_radius(altitude)

print(f"Coverage Radius = {radius:.2f} km")
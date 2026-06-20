from communication_system.propagation_engine.fspl import (
    calculate_fspl
)


def test_fspl():

    loss = calculate_fspl(
        distance_km=1000,
        frequency_ghz=12
    )

    assert loss > 100
    assert loss < 200


if __name__ == "__main__":
    test_fspl()
    print("test_fspl passed")
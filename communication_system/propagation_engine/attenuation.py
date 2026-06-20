def calculate_attenuation(
    weather_loss_db=0.0,
    atmospheric_loss_db=0.0,
    additional_loss_db=0.0
):
    return (
        weather_loss_db
        + atmospheric_loss_db
        + additional_loss_db
    )
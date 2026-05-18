def validate_baggage(baggage_weight, baggage_type, passenger_class, flight_type, hazardous_item, passport_valid):
    # Logika minimal dari Orang 1 biar test_coupon.py jadi ijo
    if hazardous_item:
        return False
    if flight_type == "international" and not passport_valid:
        return False
    return True
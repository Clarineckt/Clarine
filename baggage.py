def validate_baggage(baggage_weight, baggage_type, passenger_class, flight_type, hazardous_item, passport_valid):
    # TODO: Fitur pengecekan berat (carry-on & checked) akan diimplementasikan oleh anggota tim lain
    # Validasi barang berbahaya mutlak dilarang
    if hazardous_item:
        return False
    # Validasi penerbangan internasional wajib menyertakan paspor aktif
    if flight_type == "international" and not passport_valid:
        return False
        
    if baggage_type == "carry-on" and baggage_weight > 7:
        return False
    return True # Done Clarine
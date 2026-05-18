from baggage import validate_baggage

def test_penerbangan_domestik_normal_harus_lolos():
    # Kondisi aman semua, harusnya lolos (True)
    assert validate_baggage(5, "carry-on", "economy", "domestic", False, True) == True

def test_internasional_wajib_paspor():
    # Internasional tapi paspor False, harus direject (False)
    assert validate_baggage(5, "carry-on", "economy", "international", False, False) == False
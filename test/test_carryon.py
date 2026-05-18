from baggage import validate_baggage

def test_kabin_overweight_harus_gagal():
    # Berat 10kg harusnya False, tapi karena fungsi lu belum update, dia bakal balikin True (FAILED/RED)
    assert validate_baggage(10, "carry-on", "economy", "domestic", False, True) == False
from email_validator_test.email_validator import is_valid_email

def test_valid_email():
    assert is_valid_email('example@example.com') == True

def test_valid_email_with_numbers():
    assert is_valid_email('user123@example.com') == True

def test_invalid_email_no_at_symbol():
    assert is_valid_email('example.com') == False

def test_invalid_email_no_domain():
    assert is_valid_email('example@') == False

def test_invalid_email_special_characters():
    assert is_valid_email('user!@example.com') == False

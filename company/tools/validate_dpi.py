def validate_dpi(dpi_number):
    """
    Validate a DPI number.

    Args:
        dpi_number (str): The DPI number to validate.

    Returns:
        bool: True if the DPI number is valid, False otherwise.
    """
    try:
        # Remove spaces and hyphens from the DPI number
        dpi_number = dpi_number.replace(" ", "").replace("-", "")

        # Check if it has exactly 13 digits
        if len(dpi_number) != 13:
            return False

        # Check if it contains only numeric characters
        if not dpi_number.isdigit():
            return False

        # Calculate the checksum
        checksum = 0
        for i in range(12):
            digit = int(dpi_number[i])
            checksum += digit * (2 if i % 2 == 0 else 1)

        checksum_digit = (10 - (checksum % 10)) % 10

        # Compare the checksum digit with the last digit of the DPI
        return checksum_digit == int(dpi_number[12])

    except ValueError:
        return False

def validate_nit(nit):
    """
    Validates whether a Guatemalan NIT (Número de Identificación Tributaria) is correct.
    :param nit: String representing the NIT (may include hyphens).
    :return: Boolean value indicating whether the NIT is valid or not.
    """
    nit_clean = nit.replace(" ", "").replace(
        "-", "")  # Remove spaces and hyphens
    if nit_clean.isdigit() and len(nit_clean) == 8:
        # Extract the verifier digit (last digit or 'k')
        verifier_digit = nit_clean[-1].lower()
        verifier_digit = 10 if verifier_digit == "k" else int(verifier_digit)

        # Calculate the weighted sum of the digits
        weighted_sum = sum((int(digit) * (8 - i))
                           for i, digit in enumerate(nit_clean[:-1]))

        # Check if the NIT is valid
        return (11 - (weighted_sum % 11)) % 11 == verifier_digit
    else:
        return False

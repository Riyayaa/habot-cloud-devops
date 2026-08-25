DCYN_YES = "Yes"
DCYN_NO = "No"


def to_dcyn(value: bool) -> str:
    """Convert a boolean into a deterministic DCYN Yes/No value."""
    if value is True:
        return DCYN_YES

    if value is False:
        return DCYN_NO

    raise ValueError("DCYN value must be strictly True or False")


def requires_support_dcyn(requires_support: bool) -> str:
    """Convert requires_support into the DCYN Yes/No value."""
    return to_dcyn(requires_support)


_YES_INPUTS = frozenset({"yes", "y", "true", "1", True, 1})
_NO_INPUTS = frozenset({"no", "n", "false", "0", False, 0})


def from_raw_input(value) -> bool:
    """
    Convert explicitly recognized Yes/No input to a strict boolean.
    Reject anything ambiguous.
    """
    normalized = value.strip().lower() if isinstance(value, str) else value

    if normalized in _YES_INPUTS:
        return True
    if normalized in _NO_INPUTS:
        return False

    raise ValueError(
        f"'{value}' is not a recognized Yes/No input for requires_support."
    )

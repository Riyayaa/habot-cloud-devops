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

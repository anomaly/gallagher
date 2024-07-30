""" Constants in use for the CLI

This package contains definitions such as colours or output
messages that are shared across various CLI endpoints.
"""

# Define colors for each severity level (0-9)
# See: https://rich.readthedocs.io/en/stable/appendix/colors.html
SEVERITY_COLOURS = [
    "grey",     # 0 - least severe
    "chartreuse1",
    "gold1",
    "yellow",
    "orange1",
    "deep_pink1",
    "deep_pink2",
    "deep_pink3",
    "red1",
    "red3",  # 9 - most severe
]

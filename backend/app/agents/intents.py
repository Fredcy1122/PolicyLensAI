from enum import Enum


class Intent(str, Enum):
    LEGAL = "legal"
    CUSTOMS = "customs"
    TRADE = "trade"
    FINANCE = "finance"
    POLICY = "policy"
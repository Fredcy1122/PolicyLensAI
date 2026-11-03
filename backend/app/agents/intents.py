from enum import Enum


class Intent(str, Enum):
    RETRIEVAL = "retrieval"
    SUMMARY = "summary"
    COMPARISON = "comparison"
    METADATA = "metadata"
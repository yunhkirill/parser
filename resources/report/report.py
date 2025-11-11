from enum import Enum
from typing import  Optional
from dataclasses import dataclass

class Error(Enum):
    SYNTAX_ERROR = "SYNTAX_ERROR"
    HIERARCHY_CYCLE = "HIERARCHY_CYCLE"
    MISSING_BLOCK = "MISSING_BLOCK"
    PIN_MISMATCH = "PIN_MISMATCH"
    DISCONNECTED_PIN = "DISCONNECTED_PIN"
    ORPHANED_NET = "ORPHANED_NET"
    DUPLICATE_NAME = "DUPLICATE_NAME"

@dataclass
class ReportEntry:
    error : Error = None
    message : Optional[str] = None
    location: Optional[str] = None
    line : Optional[int] = None
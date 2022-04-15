from __future__ import annotations

from typing import Any, Union
from pydoc import locate

def parse_type(val: Any, expected_type: type) -> Union[None, Any]:
    """Parse a type into it's expected type"""
    if val is None and expected_type != bool:
        return None
    if expected_type == bool and isinstance(val, str):
        if val.lower() == "true":
            return True
        elif val.lower() == "false":
            return False
    handler = locate(expected_type.__name__)
    if handler == None:
        # figure this shit out
        raise Exception(f"Can't parse {val} to {expected_type}")
    else:
        return handler(val)

def safe_get(obj: dict, key: str) -> Any:
    """Safely get a key from a dictionary. Handles the case where the key doesn't exist"""
    if key in obj:
        return obj[key]
    return None
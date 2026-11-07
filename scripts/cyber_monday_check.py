"""Compare a Cyber Monday candidate with a Black Friday baseline."""

from typing import Any, Dict


def comparable(baseline: Dict[str, Any], cyber: Dict[str, Any]) -> bool:
    keys = ("title", "model", "variant", "condition", "currency")
    return all(baseline.get(k) == cyber.get(k) for k in keys if baseline.get(k) is not None)


def compare_prices(baseline: Dict[str, Any], cyber: Dict[str, Any]) -> Dict[str, Any]:
    if not comparable(baseline, cyber):
        return {"status": "not_comparable", "better": "unknown", "savings": None}
    try:
        old = float(baseline["price"])
        new = float(cyber["price"])
    except (KeyError, TypeError, ValueError):
        return {"status": "missing_price", "better": "unknown", "savings": None}
    return {
        "status": "compared",
        "better": "cyber_monday" if new < old else "black_friday" if old < new else "tie",
        "savings": round(old - new, 2),
    }

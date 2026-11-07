"""Pure helpers for normalizing and ranking worker findings."""

from typing import Any, Dict, Iterable, List


def discount_percent(current_price: float, comparison_price: float) -> float:
    if comparison_price <= 0 or current_price < 0:
        raise ValueError("prices must be non-negative and comparison_price must be positive")
    return round((comparison_price - current_price) / comparison_price * 100, 2)


def rank_deals(deals: Iterable[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Return a new list, highest score first; do not mutate worker records."""
    return sorted(deals, key=lambda d: float(d.get("score", 0)), reverse=True)


def normalize_candidate(raw: Dict[str, Any]) -> Dict[str, Any]:
    required = ("title", "url", "price", "currency", "merchant")
    missing = [key for key in required if not raw.get(key)]
    if missing:
        raise ValueError("missing required fields: " + ", ".join(missing))
    result = dict(raw)
    result["price"] = float(raw["price"])
    result["currency"] = str(raw["currency"]).upper()
    result.setdefault("verification_status", "needs_live_check")
    return result

"""Validate evidence fields without pretending to perform a live web check."""

from typing import Any, Dict, List
from urllib.parse import urlparse

REQUIRED_FIELDS = ("title", "url", "price", "currency", "merchant", "timestamp_utc")


def verify_deal(deal: Dict[str, Any], minimum_discount_percent: float = 15.0) -> Dict[str, Any]:
    reasons: List[str] = []
    for field in REQUIRED_FIELDS:
        if deal.get(field) in (None, ""):
            reasons.append(f"missing {field}")

    parsed = urlparse(str(deal.get("url", "")))
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        reasons.append("url is not an absolute http(s) URL")
    try:
        price = float(deal.get("price", -1))
        if price < 0:
            reasons.append("price must be non-negative")
    except (TypeError, ValueError):
        reasons.append("price is not numeric")

    if not deal.get("in_stock", False):
        reasons.append("in_stock is not confirmed")
    if not deal.get("price_evidence"):
        reasons.append("price_evidence is missing")
    if deal.get("discount_percent") is not None:
        try:
            if float(deal["discount_percent"]) < minimum_discount_percent:
                reasons.append("discount is below minimum threshold")
        except (TypeError, ValueError):
            reasons.append("discount_percent is not numeric")
    else:
        reasons.append("discount_percent is missing")

    return {
        "status": "confirmed" if not reasons else "needs_live_check",
        "reasons": reasons,
        "passed": not reasons,
    }

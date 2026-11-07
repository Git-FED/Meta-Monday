import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from cyber_monday_check import compare_prices
from deal_search import discount_percent
from stripe_funding import FundingPlan, validate_funding
from verify_deal import verify_deal
from worker_split import make_plan


class DealTests(unittest.TestCase):
    def test_item_plan_has_default_25_25_split(self):
        plan = make_plan("item", "electronics", 50, "headphones")
        self.assertEqual(len(plan), 50)
        self.assertEqual(sum(a.focus == "particular_item" for a in plan), 25)
        self.assertEqual(sum(a.focus == "category_sweep" for a in plan), 25)

    def test_worker_cap_is_enforced(self):
        with self.assertRaises(ValueError):
            make_plan("broad", "electronics", 101)

    def test_discount(self):
        self.assertEqual(discount_percent(80, 100), 20.0)

    def test_verified_deal_requires_evidence(self):
        result = verify_deal({"title": "x", "url": "https://example.com/x", "price": 80, "currency": "USD", "merchant": "Example", "timestamp_utc": "2026-11-27T00:00:00Z", "in_stock": True, "price_evidence": "history", "discount_percent": 20})
        self.assertTrue(result["passed"])

    def test_cyber_comparison(self):
        base = {"title": "x", "model": "m", "variant": "v", "condition": "new", "currency": "USD", "price": 100}
        cyber = {**base, "price": 90}
        self.assertEqual(compare_prices(base, cyber)["better"], "cyber_monday")

    def test_funding_requires_approval(self):
        plan = FundingPlan("campaign", 1000, 1000, user_approved=False)
        with self.assertRaises(PermissionError):
            validate_funding(plan, 2000)


if __name__ == "__main__":
    unittest.main()

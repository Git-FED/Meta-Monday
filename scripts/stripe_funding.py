"""Validate a proposed Muse-owned campaign funding plan; no Stripe calls."""

from dataclasses import dataclass


@dataclass(frozen=True)
class FundingPlan:
    campaign_id: str
    amount_cents: int
    max_single_transaction_cents: int
    currency: str = "USD"
    user_approved: bool = False


def validate_funding(plan: FundingPlan, configured_cap_cents: int) -> None:
    if not plan.campaign_id:
        raise ValueError("campaign_id is required")
    if plan.amount_cents <= 0:
        raise ValueError("funding amount must be positive")
    if plan.max_single_transaction_cents <= 0:
        raise ValueError("single-transaction cap must be positive")
    if plan.amount_cents > configured_cap_cents:
        raise ValueError("funding exceeds configured campaign cap")
    if plan.currency.upper() != "USD":
        raise ValueError("this scaffold is configured for USD only")
    if not plan.user_approved:
        raise PermissionError("explicit user approval is required")


def instructions() -> str:
    return (
        "Use a separate Muse-owned Stripe account funded only for this campaign. "
        "Do not connect a bank-linked user Stripe account. Funding is not purchase approval; "
        "each bid or purchase requires separate human approval."
    )

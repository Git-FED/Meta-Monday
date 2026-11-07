# Instructions

## 1. Define the search

Choose either:

- **Broad search:** a category-wide sweep divided among merchants, subcategories, and product types.
- **Particular item:** 25 workers investigate the named item and 25 workers perform a broad sweep of the related category. Do not allocate more workers unless the user explicitly orders it.

The maximum total worker count is 100. A plan is not a dispatch. The planning command only produces an auditable assignment list.

## 2. Explicitly order dispatch

Before any worker is sent out, a human must review the plan and issue an explicit order identifying:

1. the search mode and category/item;
2. the exact number of workers;
3. the allowed sources or merchant scope;
4. the start and end time;
5. the output destination;
6. the instruction to proceed.

No implied approval, default setting, or prior search counts as an order.

## 3. Worker reporting format

Every worker should return a structured record containing:

- product title, brand, model, and variant;
- merchant and canonical product URL;
- current price, currency, shipping, taxes if known, and required membership;
- stock or availability status;
- promotion terms, expiry, exclusions, and coupon requirements;
- timestamp in UTC;
- price-history or comparison evidence when available;
- exact source text or screenshot reference;
- confidence and unresolved risks.

Workers must not buy, bid, create accounts, enter payment details, or bypass access controls.

## 4. Verify before ranking

Run each candidate through `scripts/verify_deal.py`. A candidate is not a confirmed deal unless the URL, price, timestamp, availability, and evidence requirements in `docs/deal_criteria.md` are met. When live checking is unavailable, mark the candidate `needs_live_check`; never silently treat it as confirmed.

## 5. Black Friday and Cyber Monday

Capture a Black Friday baseline with timestamps. On Cyber Monday, run a new search and compare the same product or a genuinely equivalent model. A lower advertised price is not automatically better if shipping, membership, quantity limits, seller quality, warranty, or variant differ.

## 6. Stripe and bidding

Muse must use a separate Muse-owned Stripe account funded only with the amount the user authorizes. Do not connect Muse to a Stripe account linked to the user's bank account. Funding, bids, and purchases remain disabled until the rules in `docs/stripe_rules.md` are satisfied and the user gives transaction-specific approval.

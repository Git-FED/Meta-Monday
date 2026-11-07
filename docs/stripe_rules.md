# Stripe rules

## Account architecture

Use a separate Stripe account owned and controlled by Muse for campaign funding. The user should transfer only the amount needed for the approved campaign into that account. Never ask the user to connect a Stripe account that is connected to their bank account as Muse's operating account, and never store bank credentials in this repository.

This repository does not connect to Stripe and does not move money. A future implementation must use Stripe's official APIs, secret storage, webhook verification, idempotency keys, audit logs, and least-privilege access.

## Hard limits

Before funding, set all of the following explicitly:

- total campaign funding cap;
- maximum amount for one bid;
- maximum amount for one purchase;
- allowed currency;
- expiration time for unused funds;
- approved campaign and category.

The default configuration sets all monetary caps to zero and Stripe disabled.

## Approval rules

1. Funding requires the user's explicit approval of the amount and campaign.
2. Every bid or purchase requires separate, transaction-specific human approval.
3. A deal recommendation, worker result, or worker assignment is never approval.
4. No automatic rebidding, cascading bids, or checkout retries.
5. Stop if price, seller, shipping, condition, or terms change after approval.
6. Refunds and unused funds must return to the user-controlled destination according to the separate payment implementation's documented process.

## Required audit record

Record campaign ID, approver, amount, currency, timestamp, deal URL, item identity, seller, cap remaining, approval text, and final outcome. Do not record full card numbers, CVV, bank credentials, or secrets.

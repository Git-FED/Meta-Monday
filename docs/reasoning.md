# Reasoning

## Why use multiple workers?

Seasonal promotions are fragmented across retailers, marketplaces, brands, coupon pages, and local inventory. Parallel research improves coverage, but unrestricted parallelism increases duplicate results, false positives, rate-limit risk, and review burden. The system therefore caps the pool at 100 and makes allocation visible before dispatch.

## Why split a particular-item search?

A named product deserves focused comparison across merchants, models, and seller conditions. At the same time, the best value may be a close substitute or a category-level promotion. The default 25/25 split preserves both goals: 25 workers focus on the requested item and 25 sweep the broader category. The remaining capacity is deliberately unused until ordered.

## Why treat Cyber Monday as a comparison, not a fresh list?

The point of Cyber Monday is to detect whether an online offer improves on the Black Friday baseline. Comparison must normalize the item, variant, shipping, fees, membership, seller, warranty, and availability. Otherwise, a cheaper but inferior or unavailable listing can be incorrectly labeled better.

## What makes a deal trustworthy?

A discount percentage alone is weak evidence. A product can be marked up before a sale, have a low-quality seller, require a coupon or membership, or be out of stock. Verification therefore combines live URL, current price, availability, terms, timestamp, and historical or cross-merchant evidence. Unverified candidates remain useful leads but are not promoted as confirmed deals.

## Why separate Stripe funding?

A dedicated Muse-owned Stripe account limits blast radius. The user deposits only the amount approved for the specific campaign, rather than granting Muse access to a payment account connected to a personal or business bank account. Even then, funding is not permission to spend: each bid or purchase needs a separate human approval and must remain within a hard cap.

## Core principle

The system optimizes for auditable recommendations, not maximum automation. Search broadly, verify conservatively, compare like-for-like, and keep money movement human-approved.

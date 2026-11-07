"""Create auditable worker plans; never dispatch workers."""

from dataclasses import dataclass, asdict
from typing import List, Optional

MAX_WORKERS = 100


@dataclass(frozen=True)
class Assignment:
    worker_id: int
    focus: str
    category: str
    item: Optional[str] = None


def make_plan(mode: str, category: str, workers: int, item: Optional[str] = None) -> List[Assignment]:
    if mode not in {"broad", "item"}:
        raise ValueError("mode must be 'broad' or 'item'")
    if not 1 <= workers <= MAX_WORKERS:
        raise ValueError(f"workers must be between 1 and {MAX_WORKERS}")
    if mode == "item" and not item:
        raise ValueError("item mode requires an item")
    if mode == "item" and workers < 50:
        raise ValueError("item mode requires at least 50 workers for the default 25/25 split")

    assignments: List[Assignment] = []
    if mode == "item":
        for i in range(1, 26):
            assignments.append(Assignment(i, "particular_item", category, item))
        for i in range(26, 51):
            assignments.append(Assignment(i, "category_sweep", category, None))
        for i in range(51, workers + 1):
            assignments.append(Assignment(i, "reserved_unassigned", category, None))
    else:
        for i in range(1, workers + 1):
            assignments.append(Assignment(i, "broad_category_search", category, None))
    return assignments


def plan_as_dicts(*args, **kwargs):
    return [asdict(a) for a in make_plan(*args, **kwargs)]

def category_summary(expenses):
    summary = {}
    for e in expenses:
        summary[e.category] = summary.get(e.category, 0) + e.amount
    return summary

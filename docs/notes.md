## Stakeholders & Search Goals

**1. Business Analyst**
- Goal: Identify high-value orders (`amount > 5000`) to study customer behavior.
- Indexing reduced query time from 3s to 0.3s.

**2. Marketing Team**
- Goal: Run keyword-based product searches (e.g., "celular", "tv smart") for trending products.
- Full-text index improved performance from full table scan (4s) to indexed search (0.5s).

## EXPLAIN Output Analysis

- Before indexing: full table scan, rows examined > 80,000
- After indexing: index used, key: `ft_product`, rows examined ~200

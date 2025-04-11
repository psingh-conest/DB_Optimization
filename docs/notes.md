### Query Performance Analysis

**Scalar Field Test:**
- Query: `SELECT * FROM orders WHERE amount > 500;`
- Time Before Index: 
- Time After Index: 

**Full-Text Search:**
- Query: `MATCH(product_name) AGAINST('wireless headphones')`
- Time Before Index: 
- Time After Index: 

**EXPLAIN Findings:**
- Scalar query used full table scan before index
- Full-text search used FTS index after creation

---

### Who Benefits from These Queries?

1. **Sales Analysts**:
   - Want to filter high-value orders quickly → scalar indexing improves productivity.

2. **Customer Support Teams**:
   - Search products by name → full-text index allows faster case lookups.

3. **Business Intelligence Teams**:
   - Aggregating large queries for dashboards → index optimization helps real-time reporting.

---

### Conclusion

Indexing drastically improved query times. This optimization supports faster customer insights and business decisions, saving time and enhancing user experience across the board.


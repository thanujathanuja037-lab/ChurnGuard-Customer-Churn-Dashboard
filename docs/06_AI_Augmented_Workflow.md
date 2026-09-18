# AI-Augmented Development Process

This project was built using AI tooling to accelerate execution — requirement framing, SQL/DAX drafting, debugging, and documentation — while all design decisions (schema design, DAX logic validation, business interpretation of insights) were owned and validated independently.
```mermaid
flowchart TD
    A[Business Requirement] --> AI1[🤖 AI: Requirement Analysis]
    AI1 --> B[Data Sources: SQL / CSV / Excel]
    B --> AI2[🤖 AI: SQL Assistance]
    AI2 --> C[Power Query / ETL]
    C --> C1[Cleaning]
    C --> C2[M Code]
    C --> C3[Parameters]
    C1 --> AI3[🤖 AI: ETL Logic Review]
    C2 --> AI3
    C3 --> AI3
    AI3 --> D[Star Schema]
    D --> AI4[🤖 AI: Model Suggestions]
    AI4 --> E[DAX Layer]
    E --> AI5[🤖 AI: DAX Creation / Debugging]
    AI5 --> F1[Executive Report]
    AI5 --> F2[Operational Report]
    F1 --> G1[Insights & Decisions]
    F2 --> G2[Drillthrough]
    G1 --> AI6[🤖 AI: Insight Analysis]
    G2 --> AI6
    AI6 --> H[Testing & Validation]
    H --> AI7[🤖 AI: RLS Guidance]
    AI7 --> I[RLS Design]
    I --> J[Performance Test]
    J --> AI8[🤖 AI: Optimization Ideas]
    AI8 --> K[Documentation]
    K --> AI9[🤖 AI: README / Docs Generation]
    AI9 --> L[GitHub]
```
| Stage | AI Assistance | Your Contribution |
|---|---|---|
| Requirement Analysis | Helped frame churn KPIs from business goals | Chose which KPIs mattered for telecom churn specifically |
| ETL | Suggested TotalCharges cleaning approach | Validated against actual data quirk (11 blank rows) |
| DAX Layer | Drafted Churn Risk Score formula structure | Tuned weights (40/25/20/15) based on domain logic |
| RLS | Explained USERPRINCIPALNAME() pattern | Designed the manager-territory mapping |
| Documentation | Drafted README structure | Wrote all business insights and final narrative |
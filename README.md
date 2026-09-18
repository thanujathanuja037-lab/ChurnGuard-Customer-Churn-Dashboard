# ChurnGuard — Customer Churn Analysis Dashboard

## Business Problem
Telecom companies lose significant recurring revenue to undetected customer churn. This dashboard identifies at-risk segments and quantifies revenue exposure.

## Architecture
Kaggle CSV → Python ETL (pandas/SQLAlchemy) → MySQL → Power BI (star schema)
See docs/05_Architecture_Diagram.png

## Key Features
- Star schema: 1 fact table, 4 dimension tables
- Advanced DAX: Churn Risk Score, Revenue Simulator
- Row-Level Security by contract manager
- Drillthrough Customer 360 page

## Screenshots
![Segmentation](Screenshots/image.png.png)
![Risk Scoring](Screenshots/page3.png.png.png)
## Key Insights
- [Write 3-5 bullets from your actual dashboard numbers]

## Deployment Note
Power BI Service deployment (scheduled refresh via Gateway, Dev/Prod workspaces) was designed and documented in docs/04_Deployment_Process.md but not executed live in this submission due to time constraints. All modeling, DAX, and RLS were fully built and validated in Power BI Desktop.

## Documentation
- [Data Dictionary](docs/02_Data_Dictionary.md)
- [Test Cases](docs/03_Test_Cases.md)
- [AI-Augmented Workflow](docs/06_AI_Augmented_Workflow.md)

## Tech Stack
MySQL, Python, Power BI Desktop, DAX, Git/GitHub
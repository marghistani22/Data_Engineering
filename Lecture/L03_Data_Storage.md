# **Lecture 03: Introduction to Data Storage**

This lecture introduces data warehouses, their purpose, and how they differ from traditional databases. You will also learn about key concepts like OLAP, schema design, and the role of data warehouses in modern analytics.

---

## 🎯 **Learning Objectives**
By the end of this lecture, you will:
- Understand the purpose and characteristics of data warehouses.
- Differentiate between OLTP and OLAP systems.
- Learn about star and snowflake schemas used in data warehouse design.
- Recognize the role of data warehouses in supporting business intelligence and analytics.

---

## 📚 **Lecture Outline**

### 1. **Recap of Previous Lectures**
   - **Lecture 01**: Overview of data engineering and its role in data ecosystems.
   - **Lecture 02**: Basics of database design and normalization.
   - **Lecture 03**: Practical setup of SQLite and hands-on DML exercises.

### 2. **Introduction to Data Warehousing**
   - Definition: A data warehouse is a centralized repository designed for query and analysis, optimized for reporting and business intelligence.
   - Characteristics: Subject-oriented, integrated, time-variant, and non-volatile.
   - Purpose: To store historical data for strategic decision-making.

### 3. **OLTP vs. OLAP**
   - **OLTP (Online Transaction Processing)**:
     - Optimized for daily operations and transactional tasks.
     - Example: Banking, e-commerce.
   - **OLAP (Online Analytical Processing)**:
     - Optimized for analysis and reporting.
     - Example: Sales trends, customer behavior analysis.

| Feature          | OLTP (Application Database)         | OLAP (Analytical Database)       |
|-----------------|------------------------------------|----------------------------------|
| **Purpose**     | Fast transactions, real-time updates | Aggregated data analysis, reporting |
| **Data Structure** | Normalized (efficient writes)   | Denormalized (efficient reads)   |
| **Operations**  | Read/write-heavy (small transactions) | Read-heavy (complex queries) |
| **Examples**    | Banking apps, e-commerce transactions | Data warehouses, BI dashboards |


### 4. **Data Warehouse Architecture**
   - Components:
     - Source systems.
     - ETL (Extract, Transform, Load) processes.
     - Data warehouse storage (fact and dimension tables).
     - Reporting and analytics tools.
   - Layers:
     - Staging area.
     - Data integration layer.
     - Access layer.

### 5. **Schema Design for Data Warehouses**
   - **Star Schema**:
     - Simple structure with fact tables connected to dimension tables.
   - **Snowflake Schema**:
     - Normalized design with hierarchical relationships between dimension tables.
   - Comparison of schemas: Ease of use vs. complexity.

### 6. **Practical Applications of Data Warehouses**
   - Real-world use cases:
     - Retail: Sales and inventory analysis.
     - Finance: Risk assessment and fraud detection.
     - Healthcare: Patient data and treatment analysis.
---

## 📌 **Key Takeaways**
- Data warehouses are optimized for analytics and decision-making, unlike transactional databases.
- Understanding OLAP and schema design is essential for building effective data warehouses.
- ETL processes are critical for integrating and preparing data for analysis.

---

### **Resources for Lecture 03**

#### 📑 **Lecture Slides**
- [Access the slides on Canva](https://www.canva.com/design/DAGeWfr3oOQ/el0lKlRJJPhrHePYjPcd0A/view?utm_content=DAGeWfr3oOQ&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=h7f152b91b3)

#### 📂 **Further Reading**
- [Data Piplelines Pocket Reference](https://www.amazon.com/Data-Pipelines-Pocket-Reference-Processing/dp/1492087831)
- [TextBook](https://www.amazon.com/Fundamentals-Data-Engineering-Robust-Systems/dp/1098108302)

---



# **Lecture 03: Introduction to Data Warehouse**

Welcome to the fourth lecture of the **Data Engineering Principles** course! This lecture introduces data warehouses, their purpose, and how they differ from traditional databases. You will also learn about key concepts like OLAP, schema design, and the role of data warehouses in modern analytics.

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
### 📝 **In-class Assignment**
1. **Template**: Use the provided [Google Docs template](https://docs.google.com/document/d/1pnFcJMD60s7axZ195MbQuxNfZSzVf0uYNNLPZXWCAW4/edit?usp=sharing) to complete your assignment.
2. **File Naming**: Rename the document using the format: `Lecture03_firstname_lastname`.
3. **Submission**: Upload your completed assignment to the **Assignment** folder.


## 🛠️ **Activity**
1. **Design Exercise**: Create a basic star schema for MMDT data.
   - Identify fact and dimension tables.
   - Optional: Implement the schema using SQLite and populate it with sample data.

2. **Schema Documentation**: Document the schema and explain your design choices.

---

## 📌 **Key Takeaways**
- Data warehouses are optimized for analytics and decision-making, unlike transactional databases.
- Understanding OLAP and schema design is essential for building effective data warehouses.
- ETL processes are critical for integrating and preparing data for analysis.

---

### **Resources for Lecture 04**

#### 📑 **Lecture Slides**
- [Access the slides on Canva](https://www.canva.com/design/DAGcml-RWoo/lq2ZGYKeJPEFLEd01bulVw/view?utm_content=DAGcml-RWoo&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=haa70aab56b)

#### 📂 **Further Reading**
- [Data Piplelines Pocket Reference](https://www.amazon.com/Data-Pipelines-Pocket-Reference-Processing/dp/1492087831)
- [TextBook](https://www.amazon.com/Fundamentals-Data-Engineering-Robust-Systems/dp/1098108302)

---



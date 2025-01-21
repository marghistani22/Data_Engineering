# Lecture 02: Database Design

Welcome to Lecture 02 of the **Data Engineering Principles** course! This lecture covers the fundamentals of database design, including its importance, types of database models, and core concepts like normalization and Entity-Relationship Diagrams (ERD).

---

## 🎯 **Learning Objectives**
By the end of this lecture, you will:
- Understand what database design is and why it is essential.
- Explore different types of database models.
- Learn to create and interpret Entity-Relationship Diagrams (ERD).
- Understand normalization and its importance in reducing redundancy.
- Differentiate between Data Definition Language (DDL) and Data Manipulation Language (DML).

---

## 📚 **Lecture Outline**

### 1. **What is Database Design?**
   - The process of structuring and organizing data to efficiently store, manage, and retrieve it.
   - Key goals:
     - Reduce redundancy.
     - Ensure data integrity.
     - Optimize performance.

### 2. **Types of Database Models**
   - **Relational Model**: Organizes data into tables with rows and columns. Most widely used.
   - **Hierarchical Model**: Represents data in a tree-like structure with parent-child relationships.
   - **Network Model**: Similar to the hierarchical model but allows many-to-many relationships.
   - **NoSQL Models**:
     - Key-Value Stores.
     - Document Stores.
     - Columnar Databases.
     - Graph Databases.

### 3. **Entity-Relationship Diagram (ERD)**
   - A visual representation of entities, their attributes, and the relationships between them.
   - Components:
     - **Entity**: Represents an object or concept (e.g., Student, Course).
     - **Attribute**: Describes properties of an entity (e.g., Name, ID).
     - **Relationship**: Defines associations between entities (e.g., "Enrolls In").
   - Example:
     ```text
     Student --(Enrolls In)-- Course
     ```

### 4. **Normalization**
   - The process of organizing a database to minimize redundancy and dependency.
   - **Normal Forms**:
     - **1NF**: Ensures that columns contain atomic values.
     - **2NF**: Removes partial dependencies.
     - **3NF**: Removes transitive dependencies.
   - Benefits:
     - Saves storage space.
     - Improves data consistency.
     - Enhances query performance.

### 5. **Difference Between DDL and DML**
   - **Data Definition Language (DDL)**:
     - Defines the structure of the database (e.g., CREATE, ALTER, DROP).
     - Example:
       ```sql
       CREATE TABLE students (
           student_id INT PRIMARY KEY,
           name VARCHAR(50)
       );
       ```
   - **Data Manipulation Language (DML)**:
     - Manages data within the database (e.g., INSERT, UPDATE, DELETE).
     - Example:
       ```sql
       INSERT INTO students (student_id, name) VALUES (1, 'John Doe');
       ```

---

## 📂 **Resources**

### 📑 **Lecture Slides**
- [View the lecture slides on Canva][(https://www.canva.com/design/DAGcm9szo3M/91uQo5crMu2UycpqzJzkJw/view?utm_content=DAGcm9szo3M&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=heb02958cb3)]

### 📝 **In-class Assignment**
1. **Template**: Use the provided [Google Docs template](https://docs.google.com/document/d/1pnFcJMD60s7axZ195MbQuxNfZSzVf0uYNNLPZXWCAW4/edit?usp=sharing) to complete your assignment.
2. **File Naming**: Rename the document using the format: `Lecture02_firstname_lastname`.
3. **Submission**: Upload your completed assignment to the **Assignments** folder.

---

## 📌 **Key Takeaways**
- Database design is critical for managing and organizing data effectively.
- ERDs help visualize entities, attributes, and relationships.
- Normalization ensures data integrity and reduces redundancy.
- DDL defines database structure, while DML manages data.

---


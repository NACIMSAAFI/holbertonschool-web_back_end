# MySQL Advanced

## 📚 Curriculum
**Holberton School – Specialization: Web Stack Programming**  
**Cohort:** C#22 (2024)  
**Project:** MySQL Advanced  
**Level:** Novice  
**Weight:** 1  

---

## 📝 Description

This project focuses on **advanced features of MySQL**. The goal is to become comfortable working with constraints, indexes, stored procedures, views, and triggers to build powerful and optimized database structures.

---

## 🎯 Learning Objectives

By the end of this project, you should be able to explain and apply the following concepts:

- ✅ How to create tables with constraints (`PRIMARY KEY`, `UNIQUE`, `NOT NULL`, etc.)
- ✅ How to optimize queries by adding indexes
- ✅ What stored procedures are, and how to implement them in MySQL
- ✅ What views are, and how to implement them
- ✅ What triggers are, and how to create them

---

## 📌 Project Requirements

- All SQL files executed on **Ubuntu 20.04 LTS** with **MySQL 8.0**
- Each file:
  - Starts with a **comment describing the task**
  - Contains **SQL keywords in uppercase**
  - Ends with a **new line**
  - Includes **a comment before each SQL query**
- A `README.md` file at the root of the project is **mandatory**
- File lengths tested using `wc`

---

## 📎 Resources

To help complete this project, you can refer to:

- [MySQL cheatsheet](https://devhints.io/mysql)
- [MySQL Performance: How To Leverage Indexing](https://www.percona.com/blog/2020/08/12/mysql-performance-how-to-leverage-mysql-database-indexing/)
- [Stored Procedures and Functions](https://dev.mysql.com/doc/refman/8.0/en/stored-routines.html)
- [Triggers](https://dev.mysql.com/doc/refman/8.0/en/triggers.html)
- [Views](https://dev.mysql.com/doc/refman/8.0/en/views.html)
- [CREATE TABLE Statement](https://dev.mysql.com/doc/refman/8.0/en/create-table.html)
- [CREATE INDEX Statement](https://dev.mysql.com/doc/refman/8.0/en/create-index.html)

---

## 🚀 Example Command: Importing a SQL Dump

```bash
echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
curl "https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows
echo "SELECT * FROM tv_genres" | mysql -uroot -p hbtn_0d_tvshows

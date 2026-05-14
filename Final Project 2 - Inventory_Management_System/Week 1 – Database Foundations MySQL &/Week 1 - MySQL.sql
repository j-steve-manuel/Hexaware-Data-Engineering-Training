-- Create Database
CREATE DATABASE InventoryDB;
USE InventoryDB;

-- 1. Tables Creation
CREATE TABLE suppliers (
    supplier_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    contact_email VARCHAR(100)
);

CREATE TABLE products (
    product_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    reorder_level INT,
    supplier_id INT,
    FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id),
    INDEX (product_id) -- Requirement: Index for quick search
);

CREATE TABLE warehouses (
    warehouse_id INT PRIMARY KEY AUTO_INCREMENT,
    location VARCHAR(100),
    INDEX (warehouse_id)
);

CREATE TABLE stock_movements (
    movement_id INT PRIMARY KEY AUTO_INCREMENT,
    product_id INT,
    warehouse_id INT,
    quantity INT,
    movement_type ENUM('IN', 'OUT'),
    movement_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES products(product_id),
    FOREIGN KEY (warehouse_id) REFERENCES warehouses(warehouse_id)
);

-- 2. CRUD Operations
INSERT INTO suppliers (name, contact_email) VALUES ('Global Tech', 'sales@gt.com');
INSERT INTO products (name, reorder_level, supplier_id) VALUES ('Laptop L4', 10, 1);
INSERT INTO warehouses (location) VALUES ('Main Hub - Mumbai');

-- Update stock levels 
UPDATE stock_movements SET quantity = 55 WHERE movement_id = 1;

-- 3. Stored Procedure for Reordering
DELIMITER //
CREATE PROCEDURE GetLowStockProducts()
BEGIN
    SELECT p.name, SUM(sm.quantity) as total_stock, p.reorder_level
    FROM products p
    JOIN stock_movements sm ON p.product_id = sm.product_id
    GROUP BY p.product_id
    HAVING total_stock < p.reorder_level;
END //
DELIMITER ;
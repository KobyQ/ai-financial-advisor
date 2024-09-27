import sqlite3

# Create a new SQLite3 database and establish a connection
conn = sqlite3.connect('/Volumes/QDrive/Workspace/portfolio-projects/ai-financial-advisor/ai-financial-advisor.db')
cursor = conn.cursor()

# Create a table for clients
cursor.execute('''
CREATE TABLE IF NOT EXISTS clients (
    client_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    income REAL NOT NULL,
    risk_tolerance TEXT NOT NULL,  -- Low, Medium, High
    financial_goal TEXT NOT NULL   -- Retirement, Education, Investment
);
''')

# Create a table for fintech products
cursor.execute('''
CREATE TABLE IF NOT EXISTS fintech_products (
    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_name TEXT NOT NULL,
    product_type TEXT NOT NULL,    -- Savings, Investment, Loan, Insurance
    risk_level TEXT NOT NULL,      -- Low, Medium, High
    expected_return REAL NOT NULL, -- Expected return in percentage
    minimum_income REAL NOT NULL   -- Minimum income requirement
);
''')

# Create a table for recommendations
cursor.execute('''
CREATE TABLE IF NOT EXISTS recommendations (
    recommendation_id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    recommendation_reason TEXT,
    FOREIGN KEY (client_id) REFERENCES clients(client_id),
    FOREIGN KEY (product_id) REFERENCES fintech_products(product_id)
);
''')

# Insert sample data for clients
clients_data = [
    ('Alice Johnson', 28, 45000, 'Medium', 'Investment'),
    ('Bob Smith', 35, 80000, 'High', 'Retirement'),
    ('Charlie Davis', 22, 30000, 'Low', 'Education'),
    ('Diana Martinez', 45, 120000, 'High', 'Retirement'),
    ('Evan Lewis', 55, 95000, 'Medium', 'Retirement')
]

cursor.executemany('''
INSERT INTO clients (name, age, income, risk_tolerance, financial_goal)
VALUES (?, ?, ?, ?, ?);
''', clients_data)

# Insert sample data for fintech products
products_data = [
    ('Growth Stock Portfolio', 'Investment', 'High', 15.0, 50000),
    ('Retirement Bond Fund', 'Investment', 'Low', 5.0, 20000),
    ('Education Savings Plan', 'Savings', 'Low', 3.0, 10000),
    ('High-Yield Savings Account', 'Savings', 'Low', 1.5, 10000),
    ('Cryptocurrency Fund', 'Investment', 'High', 25.0, 60000),
    ('Short-Term Loan', 'Loan', 'Medium', 12.0, 30000),
    ('Health Insurance Plan', 'Insurance', 'Low', 0.0, 20000)
]

cursor.executemany('''
INSERT INTO fintech_products (product_name, product_type, risk_level, expected_return, minimum_income)
VALUES (?, ?, ?, ?, ?);
''', products_data)

# Commit changes and close the connection
conn.commit()
conn.close()

"/Volumes/QDrive/Workspace/portfolio-projects/ai-financial-advisor/ai-financial-advisor.db"

USE subscriber_db;
ALTER TABLE subscriber ADD COLUMN subscription_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP;

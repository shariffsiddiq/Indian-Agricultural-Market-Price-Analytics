USE indian_agricultural_market_prices_cleaned;
-- 2.DATA VALIDATION

-- SELECT COUNT(*) AS total_records
-- FROM indian_agricultural_market_prices_cleaned;

-- SELECT
--     MIN(Arrival_Date) AS first_date,
--     MAX(Arrival_Date) AS last_date
-- FROM indian_agricultural_market_prices_cleaned;

-- Basic SQL analysis

-- Query 1 — Number of states
-- SELECT COUNT(DISTINCT State) AS total_states
-- FROM indian_agricultural_market_prices_cleaned;

-- Query 2 — Number of markets;
-- SELECT COUNT(DISTINCT Market) AS total_markets
-- FROM indian_agricultural_market_prices_cleaned;

-- Query 3 — Number of commodities
-- SELECT COUNT(DISTINCT Commodity) AS total_commodities
-- FROM indian_agricultural_market_prices_cleaned;

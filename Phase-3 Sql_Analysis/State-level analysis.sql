USE indian_agricultural_market_prices_cleaned;
-- 3.State-level analysis
-- Records by state
-- SELECT
--     State,
--     COUNT(*) AS record_count
-- FROM indian_agricultural_market_prices_cleaned
-- GROUP BY State
-- ORDER BY record_count DESC;


-- Average modal price by state
-- SELECT
--     State,
--     ROUND(AVG(Modal_Price), 2) AS avg_modal_price
-- FROM indian_agricultural_market_prices_cleaned
-- GROUP BY State
-- ORDER BY avg_modal_price DESC;

-- State market coverage
-- SELECT
--     State,
--     COUNT(DISTINCT Market) AS total_markets,
--     COUNT(*) AS total_records
-- FROM indian_agricultural_market_prices_cleaned
-- GROUP BY State
-- ORDER BY total_markets DESC;
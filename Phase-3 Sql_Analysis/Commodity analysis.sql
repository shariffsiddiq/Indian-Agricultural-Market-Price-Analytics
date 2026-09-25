USE indian_agricultural_market_prices_cleaned;
-- 4.Commodity analysis
-- Top 10 commodities by average modal price
-- SELECT
--     Commodity,
--     COUNT(*) AS record_count,
-- ROUND(AVG(Modal_Price), 2) AS avg_modal_price
-- FROM indian_agricultural_market_prices_cleaned
-- GROUP BY Commodity
-- HAVING COUNT(*) >= 5
-- ORDER BY avg_modal_price DESC
-- LIMIT 10;


-- Most widely available commodities
-- SELECT
--     Commodity,
--     COUNT(DISTINCT Market) AS market_count
-- FROM indian_agricultural_market_prices_cleaned
-- GROUP BY Commodity
-- ORDER BY market_count DESC
-- LIMIT 10;


-- Commodity price range
-- SELECT
--     Commodity,
--     ROUND(MIN(Modal_Price), 2) AS min_modal_price,
--     ROUND(MAX(Modal_Price), 2) AS max_modal_price,
--     ROUND(MAX(Modal_Price) - MIN(Modal_Price), 2) AS price_difference
-- FROM indian_agricultural_market_prices_cleaned
-- GROUP BY Commodity
-- HAVING COUNT(*) >= 5
-- ORDER BY price_difference DESC
-- LIMIT 10;
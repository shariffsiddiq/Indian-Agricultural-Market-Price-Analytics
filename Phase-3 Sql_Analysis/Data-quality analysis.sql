USE indian_agricultural_market_prices_cleaned;
-- 6.Data-quality analysis
-- Check invalid price relationships
-- SELECT COUNT(*) AS invalid_records
-- FROM indian_agricultural_market_prices_cleaned
-- WHERE Min_Price > Modal_Price
--    OR Modal_Price > Max_Price
--    OR Min_Price < 0
--    OR Modal_Price < 0
--    OR Max_Price < 0;


-- Find unusually low prices
-- SELECT
--     State,
--     Market,
--     Commodity,
--     Variety,
--     Min_Price,
--     Max_Price,
--     Modal_Price
-- FROM indian_agricultural_market_prices_cleaned
-- WHERE Modal_Price < 100
-- ORDER BY Modal_Price;


-- Find unusually high prices
-- SELECT
--     State,
--     Market,
--     Commodity,
--     Variety,
--     Min_Price,
--     Max_Price,
--     Modal_Price
-- FROM indian_agricultural_market_prices_cleaned
-- WHERE Modal_Price >= 50000
-- ORDER BY Modal_Price DESC;
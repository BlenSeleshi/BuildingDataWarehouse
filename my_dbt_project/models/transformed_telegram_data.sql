-- {{ config(materialized='table') }}

-- WITH filtered_messages AS (
--     SELECT 
--         -- Extracting product name
--         SUBSTRING(message, 1, NULLIF(POSITION(E'\n' IN message) - 1, -1)) AS product_name,
        
--         -- Extracting price
--         CAST(
--             TRIM(
--                 SUBSTRING(
--                     message, 
--                     POSITION('Price' IN message) + 6, 
--                     NULLIF(POSITION('birr' IN message) - POSITION('Price' IN message) - 6, -1)
--                 )
--             ) AS INTEGER
--         ) AS price,
        
--         -- Extracting first phone number
--         TRIM(
--             SUBSTRING(
--                 message, 
--                 POSITION('call' IN message) + 5, 
--                 NULLIF(POSITION('/' IN message) - POSITION('call' IN message) - 5, -1)
--             )
--         ) AS phone_number_1,
        
--         -- Extracting second phone number
--         TRIM(
--             SUBSTRING(
--                 message, 
--                 POSITION('/' IN message) + 1, 
--                 NULLIF(POSITION(E'\n' IN message) - (POSITION('/' IN message) + 1), -1)
--             )
--         ) AS phone_number_2,
        
--         -- Extracting store address
--         TRIM(
--             SUBSTRING(
--                 message, 
--                 POSITION('Adress' IN message) + 8,  
--                 NULLIF(POSITION(E'\n' IN message) - (POSITION('Adress' IN message) + 8), -1)
--             )
--         ) AS store_address
--     FROM {{ source('public', 'raw_data') }} 
--     WHERE channel_username = '@lobelia4cosmetics' 
--     -- Referring to your raw data source
-- )
-- SELECT * FROM filtered_messages


{{ config(materialized='table') }}

WITH filtered_messages AS (
    SELECT 
        -- Extracting product name
        message AS products
    FROM {{ source('public', 'raw_data') }} 
    WHERE channel_username = '@lobelia4cosmetics' 
    -- Referring to your raw data source
)
SELECT * FROM filtered_messages
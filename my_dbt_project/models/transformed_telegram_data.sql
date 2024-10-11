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

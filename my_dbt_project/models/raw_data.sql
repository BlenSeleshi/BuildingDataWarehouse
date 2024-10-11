
{{ config(materialized='table') }}

SELECT *
FROM public.raw_data

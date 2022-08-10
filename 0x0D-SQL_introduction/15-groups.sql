-- does an aggregation on table records
SELECT score, COUNT(*) AS number FROM second_table GROUP BY (score) ORDER BY number DESC;

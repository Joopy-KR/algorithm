SELECT F.FLAVOR
FROM FIRST_HALF F
  INNER JOIN JULY J
    ON F.FLAVOR = J.FLAVOR
GROUP BY F.FLAVOR
ORDER BY SUM(F.TOTAL_ORDER + J.TOTAL_ORDER) DESC
LIMIT 3;
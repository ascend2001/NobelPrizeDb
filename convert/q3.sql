-- Find the family names associated with five or more Nobel prizes (Answer: Smith, Wilson)

SELECT familyName 
FROM PersonName 
WHERE id IN (
    SELECT id 
    FROM NobelPrize
)
GROUP BY familyName 
HAVING count(*) > 4; 
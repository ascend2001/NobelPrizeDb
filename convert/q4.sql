-- How many different locations does the affiliation “University of California” have? Assume that a location is uniquely identified by its city and country. (Answer: 6)

SELECT COUNT(*)
FROM (
    SELECT city, country
    FROM Affiliations
    WHERE name = 'University of California'
    GROUP BY city, country
) AS UC;

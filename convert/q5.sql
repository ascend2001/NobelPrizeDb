-- In how many years was a Nobel prize awarded to an organization (as opposed to a person) in at least one category? (Answer: 26)


SELECT COUNT(DISTINCT awardYear) 
FROM NobelPrize 
WHERE id IN (
    SELECT id 
    FROM OrgName
);
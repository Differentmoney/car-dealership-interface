SELECT s.vin, s.SoldDate, s.SoldPrice, v.invoiceprice, s.SoldPrice/v.invoiceprice AS 'ratio', n.name AS Cname, CONCAT(u.FirstName, " ", U.LastName) AS Salesperson
from sellvehicle AS s, vehicle AS v, user as u,
(SELECT customerID, concat(i.firstname, ' ', i.lastname) AS 'name'
FROM individual AS i
UNION
SELECT customerID, businessname
FROM business) as n
WHERE s.vin = v.vin AND s.customerID = n.customerID AND s.Username = u.Username
ORDER BY s.SoldDate DESC, ratio DESC;
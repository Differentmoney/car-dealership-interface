SELECT C1.Name, SUM(Total) AS Gross, min(DT) as Oldest, max(DT) as newest, C1.CID
FROM (SELECT I.CustomerID AS CID, CONCAT(FirstName, ' ', LastName) Name
FROM Individual I, Customer C
WHERE I.CustomerID =C.CustomerID
UNION
SELECT B.CustomerID, BusinessName Name
FROM Business B, Customer C
WHERE B.CustomerID=C.CustomerID
) AS C1, 
-- Sum repair cost
(SELECT R.CustomerID AS CID, PC.Cost + R.LaborCharge AS Total, R.CompleteDate AS DT
FROM Repair AS R 
 INNER JOIN(
-- Sum part cost for each repair
SELECT R.Vin, R.StartDate, R.CustomerID, SUM(Quantity*Price) AS Cost
FROM Part P, Repair R, Customer C
WHERE P.Vin=R.Vin AND P.StartDate=R.StartDate AND C.CustomerID=R.CUstomerID
GROUP BY R.Vin, R.StartDate, R.CustomerID) AS PC
ON PC.Vin=R.Vin AND PC.StartDate=R.StartDate AND PC.CustomerID=R.CustomerID
UNION
SELECT CustomerID AS CID, SoldPrice AS Total, SoldDate AS DT
FROM SellVehicle AS S) AS Result
WHERE C1.CID=Result.CID AND DT IS NOT NULL
GROUP BY C1.Name, C1.CID
ORDER BY Gross DESC, newest DESC
LIMIT 15;

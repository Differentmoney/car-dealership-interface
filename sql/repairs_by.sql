SELECT ManufacturerName, IFNULL(CNT,0), IFNULL(PartC,0), IFNULL(LaborC,0), IFNULL(Total,0)
FROM Manufacturer AS M
LEFT JOIN (
SELECT ManufacturerID, Count(*) AS CNT, SUM(Price*Quantity) AS PartC, SUM(LaborCharge) AS LaborC, SUM(Price*Quantity + LaborCharge) AS Total
FROM Vehicle AS V 
INNER JOIN Repair AS R ON V.Vin=R.Vin
INNER JOIN Part AS P ON R.Vin=P.Vin AND R.CustomerID=P.CustomerID AND R.StartDate=P.StartDate
GROUP BY ManufacturerID) AS M1
ON M1.ManufacturerID=M.ManufacturerID
ORDER BY ManufacturerName ASC;
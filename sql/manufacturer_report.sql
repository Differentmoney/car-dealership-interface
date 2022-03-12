SELECT ManufacturerName, 
SUM(CASE 
WHEN DATEDIFF(SDate, s.soldDate)<=30 THEN 1
ELSE 0
END) month,
SUM(case
WHEN DATEDIFF(SDate, s.soldDate)<=365 THEN 1
ELSE 0
END) year,
COUNT(ManufacturerName) allTime
FROM SellVehicle s, Vehicle v, Manufacturer m, 
(SELECT MAX(soldDate) SDate
FROM SellVehicle) AS DT
WHERE s.Vin=v.Vin AND m.ManufacturerID=v.ManufacturerID
GROUP BY ManufacturerName
ORDER BY ManufacturerName ASC;

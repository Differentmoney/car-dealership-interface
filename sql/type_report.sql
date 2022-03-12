SELECT t.vehicleType, 
#Month
SUM(CASE
WHEN DATEDIFF(SDate,s.soldDate)<=30 THEN 1
ELSE 0
END) month,
#Year
SUM(case
WHEN DATEDIFF(SDate,s.soldDate)<=365 THEN 1
ELSE 0
END) year,
#AllTime
COUNT(t.vehicleType) allTime
FROM SellVehicle s, Vehicle v, VehicleType t, 
(SELECT MAX(soldDate) SDate
FROM sellVehicle) AS DT
WHERE s.Vin=v.Vin AND t.vehicleTypeNumber=v.vehicleTypeNumber
GROUP BY vehicleType
ORDER BY vehicleType;

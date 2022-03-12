SELECT T.VehicleType, IFNULL(IFNULL(AVG(DATEDIFF(s.soldDate, v.addDate) + 1), 0),'N/A') average 
FROM VehicleType T, Vehicle V, SellVehicle S
WHERE V.VehicleTypeNumber=T.VehicleTypeNumber AND V.Vin=S.Vin
GROUP BY T.VehicleType
ORDER BY T.VehicleType ASC;
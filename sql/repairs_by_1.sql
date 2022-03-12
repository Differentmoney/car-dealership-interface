SELECT vehicledetail, Count(*), SUM(Price * Quantity), SUM(LaborCharge), SUM(Price*Quantity + LaborCharge)
FROM Vehicle AS V 
INNER JOIN Repair AS R ON V.Vin=R.Vin
INNER JOIN Part AS P ON R.Vin=P.Vin AND R.CustomerID=P.CustomerID AND R.StartDate=P.StartDate
INNER JOIN Manufacturer AS M ON V.ManufacturerID = M.ManufacturerID 
INNER JOIN VehicleType AS VT ON V.vehicletypenumber = VT.vehicletypenumber
WHERE ManufacturerName = $Manufacturer
GROUP BY vehicletype
ORDER BY Count(*) DESC;

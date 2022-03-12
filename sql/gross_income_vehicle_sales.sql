#Vehicle Sales
SELECT soldDate, soldPrice, S.VIN, ModelYear, M.ManufacturerName, Model, CONCAT(U.FirstName,' ' ,U.LastName) name
FROM Vehicle V, SellVehicle S, User U, Manufacturer M
WHERE S.Username = U.Username AND V.Vin = S.Vin AND V.manufacturerID = M.manufacturerID AND S.CustomerID=$CustomerID 
ORDER BY soldDate DESC, VIN ASC; 


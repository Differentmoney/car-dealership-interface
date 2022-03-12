SELECT YEAR(SoldDate), MONTH(SoldDate), Count(SoldDate) AS TotalVehicleSold, SUM(SoldPrice) AS TotalSales, SUM(SoldPrice - InvoicePrice) AS TotalNet, AVG(SoldPrice/InvoicePrice) AS Ratio
FROM Vehicle AS V, SellVehicle AS S
WHERE V.VIN=S.VIN
GROUP BY YEAR(SoldDate), MONTH(SoldDate)
ORDER BY YEAR(SoldDate) DESC, MONTH(SoldDate) DESC
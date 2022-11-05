--
-- Pet, customer, invoice API.
-- Database: `core`
-- Prepared SQL queries for 'Customer' definition.
--


--
-- SELECT template for table `Customer`
--
SELECT `firstname`, `lastname`, `age`
FROM `core`.`Customer`
WHERE 1;

--
-- INSERT template for table `Customer`
--
INSERT INTO `core`.`Customer`(`firstname`, `lastname`, `age`)
VALUES (?, ?, ?);

--
-- UPDATE template for table `Customer`
--
UPDATE `core`.`Customer`
SET `firstname` = ?,
    `lastname`  = ?,
    `age`       = ?
WHERE 1;

--
-- DELETE template for table `Customer`
--
DELETE
FROM `core`.`Customer`
WHERE 0;

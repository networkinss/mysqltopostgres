--
-- Pet, customer, invoice API.
-- Database: `core`
-- Prepared SQL queries for 'Invoice' definition.
--


--
-- SELECT template for table `Invoice`
--
SELECT `product`, `amount`, `price`
FROM `core`.`Invoice`
WHERE 1;

--
-- INSERT template for table `Invoice`
--
INSERT INTO `core`.`Invoice`(`product`, `amount`, `price`)
VALUES (?, ?, ?);

--
-- UPDATE template for table `Invoice`
--
UPDATE `core`.`Invoice`
SET `product` = ?,
    `amount`  = ?,
    `price`   = ?
WHERE 1;

--
-- DELETE template for table `Invoice`
--
DELETE
FROM `core`.`Invoice`
WHERE 0;


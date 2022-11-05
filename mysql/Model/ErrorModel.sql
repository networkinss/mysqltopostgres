--
-- Pet, customer, invoice API.
-- Database: `core`
-- Prepared SQL queries for 'ErrorModel' definition.
--


--
-- SELECT template for table `ErrorModel`
--
SELECT `code`, `message`
FROM `core`.`ErrorModel`
WHERE 1;

--
-- INSERT template for table `ErrorModel`
--
INSERT INTO `core`.`ErrorModel`(`code`, `message`)
VALUES (?, ?);

--
-- UPDATE template for table `ErrorModel`
--
UPDATE `core`.`ErrorModel`
SET `code`    = ?,
    `message` = ?
WHERE 1;

--
-- DELETE template for table `ErrorModel`
--
DELETE
FROM `core`.`ErrorModel`
WHERE 0;


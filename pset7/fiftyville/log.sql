-- Keep a log of any SQL queries you execute as you solve the mystery.

-- 1. Get description from crime_scene_reports
SELECT description FROM crime_scene_reports
WHERE year = 2020 AND month = 7 AND day = 28 AND street = "Chamberlin Street";

-- 2. Get transcripts from interviewees who mentioned "courthouse"
SELECT name, transcript FROM intervies
WHERE year = 2020 AND month = 7 AND day = 28 AND transcript LIKE "%courthouse%";

-- 3. Get names of people who got into car within ten mins of the theft.
SELECT name FROM people
JOIN courthouse_security_logs ON people.license_plate = courthouse_security_logs.license_plate
WHERE year = 2020 AND month = 7 AND day = 28
AND hour = 10 AND minute >= 15 AND minute < 25 AND activity = "exit";

-- 4. Get names of people who withdrew money from atm at the FIfer st.
SELECT name FROM people
JOIN bank_accounts ON bank_accounts.person_id = people.id
JOIN atm_transactions ON atm_transactions.account_number = bank_accounts.account_number
WHERE year = 2020 AND month = 7 AND day = 28 AND atm_location = "Fifer Street"
AND transaction_type = "withdraw";

-- 5. Find earliest flight on 7/29.
SELECT id, destination_airport_id FROM flights
WHERE year = 2020 AND month = 7 AND day = 29 ORDER BY hour ASC;

-- 6. Find passengers' name with flight id.
SELECT name FROM people
JOIN passengers ON people.passport_number = passengers.passport_number
WHERE flight_id = 36;
-- >> The name "Ernest" is always in the list of results. So we can assume that the thief is "Ernest".

-- 7. Find out Ernest's phone number.
SELECT name FROM people
JOIN phone_calls ON people.phone_number = phone_calls.receiver
WHERE year = 2020 AND month = 7 AND day = 28 AND duration < 60 AND caller = (SELECT phone_number FROM people WHERE name = "Ernest");

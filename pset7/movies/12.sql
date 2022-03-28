SELECT movies.title FROM people
    JOIN stars ON people.id = stars.person_id
    JOIN movies ON stars.movie_id = movies.id
    WHERE people.name = "Johnny Depp"
INTERSECT
SELECT movies.title FROM people
    JOIN stars ON stars.person_id = people.id
    JOIN movies ON stars.movie_id = movies.id
    WHERE name = "Helena Bonham Carter"

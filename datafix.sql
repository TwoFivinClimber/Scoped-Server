UPDATE scoped_api_image
SET image = "https://res.cloudinary.com/twofiveclimb/image/upload/v1665604523/mad-app/le21h3jowmdjqcziylly.jpg"
WHERE id = 2

UPDATE scoped_api_user
SET name = "Wayne Brettski"
WHERE id = 9

DELETE FROM scoped_api_crew
WHERE id = 13

DELETE FROM scoped_api_employee
WHERE id = 10

UPDATE scoped_api_company
SET logo = "https://projectscoped.s3.us-east-2.amazonaws.com/Plantitas.png"
WHERE id = 2

UPDATE scoped_api_image
SET image = "https://res.cloudinary.com/twofiveclimb/image/upload/v1665604523/mad-app/le21h3jowmdjqcziylly.jpg"
WHERE id = 2

UPDATE scoped_api_crew
SET accepted = null
WHERE id = 1

DELETE FROM scoped_api_user
WHERE id = 8

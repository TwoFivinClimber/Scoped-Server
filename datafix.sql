UPDATE scoped_api_image
SET image = "https://res.cloudinary.com/twofiveclimb/image/upload/v1665604523/mad-app/le21h3jowmdjqcziylly.jpg"
WHERE id = 2

UPDATE scoped_api_job
SET datetime = "2023-04-23 22:00:00"
WHERE id = 19

UPDATE scoped_api_user
SET name = "Lesley Keyes"

INSERT into scoped_api_invite (id, company_id, uid_id)
VALUES (15, 2, 1)

DELETE FROM scoped_api_crew
WHERE id = 23

INSERT INTO scoped_api_crew (id, accepted, job_id, skill_id, uid_id)
VALUES (23, Null, 2, 2, 1)

INSERT INTO scoped_api_userskill (id, company_id, skill_id, user_id)
VALUES (41, 2, 2, 1)



UPDATE scoped_api_crew
SET accepted = 1
WHERE id = 21

DELETE FROM scoped_api_employee
WHERE id = 10

UPDATE scoped_api_company
SET logo = "https://projectscoped.s3.us-east-2.amazonaws.com/Plantitas.png"
WHERE id = 2

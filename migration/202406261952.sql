-- migrate:up

CREATE TABLE IF NOT EXISTS JobTitles
(
    JobTitle VARCHAR(255)
);

-- migrate:down
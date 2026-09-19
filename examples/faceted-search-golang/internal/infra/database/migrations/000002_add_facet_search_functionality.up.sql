-- Create search column
ALTER TABLE posts
ADD COLUMN search tsvector;
-- Create the function that updates the search column
CREATE OR REPLACE FUNCTION posts_search_trigger() RETURNS trigger AS $$ BEGIN NEW.search := setweight(
    to_tsvector('simple', COALESCE(NEW.title, '')),
    'A'
  ) || setweight(
    to_tsvector('simple', COALESCE(NEW.type, '')),
    'B'
  );
RETURN NEW;
END;
$$ LANGUAGE plpgsql;
-- Create the trigger that calls the function on insert or update
CREATE TRIGGER update_posts_search BEFORE
INSERT
  OR
UPDATE ON posts FOR EACH ROW EXECUTE PROCEDURE posts_search_trigger();
-- Create the index for the search column
CREATE INDEX IF NOT EXISTS post_weighted_idx ON posts USING gin (search);
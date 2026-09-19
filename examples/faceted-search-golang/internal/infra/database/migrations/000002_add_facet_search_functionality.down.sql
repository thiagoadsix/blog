-- Remove the index
DROP INDEX IF EXISTS post_weighted_idx;
-- Remove the trigger
DROP TRIGGER IF EXISTS update_posts_search ON posts;
-- Remove the function
DROP FUNCTION IF EXISTS posts_search_trigger;
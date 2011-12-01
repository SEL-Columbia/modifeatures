CREATE EXTENSION IF NOT EXISTS hstore;

DROP TABLE IF EXISTS features; 

-- Maybe we should follow the Geojson spec

CREATE TABLE features (
       id serial PRIMARY KEY,
       properties hstore
);

DROP INDEX IF EXISTS hidx;

CREATE INDEX hidx ON features USING btree (properties);

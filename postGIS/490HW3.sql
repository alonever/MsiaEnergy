-- MSIA 490 Homework Assignment 3
-- Qifan Wu

-- Q1: For each neighborhood, find the number of streets in the neighborhood. Specify your definition of 'in'.
-- WHENEVER A STREET APPEARS IN A NEIGHBORHOOD, IT IS COUNTED IN THE TOTAL NUMBER
SELECT nbhd.name AS neighborhood_name,
	count(str.*)
FROM nyc_neighborhoods AS nbhd
	JOIN nyc_streets AS str
	ON ST_Intersects(nbhd.geom, str.geom)
GROUP BY nbhd.name;

-- Q2: Find the number of subway stations in each block
SELECT blkid, count(sbw.*)
FROM nyc_census_blocks AS blk
	JOIN nyc_subway_stations AS sbw
	ON ST_Contains(blk.geom, sbw.geom)
GROUP BY blkid
ORDER BY count(sbw.*) DESC;

-- Q3: Find the block with the largest number of people with a college diploma (college diploma or graduate degree)
SELECT blkid, SUM(edu_college_dipl + edu_graduate_dipl)
FROM nyc_census_sociodata AS soc
	JOIN nyc_census_blocks AS blk 
	ON SubStr(blk.blkid, 1, 11) = soc.tractid
WHERE (soc.edu_college_dipl + soc.edu_graduate_dipl) = 
	(SELECT max(edu_college_dipl + edu_graduate_dipl) FROM nyc_census_sociodata)
GROUP BY blkid;

-- Q4: Find the subway station closest to the Manhattan borough (but not in the borough)
SELECT "name", sbw.borough, sbw.routes
FROM nyc_subway_stations AS sbw
WHERE sbw.borough != 'Manhattan'
ORDER BY ST_Distance(geom, 
	(SELECT ST_Union(geom)
	FROM nyc_neighborhoods
	WHERE boroname='Manhattan'))
LIMIT 1;

-- Q5: For each block, find all adjacent blocks
-- 35s query time, 267540 results
SELECT blk1.blkid AS BlockID, blk2.blkid AS AdjBlockID
FROM nyc_census_blocks AS blk1 JOIN nyc_census_blocks AS blk2
	ON ST_Touches(blk1.geom, blk2.geom);
-- QUICK INDEX WAY, BUT NOT ACURATE 
-- 6s query time, 329748 results
SELECT blk1.blkid AS BlockID, blk2.blkid AS AdjBlockID
FROM nyc_census_blocks AS blk1 JOIN nyc_census_blocks AS blk2
	ON blk1.geom && blk2.geom
WHERE blk1.blkid != blk2.blkid; 
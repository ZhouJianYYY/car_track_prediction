# 运行范围

# 日期,周末,早中晚


# Data Analysis
## Train: 1448321, 8
* Car:5819

## Test: 47493, 5 (5817=>5033)
* Car:5734 Overlap car with traing:5734
* Avg 1 car has 10 records

## TIPS
* time, week, Holiday
* How many time for long distance
* Similar calculation
* Compay,Home
* Speed, avg distance 
* Distance/ClusterNumber bin
* How many record over n times average
* Drop long weekend
* Each address arrive times, last time
* Group remaining address by long gap
* cal speed, then label the tracking type
* Len of the holiday
* Remain of the holiday 
* Reduce the start_zone far from the home and low frequency
* geohash to define the attribute of a zoneid
* Long distance times, 
* center#1 to center#2 distance
* group out_id(zoneid count, distance count)
* dynamic reduce address
* duration is usless
* Latest data has hight priority

* Continue reduce for car_id with multiply addressid
* Time avg distance
* Day avg distance
* Start_zoneid avg distance
* reduce to until only n address for one out_id
* Kmeans reduce address to diff group

* Reduce address by geohash

* Remove address by geohash

* zoneid category is small

* zoneid type base on hot position
* Cal poi to the center, and count the density
* Data enhance(Duplicate hot, fill missing data)
* latest data has high priority

# Classfy
* Top 10 multiple class:DC Tree
* Top 10 KNN



[LightGBM] [Warning] Accuracy may be bad since you didn't set num_leaves and 2^max_depth > num_leaves.


## 

## Install
* conda install basemap

home/code/result.csv


#TODO
pivot_table vs pivot


1) Remove low frequency data
2) Stable out_id with less type
3) Stable zoneid geo4
4) 



zoneid reduce step:
1) zoneid category type is small
2) break down geo7 already have many sample
3) 
4) Narrow down by geo*



* Remove usless geo4
* Recal center add
* cal centerid by geo4
* train model by big geoid
from code_felix.car.utils import *

@timed()
def cal_distance_gap_lat():
    train = pd.read_csv(train_file, delimiter=',', parse_dates=['start_time'])[:100]
    test = pd.read_csv(train_file, delimiter=',', parse_dates=['start_time'])[:200]

    df_list = [train[['out_id', 'start_lat', 'start_lon']],
               train[['out_id', 'end_lat', 'end_lon']],
               test[['out_id', 'start_lat', 'start_lon']],
               ]

    for df in df_list:
        df.columns = ['out_id', 'lat', 'lon']

    place_list = pd.concat(df_list)
    old_len = len(place_list)
    place_list = place_list.drop_duplicates()
    logger.debug(f"There are { old_len - len(place_list)} duplicates address drop from {old_len} records")

    place_list = place_list.sort_values(['out_id', 'lat', 'lon']).reset_index(drop=True)

    place_list['lat_2'] = place_list['lat'].shift(1)
    place_list['lon_2'] = place_list['lon'].shift(1)
    place_list['gap'] = np.abs(place_list['lat_2'] - place_list['lat']) + np.abs(
        place_list['lon_2'] - place_list['lon'])
    place_list['distance_gap'] = round(
        place_list.apply(lambda val: getDistance(val.lat_2, val.lon_2, val.lat, val.lon), axis=1))
    return place_list

@timed()
def cal_zoneid(place_list):
    distance_gap = 100
    place_list['zoneid']=None
    for index, item in place_list.iterrows():
        if index==0 or place_list.loc[index,'out_id'] != place_list.loc[index-1,'out_id']:
            place_list.loc[index,'zoneid']=0
        elif item.distance_gap <= distance_gap:
            place_list.loc[index,'zoneid']=place_list.loc[index-1,'zoneid']
        else:
            place_list.loc[index,'zoneid']=place_list.loc[index-1,'zoneid']+1

    return place_list

@timed()
def cal_center_of_zoneid(place_list):
    place_list[['center_lat', 'center_lon']] = place_list.groupby(['out_id','zoneid'])[['lat', 'lon']].transform('mean')

    place_list['distance_2_center'] = round(
        place_list.apply(lambda val: getDistance(val.center_lat, val.center_lon, val.lat, val.lon), axis=1))

    return place_list

@timed()
def cal_distance_gap_center_lon(place_list):

    place_list = place_list.sort_values(['out_id', 'center_lon', 'center_lat']).reset_index(drop=True)

    place_list['lat_3'] = place_list['center_lat'].shift(1)
    place_list['lon_3'] = place_list['center_lon'].shift(1)

    place_list['distance_gap'] = round(
        place_list.apply(lambda val: getDistance(val.lat_3, val.lon_3, val.center_lat, val.center_lon), axis=1))
    return place_list


@file_cache()
def reduce_address():
    distance_gap_lat = cal_distance_gap_lat()

    distance_zone_id_lat =  cal_zoneid(distance_gap_lat)

    center_lat = cal_center_of_zoneid(distance_zone_id_lat)

    distance_center = cal_distance_gap_center_lon(center_lat)

    distance_zone_id_lon = cal_zoneid(distance_center)

    distance_center = cal_distance_gap_center_lon(distance_zone_id_lon)

    return distance_center



if __name__ == '__main__':
    df = reduce_address()
    logger.debug(df.shape)
    addressid = df[['out_id', 'zoneid']].drop_duplicates()
    logger.debug(f"Only keep {len(addressid)} address")

import pyproj    
import shapely
import shapely.ops as ops
from shapely.geometry.polygon import Polygon
from functools import partial


terr_db = {}


def check_coords(coords_array):
	result = True
	for coords in coords_array:
		if not isinstance(coords[0], (int, float)) or not isinstance(coords[1], (int, float)):
			print(isinstance(coords[0], (int, float)))
			result = False
			break
	return result


def get_occurrence(field, district):
	field_id = field['id']
	distr_id = district['id']
	polig_field = terr_db[field_id]
	polig_distr = terr_db[distr_id]
	if polig_field.is_valid and polig_distr.is_valid:
		result = polig_field.intersection(polig_distr).area
	else:
		result = 0
	return result


def calc_main_alter(fields, districts):
	result = []
	create_polig_db(fields)
	create_polig_db(districts)
	for field in fields:
		in_field = {
			'field_id': field['id'],
			'districts': []
			}
		for district in districts:
			occurrence = get_occurrence(field, district)
			if occurrence != 0:
				in_district = {
					'district_id': district['id'],
					'occurrence': occurrence
				}
				in_field['districts'].append(in_district)
		if len(in_field['districts']) != 0:
			result.append(in_field)
	return result


def create_polig_db(territories):
	for territory in territories:
		name = territory['id']
		terr_db[name] = Polygon([(item[0], item[1]) for item in territory['coordinates'][0][0]])
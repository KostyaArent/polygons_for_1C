from shapely.geometry import Polygon
from area import area


def get_occurrence(field, district):
	field_coords = field['coordinates'][0][0]
	district_coords = field['coordinates'][0][0]
	return Polygon([(item[0], item[1]) for item in field_coords]).intersection(Polygon([(item[0],item[1]) for item in district_coords])).area


def calc_main(fields, districts):
	result = []
	for field in fields:
		result.append( 
			{ 
			'field_id': field['id'],
			'districts': [{'district_id': district['id'], 'occurrence': get_occurrence(field, district)} if get_occurrence(field, district) > 0 else None for district in districts]
			})
	return result
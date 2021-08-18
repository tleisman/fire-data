import pytest


@pytest.fixture
def mock_api_data():
    return {
        "type": "FeatureCollection",
        "name": "Greensboro_Fire_Incidents",
        "crs": {
            "type": "name",
            "properties": {"name": "urn:ogc:def:crs:OGC:1.3:CRS84"},
        },
        "features": [
            {
                "type": "Feature",
                "properties": {
                    "ID": 1,
                    "IncidentID": "_2Z005MWUT",
                    "IncidentNumber": "10-0701012",
                    "ExposureNumber": 0,
                    "Month": "07",
                    "MonthName": "July",
                    "Day": 1,
                    "DayOfWeek": "Thursday",
                    "Week": 27,
                    "Year": "2010",
                    "FiscalYear": "2010/2011",
                    "CallProcessingTime": "00:00:56",
                    "ResponseTime": "00:03:29",
                    "TotalResponseTime": "00:04:25",
                    "AlarmHour": 2,
                    "P911CenterReceived": "7/1/2010 2:21:20 AM",
                    "AlarmDate": "7/1/2010 2:22:16 AM",
                    "UnderControlTime": "7/1/2010 2:30:29 AM",
                    "IncidentClearTime": "7/1/2010 2:37:30 AM",
                    "FireDistrict": "Battalion II",
                    "station": "48",
                    "shift": "A",
                    "FireDemandZone": "3431",
                    "NumberOfAlarms": 1,
                    "NatureCode": "HEART",
                    "PropertyUse": "419 - 1 or 2 family dwelling",
                    "PropertyLoss": 0,
                    "ContentLoss": 0,
                    "TotalLosses": 0,
                    "PropertyValue": 0,
                    "ContentValue": 0,
                    "FireServiceFatalities": 0,
                    "FireServiceInjuries": 0,
                    "CivilianInjuries": 0,
                    "CivilianFatalities": 0,
                    "TotalStaffOnIncident": 4,
                    "TotalApparatus": 1,
                    "FlameSpreadDesc": "",
                    "ExtinguishedByDesc": "",
                    "ConditionsOnArrival": "",
                    "ExtinguishMethod": "",
                    "OccupancyStatus": "",
                    "AreaOfFireOrigin": "",
                    "HeatSource": "",
                    "NFIRS_IncidentGroup": "3-Rescue & Emergency Medical Service Incident",
                    "IncidentCategory": "31-Medical assist",
                    "NFIRS_IncidentType": "3111",
                    "NFIRS_IncidentTypeDescription": "3111-Medical Assist - Fire First",
                    "MutualAid": "None",
                    "geox": 1747390.3,
                    "geoy": 827303.63,
                    "Latitude": 36.020104,
                    "Longitude": -79.854213,
                    "AddressNumber": "3223",
                    "StreetPrefix": "",
                    "StreetName": "TWIN BROOKS",
                    "StreetType": "DR",
                    "StreetSuffix": "",
                    "FullAddress": "3223 TWIN BROOKS DR",
                },
                "geometry": None,
            },
            {
                "type": "Feature",
                "properties": {
                    "ID": 2,
                    "IncidentID": "_2Z00IMYSI",
                    "IncidentNumber": "10-0701035",
                    "ExposureNumber": 0,
                    "Month": "07",
                    "MonthName": "July",
                    "Day": 1,
                    "DayOfWeek": "Thursday",
                    "Week": 27,
                    "Year": "2010",
                    "FiscalYear": "2010/2011",
                    "CallProcessingTime": "00:00:12",
                    "ResponseTime": "00:03:26",
                    "TotalResponseTime": "00:03:38",
                    "AlarmHour": 8,
                    "P911CenterReceived": "7/1/2010 8:24:34 AM",
                    "AlarmDate": "7/1/2010 8:24:46 AM",
                    "UnderControlTime": "7/1/2010 8:31:13 AM",
                    "IncidentClearTime": "7/1/2010 8:40:59 AM",
                    "FireDistrict": "Battalion IV",
                    "station": "41",
                    "shift": "B",
                    "FireDemandZone": "1285",
                    "NumberOfAlarms": 1,
                    "NatureCode": "BREATH",
                    "PropertyUse": "962 - Residential street, road or residential driveway",
                    "PropertyLoss": 0,
                    "ContentLoss": 0,
                    "TotalLosses": 0,
                    "PropertyValue": 0,
                    "ContentValue": 0,
                    "FireServiceFatalities": 0,
                    "FireServiceInjuries": 0,
                    "CivilianInjuries": 0,
                    "CivilianFatalities": 0,
                    "TotalStaffOnIncident": 4,
                    "TotalApparatus": 1,
                    "FlameSpreadDesc": "",
                    "ExtinguishedByDesc": "",
                    "ConditionsOnArrival": "",
                    "ExtinguishMethod": "",
                    "OccupancyStatus": "",
                    "AreaOfFireOrigin": "",
                    "HeatSource": "",
                    "NFIRS_IncidentGroup": "3-Rescue & Emergency Medical Service Incident",
                    "IncidentCategory": "31-Medical assist",
                    "NFIRS_IncidentType": "3111",
                    "NFIRS_IncidentTypeDescription": "3111-Medical Assist - Fire First",
                    "MutualAid": "None",
                    "geox": 1755838.4,
                    "geoy": 877890.44,
                    "Latitude": 36.159257,
                    "Longitude": -79.827072,
                    "AddressNumber": "1700",
                    "StreetPrefix": "",
                    "StreetName": "TRIER",
                    "StreetType": "DR",
                    "StreetSuffix": "",
                    "FullAddress": "1700 TRIER DR",
                },
                "geometry": None,
            },
            {
                "type": "Feature",
                "properties": {
                    "ID": 3,
                    "IncidentID": "_2Z01E14A0",
                    "IncidentNumber": "10-0701109",
                    "ExposureNumber": 0,
                    "Month": "07",
                    "MonthName": "July",
                    "Day": 1,
                    "DayOfWeek": "Thursday",
                    "Week": 27,
                    "Year": "2010",
                    "FiscalYear": "2010/2011",
                    "CallProcessingTime": "00:00:09",
                    "ResponseTime": "00:02:31",
                    "TotalResponseTime": "00:02:40",
                    "AlarmHour": 23,
                    "P911CenterReceived": "7/1/2010 11:05:43 PM",
                    "AlarmDate": "7/1/2010 11:05:52 PM",
                    "UnderControlTime": "",
                    "IncidentClearTime": "7/1/2010 11:17:32 PM",
                    "FireDistrict": "Battalion I",
                    "station": "14",
                    "shift": "B",
                    "FireDemandZone": "2122",
                    "NumberOfAlarms": 1,
                    "NatureCode": "50PI",
                    "PropertyUse": "962 - Residential street, road or residential driveway",
                    "PropertyLoss": 0,
                    "ContentLoss": 0,
                    "TotalLosses": 0,
                    "PropertyValue": 0,
                    "ContentValue": 0,
                    "FireServiceFatalities": 0,
                    "FireServiceInjuries": 0,
                    "CivilianInjuries": 0,
                    "CivilianFatalities": 0,
                    "TotalStaffOnIncident": 4,
                    "TotalApparatus": 1,
                    "FlameSpreadDesc": "",
                    "ExtinguishedByDesc": "",
                    "ConditionsOnArrival": "",
                    "ExtinguishMethod": "",
                    "OccupancyStatus": "",
                    "AreaOfFireOrigin": "",
                    "HeatSource": "",
                    "NFIRS_IncidentGroup": "3-Rescue & Emergency Medical Service Incident",
                    "IncidentCategory": "32-Emergency medical service (EMS) Incident",
                    "NFIRS_IncidentType": "324",
                    "NFIRS_IncidentTypeDescription": "324-Motor Vehicle Accident with no injuries",
                    "MutualAid": "None",
                    "geox": 1777094.8,
                    "geoy": 867220.19,
                    "Latitude": 36.130413,
                    "Longitude": -79.754796,
                    "AddressNumber": "3719",
                    "StreetPrefix": "",
                    "StreetName": "MARTIN",
                    "StreetType": "AV",
                    "StreetSuffix": "",
                    "FullAddress": "3719 MARTIN AV",
                },
                "geometry": None,
            },
            {
                "type": "Feature",
                "properties": {
                    "ID": 4,
                    "IncidentID": "_2ZI1FFWUY",
                    "IncidentNumber": "10-0719045",
                    "ExposureNumber": 0,
                    "Month": "07",
                    "MonthName": "July",
                    "Day": 19,
                    "DayOfWeek": "Monday",
                    "Week": 30,
                    "Year": "2010",
                    "FiscalYear": "2010/2011",
                    "CallProcessingTime": "00:00:26",
                    "ResponseTime": "00:02:44",
                    "TotalResponseTime": "00:03:10",
                    "AlarmHour": 11,
                    "P911CenterReceived": "7/19/2010 11:35:12 AM",
                    "AlarmDate": "7/19/2010 11:35:38 AM",
                    "UnderControlTime": "",
                    "IncidentClearTime": "7/19/2010 11:49:33 AM",
                    "FireDistrict": "Battalion II",
                    "station": "08",
                    "shift": "B",
                    "FireDemandZone": "3257",
                    "NumberOfAlarms": 1,
                    "NatureCode": "UNCON",
                    "PropertyUse": "419 - 1 or 2 family dwelling",
                    "PropertyLoss": 0,
                    "ContentLoss": 0,
                    "TotalLosses": 0,
                    "PropertyValue": 0,
                    "ContentValue": 0,
                    "FireServiceFatalities": 0,
                    "FireServiceInjuries": 0,
                    "CivilianInjuries": 0,
                    "CivilianFatalities": 0,
                    "TotalStaffOnIncident": 4,
                    "TotalApparatus": 1,
                    "FlameSpreadDesc": "",
                    "ExtinguishedByDesc": "",
                    "ConditionsOnArrival": "",
                    "ExtinguishMethod": "",
                    "OccupancyStatus": "",
                    "AreaOfFireOrigin": "",
                    "HeatSource": "",
                    "NFIRS_IncidentGroup": "3-Rescue & Emergency Medical Service Incident",
                    "IncidentCategory": "31-Medical assist",
                    "NFIRS_IncidentType": "3111",
                    "NFIRS_IncidentTypeDescription": "3111-Medical Assist - Fire First",
                    "MutualAid": "None",
                    "geox": 1754668.0,
                    "geoy": 839458.5,
                    "Latitude": 36.053663,
                    "Longitude": -79.829948,
                    "AddressNumber": "2401",
                    "StreetPrefix": "",
                    "StreetName": "MAYWOOD",
                    "StreetType": "ST",
                    "StreetSuffix": "",
                    "FullAddress": "2401 MAYWOOD ST",
                },
                "geometry": None,
            },
            {
                "type": "Feature",
                "properties": {
                    "ID": 5,
                    "IncidentID": "_2Z91FF8MT",
                    "IncidentNumber": "10-0710043",
                    "ExposureNumber": 0,
                    "Month": "07",
                    "MonthName": "July",
                    "Day": 10,
                    "DayOfWeek": "Saturday",
                    "Week": 28,
                    "Year": "2010",
                    "FiscalYear": "2010/2011",
                    "CallProcessingTime": "00:00:07",
                    "ResponseTime": "00:03:49",
                    "TotalResponseTime": "00:03:56",
                    "AlarmHour": 16,
                    "P911CenterReceived": "7/10/2010 4:15:55 PM",
                    "AlarmDate": "7/10/2010 4:16:02 PM",
                    "UnderControlTime": "7/10/2010 4:25:28 PM",
                    "IncidentClearTime": "7/10/2010 4:31:45 PM",
                    "FireDistrict": "Battalion II",
                    "station": "48",
                    "shift": "B",
                    "FireDemandZone": "3460",
                    "NumberOfAlarms": 1,
                    "NatureCode": "HEART",
                    "PropertyUse": "419 - 1 or 2 family dwelling",
                    "PropertyLoss": 0,
                    "ContentLoss": 0,
                    "TotalLosses": 0,
                    "PropertyValue": 0,
                    "ContentValue": 0,
                    "FireServiceFatalities": 0,
                    "FireServiceInjuries": 0,
                    "CivilianInjuries": 0,
                    "CivilianFatalities": 0,
                    "TotalStaffOnIncident": 4,
                    "TotalApparatus": 1,
                    "FlameSpreadDesc": "",
                    "ExtinguishedByDesc": "",
                    "ConditionsOnArrival": "",
                    "ExtinguishMethod": "",
                    "OccupancyStatus": "",
                    "AreaOfFireOrigin": "",
                    "HeatSource": "",
                    "NFIRS_IncidentGroup": "3-Rescue & Emergency Medical Service Incident",
                    "IncidentCategory": "31-Medical assist",
                    "NFIRS_IncidentType": "3111",
                    "NFIRS_IncidentTypeDescription": "3111-Medical Assist - Fire First",
                    "MutualAid": "None",
                    "geox": 1759766.1,
                    "geoy": 822529.31,
                    "Latitude": 36.007275,
                    "Longitude": -79.812233,
                    "AddressNumber": "801",
                    "StreetPrefix": "",
                    "StreetName": "BANNER OAK",
                    "StreetType": "CT",
                    "StreetSuffix": "",
                    "FullAddress": "801 BANNER OAK CT",
                },
                "geometry": None,
            },
        ],
    }
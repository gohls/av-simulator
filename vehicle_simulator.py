#######################################################################
# Mapping API
# Author: Simon Gohl
# Date: 4/1/19
# Import References/Resources:
# https://bitbucket.org/team_24_swe/mapping_service_api/src/master/README.md
#######################################################################

import requests
import time
import unittest
from pprint import pprint

# global variable
base_url = 'https://team24.softwareengineeringii.com'


def autonomous_vehicle_command_menu():
    # Simple menu function
    print(bcolors.HEADER + "\nAutonomous-Vehicle Command Menu:" + bcolors.ENDC)
    print("     1. Start TaaS > An automated process whereby any outstanding orders are sequentially initiated")
    print("     2. Pending Orders > Prints a report of any outstanding orders")
    # print("     3. Get Vehicle Info > Prints the info of the selected vehicle")
    print("     3. Go Here > Send an autonomous vehicle anywhere with this command")
    print("     4. Exit")

    try:
        command = int(input(bcolors.OKGREEN + "\nEnter command: " + bcolors.ENDC))
    except ValueError:
        print()
        print(bcolors.FAIL + "That's not a number! - Try again" + bcolors.ENDC)
        autonomous_vehicle_command_menu()
    if command < 1 or command > 4:
        print()
        print(bcolors.FAIL + "Your number is to high or low! - Try again" + bcolors.ENDC)
        autonomous_vehicle_command_menu()

    return command


def set_a_dest():
    try:
        # Input is given as address NOT coordinates
        address = str(input(bcolors.OKGREEN + "Enter an address: " + bcolors.ENDC))
        data = {"destination": address}

        # print(data)
        # Get latitude and longitude coordinates on address
        url = f'{base_url}/mapping/address'
        resp = requests.get(url=url, json=data).json()

        # print("resp:", resp)
        addr_latitude = resp['latitude']
        addr_longitude = resp['longitude']

        # Reverse latitude and longitude, per Mapbox practices
        go_here = [addr_longitude, addr_latitude]

        return go_here

    except Exception as exp:
        print(bcolors.FAIL, exp, bcolors.ENDC)


def get_vehicle():
    vehicle_id = int(input(bcolors.OKGREEN + "Enter a vehicle #: " + bcolors.ENDC))

    return vehicle_id


def check_for_order():
    try:
        # api-endpoint
        url = f'{base_url}/supply/vehicle/available'
        # print(url)
        resp = requests.get(url=url)
        data = resp.json()
        # print(data)

        # Response from supply side will only give "available" vehicles
        # Iterate and filter the response of vehicle objects to only ones that have an order
        # An order is determined if Origin and Destination coordinates are different and are not None
        pending_orders_list = []
        for vehicle in data:
            if vehicle['destination_latitude'] is not None:
                if vehicle['current_latitude'] != vehicle['destination_latitude']:
                    if vehicle['current_longitude'] != vehicle['destination_longitude']:
                        pending_orders_list.append(vehicle)

        return pending_orders_list

    except Exception as exp:
        print(bcolors.FAIL, exp, bcolors.ENDC)


def print_pending_orders(pending_order_list):
    if pending_order_list is not None:
        for order in pending_order_list:
            print()
            print("Vehicle ID:", bcolors.OKBLUE, order['vehicle_id'], bcolors.ENDC)
            print("Coordinates       Latitude       Longitude")
            print("Current:\t", bcolors.OKBLUE, order['current_latitude'], "\t", order['current_longitude'], bcolors.ENDC)
            print("Destination:\t", bcolors.OKBLUE, order['destination_latitude'], "\t", order['destination_longitude'],
                   bcolors.ENDC)
    else:
        print(bcolors.FAIL + "Input parameter is None" + bcolors.FAIL)


def get_route(origin_lat, origin_long, dest_lat, dest_long):
    if origin_lat is not None and origin_long is not None and dest_lat is not None and dest_long is not None:
        try:
            # api-endpoint
            url = f'{base_url}/mapping/route'

            # use print(URL) to print full build url
            # print(url)

            coordinates = {"Origin latitude": origin_lat,
                           "Origin longitude": origin_long,
                           "Destination latitude": dest_lat,
                           "Destination longitude": dest_long}

            # print(requests.get(url=url, headers={'Content-Type': 'application/json'}, json=coordinates))
            # sending get request and saving the response as response object
            resp = requests.get(url=url, headers={'Content-Type': 'application/json'}, json=coordinates)

            # extracting data in json format
            data = resp.json()
            # print("Mapping data:", data)

            return data

        except Exception as exp:
            print(bcolors.FAIL, exp, bcolors.ENDC)

    else:
        print(bcolors.FAIL + "Input parameter is None" + bcolors.FAIL)


def parse_duration_into_list(data_JSON):
    if data_JSON is not None:
        # Parse out duration values and append into duration list
        duration_list = []
        for duration in data_JSON['steps']:
            duration_list.append(duration['duration'])

        # print("Duration list: ", duration_list)

        eta = data_JSON['eta']

        return duration_list, eta
    else:
        print(bcolors.FAIL + "Input parameter is None" + bcolors.FAIL)


def parse_lat_and_long_into_list(data_JSON):
    if data_JSON is not None:
        # Parse out the coordinate values and append into coordinates list
        coordinates_list = []
        for coordinates in data_JSON['steps']:
            lat_and_long_list = [coordinates['latitude'], coordinates['longitude']]
            coordinates_list.append(lat_and_long_list)

        # print("Steps coor. list:", coordinates_list)

        return coordinates_list
    else:
        print(bcolors.FAIL + "Input parameter is None" + bcolors.FAIL)


def simulate_instance(d_list, c_list, vehicle, dest_eta):
    if d_list is not None and c_list is not None and vehicle is not None and dest_eta is not None:
        # Step through the duration and coordinates lists
        # Sleep for the defined time of each duration in the duration list
        # While stepping to the next coordinate
        i = 0
        while d_list[i] != 0:
            print()
            print('In Route:', bcolors.OKBLUE, 'Vehicle', vehicle, bcolors.ENDC)
            print('Current Veh. Coor.:', bcolors.OKBLUE, c_list[i], bcolors.ENDC)
            print('Next Step ETA:', bcolors.OKBLUE, format(d_list[i], '.0f'), "seconds", bcolors.ENDC)
            dest_eta = dest_eta - (d_list[i] / 60)
            print('Destination ETA:', bcolors.OKBLUE, format(dest_eta, '.0f'), "minutes", bcolors.ENDC)
            update_vehicle_coordinates(c_list[i], vehicle, "In route")
            time.sleep(d_list[i])
            i += 1

        print()
        print('Route Concluded:', bcolors.OKBLUE, 'Vehicle', vehicle, bcolors.ENDC)
        print('Final Veh. Coor.:', c_list[i])
        print('Status set to available')
        update_vehicle_coordinates(c_list[i], vehicle, "available")
    else:
        print(bcolors.FAIL + "Input parameter is None" + bcolors.FAIL)


def update_vehicle_coordinates(c_list, vehicle, status):
    if c_list is not None and vehicle is not None and status is not None:
        # api-endpoint
        url = f'{base_url}/supply/vehicle/update'

        lat = c_list[1]
        long = c_list[0]

        update = {"vehicle_id": vehicle,
                  "latitude": lat,
                  "longitude": long,
                  "status": status
                  }
        try:
            requests.post(url=url, headers={'Content-Type': 'application/json'}, json=update)
        except Exception as exp:
            print(bcolors.FAIL, exp, bcolors.ENDC)
    else:
        print(bcolors.FAIL + "Input parameter is None" + bcolors.FAIL)


def start_TaaS(data):
    if data is not None:
        for order in data:
            # data contains vehicle objects as listed below
            vehicle_id = order['vehicle_id']
            status = order['status']
            origin_lat = order['current_latitude']
            origin_long = order['current_longitude']
            dest_lat = order['destination_latitude']
            dest_long = order['destination_longitude']

            # Make a request to mapping API
            # rv = eta: total, steps: duration, latitude, longitude for each step
            duration_and_steps_JSON = get_route(origin_lat, origin_long, dest_lat, dest_long)

            # pprint(duration_and_steps_JSON)
            # Parse out the duration from each step and put into duration list
            duration_list, dest_eta = parse_duration_into_list(duration_and_steps_JSON)

            # Parse out the latitude and longitude of each step and put into coordinates list
            coordinates_list = parse_lat_and_long_into_list(duration_and_steps_JSON)

            # Simulate the instance with the given durations and coordinates increments
            simulate_instance(duration_list, coordinates_list, vehicle_id, dest_eta)
    else:
        print(bcolors.FAIL + "Input parameter is None" + bcolors.FAIL)


def vSim():
    # Manual input from user/operator on vehicle actuators
    command = autonomous_vehicle_command_menu()

    # Exit command == 4
    while command != 4:
        if command == 1:
            pending_order_list = check_for_order()
            if not pending_order_list:
                print("There are no pending orders")
            else:
                start_TaaS(pending_order_list)
        elif command == 2:
            pending_order_list = check_for_order()
            if not pending_order_list:
                print("There are no pending orders")
            else:
                print_pending_orders(pending_order_list)
        # elif command == 3:
        #         get_vehicle()
        elif command == 3:
            go_here = set_a_dest()
            if not go_here:
                print("Something went wrong")
            else:
                vehicle_id = get_vehicle()
                update_vehicle_coordinates(go_here, vehicle_id, "available")

        command = autonomous_vehicle_command_menu()

# Just some color to the terminal for fun!!!!
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

    def disable(self):
        self.HEADER = ''
        self.OKBLUE = ''
        self.OKGREEN = ''
        self.WARNING = ''
        self.FAIL = ''
        self.ENDC = ''


if __name__ == '__main__':
    vSim()

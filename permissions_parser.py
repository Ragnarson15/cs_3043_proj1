import csv
import operator
import json

data = []


#-------------------------------------------------------------------------------

def main():

        permissions_data = {}
        permissions_data['name'] = 'Permissions'
        permissions_data['children'] = get_permissions()
        data.append(permissions_data)

        with open('data.json', 'w') as fp:
            json.dump(data, fp, sort_keys=False, indent=4)


#-------------------------------------------------------------------------------


def get_permissions():

        permissions = []

        needed_permissions = {}
        needed_permissions['name'] = 'Needed Permissions'
        needed_permissions['children'] = get_needed_children()
        permissions.append(needed_permissions)

        wanted_permissions = {}
        wanted_permissions['name'] = 'Wanted Permissions'
        wanted_permissions['children'] = get_wanted_children()
        permissions.append(wanted_permissions)

        no_permissions = {}
        no_permissions['name'] = 'Permissions Not Required'
        no_permissions['children'] = get_no_children()
        permissions.append(no_permissions)

        return permissions


#-------------------------------------------------------------------------------


def get_needed_children():

    needed_children = []

    temp = {}
    temp['name'] = 'Calender'
    temp['children'] = get_cal_need_children()
    needed_children.append(temp)

    temp = {}
    temp['name'] = 'Camera'
    temp['children'] = get_cam_need_children()
    needed_children.append(temp)

    temp = {}
    temp['name'] = 'Contacts'
    temp['children'] = get_con_need_children()
    needed_children.append(temp)

    temp = {}
    temp['name'] = 'Location'
    temp['children'] = get_loc_need_children()
    needed_children.append(temp)

    temp = {}
    temp['name'] = 'Microphone'
    temp['children'] = get_mic_need_children()
    needed_children.append(temp)

    temp = {}
    temp['name'] = 'SMS'
    temp['children'] = get_sms_need_children()
    needed_children.append(temp)

    temp = {}
    temp['name'] = 'Storage'
    temp['children'] = get_sto_need_children()
    needed_children.append(temp)

    temp = {}
    temp['name'] = 'Phone'
    temp['children'] = get_pho_need_children()
    needed_children.append(temp)

    return needed_children


def get_wanted_children():

    wanted_children = []

    temp = {}
    temp['name'] = 'Calender'
    temp['children'] = get_cal_want_children()
    wanted_children.append(temp)

    temp = {}
    temp['name'] = 'Camera'
    temp['children'] = get_cam_want_children()
    wanted_children.append(temp)

    temp = {}
    temp['name'] = 'Contacts'
    temp['children'] = get_con_want_children()
    wanted_children.append(temp)

    temp = {}
    temp['name'] = 'Location'
    temp['children'] = get_loc_want_children()
    wanted_children.append(temp)

    temp = {}
    temp['name'] = 'Microphone'
    temp['children'] = get_mic_want_children()
    wanted_children.append(temp)

    temp = {}
    temp['name'] = 'SMS'
    temp['children'] = get_sms_want_children()
    wanted_children.append(temp)

    temp = {}
    temp['name'] = 'Storage'
    temp['children'] = get_sto_want_children()
    wanted_children.append(temp)

    temp = {}
    temp['name'] = 'Phone'
    temp['children'] = get_pho_want_children()
    wanted_children.append(temp)

    return wanted_children


def get_no_children():

    no_children = []

    temp = {}
    temp['name'] = 'Calender'
    temp['children'] = get_cal_no_children()
    no_children.append(temp)

    temp = {}
    temp['name'] = 'Camera'
    temp['children'] = get_cam_no_children()
    no_children.append(temp)

    temp = {}
    temp['name'] = 'Contacts'
    temp['children'] = get_con_no_children()
    no_children.append(temp)

    temp = {}
    temp['name'] = 'Location'
    temp['children'] = get_loc_no_children()
    no_children.append(temp)

    temp = {}
    temp['name'] = 'Microphone'
    temp['children'] = get_mic_no_children()
    no_children.append(temp)

    temp = {}
    temp['name'] = 'SMS'
    temp['children'] = get_sms_no_children()
    no_children.append(temp)

    temp = {}
    temp['name'] = 'Storage'
    temp['children'] = get_sto_no_children()
    no_children.append(temp)

    temp = {}
    temp['name'] = 'Phone'
    temp['children'] = get_pho_no_children()
    no_children.append(temp)

    return no_children


#-------------------------------------------------------------------------------


def get_cal_need_children():

    needed_children = []

    with open('permissions.csv', 'rb') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:

            temp_child = {}
            if (row[4] == 'n'):
                temp_child['name'] = row[2]
                needed_children.append(temp_child)

    return needed_children


def get_cam_need_children():

    needed_children = []

    with open('permissions.csv', 'rb') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:

            temp_child = {}
            if (row[5] == 'n'):
                temp_child['name'] = row[2]
                needed_children.append(temp_child)

    return needed_children


def get_con_need_children():

    needed_children = []

    with open('permissions.csv', 'rb') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:

            temp_child = {}
            if (row[6] == 'n'):
                temp_child['name'] = row[2]
                needed_children.append(temp_child)

    return needed_children


def get_loc_need_children():

    needed_children = []

    with open('permissions.csv', 'rb') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:

            temp_child = {}
            if (row[7] == 'n'):
                temp_child['name'] = row[2]
                needed_children.append(temp_child)

    return needed_children


def get_mic_need_children():

    needed_children = []

    with open('permissions.csv', 'rb') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:

            temp_child = {}
            if (row[8] == 'n'):
                temp_child['name'] = row[2]
                needed_children.append(temp_child)

    return needed_children


def get_sms_need_children():

    needed_children = []

    with open('permissions.csv', 'rb') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:

            temp_child = {}
            if (row[9] == 'n'):
                temp_child['name'] = row[2]
                needed_children.append(temp_child)

    return needed_children


def get_sto_need_children():

    needed_children = []

    with open('permissions.csv', 'rb') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:

            temp_child = {}
            if (row[10] == 'n'):
                temp_child['name'] = row[2]
                needed_children.append(temp_child)

    return needed_children


def get_pho_need_children():

    needed_children = []

    with open('permissions.csv', 'rb') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:

            temp_child = {}
            if (row[11] == 'n'):
                temp_child['name'] = row[2]
                needed_children.append(temp_child)

    return needed_children


#-------------------------------------------------------------------------------


def get_cal_want_children():

    wanted_children = []

    with open('permissions.csv', 'rb') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:

            temp_child = {}
            if (row[4] == 'w'):
                temp_child['name'] = row[2]
                wanted_children.append(temp_child)

    return wanted_children


def get_cam_want_children():

    wanted_children = []

    with open('permissions.csv', 'rb') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:

            temp_child = {}
            if (row[5] == 'w'):
                temp_child['name'] = row[2]
                wanted_children.append(temp_child)

    return wanted_children


def get_con_want_children():

    wanted_children = []

    with open('permissions.csv', 'rb') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:

            temp_child = {}
            if (row[6] == 'w'):
                temp_child['name'] = row[2]
                wanted_children.append(temp_child)

    return wanted_children


def get_loc_want_children():

    wanted_children = []

    with open('permissions.csv', 'rb') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:

            temp_child = {}
            if (row[7] == 'w'):
                temp_child['name'] = row[2]
                wanted_children.append(temp_child)

    return wanted_children


def get_mic_want_children():

    wanted_children = []

    with open('permissions.csv', 'rb') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:

            temp_child = {}
            if (row[8] == 'w'):
                temp_child['name'] = row[2]
                wanted_children.append(temp_child)

    return wanted_children


def get_sms_want_children():

    wanted_children = []

    with open('permissions.csv', 'rb') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:

            temp_child = {}
            if (row[9] == 'w'):
                temp_child['name'] = row[2]
                wanted_children.append(temp_child)

    return wanted_children


def get_sto_want_children():

    wanted_children = []

    with open('permissions.csv', 'rb') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:

            temp_child = {}
            if (row[10] == 'w'):
                temp_child['name'] = row[2]
                wanted_children.append(temp_child)

    return wanted_children


def get_pho_want_children():

    wanted_children = []

    with open('permissions.csv', 'rb') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:

            temp_child = {}
            if (row[11] == 'w'):
                temp_child['name'] = row[2]
                wanted_children.append(temp_child)

    return wanted_children


#-------------------------------------------------------------------------------


def get_cal_no_children():

    no_children = []

    with open('permissions.csv', 'rb') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:

            temp_child = {}
            if (row[4] == 'e'):
                temp_child['name'] = row[2]
                no_children.append(temp_child)

    return no_children


def get_cam_no_children():

    no_children = []

    with open('permissions.csv', 'rb') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:

            temp_child = {}
            if (row[5] == 'e'):
                temp_child['name'] = row[2]
                no_children.append(temp_child)

    return no_children


def get_con_no_children():

    no_children = []

    with open('permissions.csv', 'rb') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:

            temp_child = {}
            if (row[6] == 'e'):
                temp_child['name'] = row[2]
                no_children.append(temp_child)

    return no_children


def get_loc_no_children():

    no_children = []

    with open('permissions.csv', 'rb') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:

            temp_child = {}
            if (row[7] == 'e'):
                temp_child['name'] = row[2]
                no_children.append(temp_child)

    return no_children


def get_mic_no_children():

    no_children = []

    with open('permissions.csv', 'rb') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:

            temp_child = {}
            if (row[8] == 'e'):
                temp_child['name'] = row[2]
                no_children.append(temp_child)

    return no_children


def get_sms_no_children():

    no_children = []

    with open('permissions.csv', 'rb') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:

            temp_child = {}
            if (row[9] == 'e'):
                temp_child['name'] = row[2]
                no_children.append(temp_child)

    return no_children


def get_sto_no_children():

    no_children = []

    with open('permissions.csv', 'rb') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:

            temp_child = {}
            if (row[10] == 'e'):
                temp_child['name'] = row[2]
                no_children.append(temp_child)

    return no_children


def get_pho_no_children():

    no_children = []

    with open('permissions.csv', 'rb') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:

            temp_child = {}
            if (row[11] == 'e'):
                temp_child['name'] = row[2]
                no_children.append(temp_child)

    return no_children


#-------------------------------------------------------------------------------


if __name__ == '__main__':
    main()

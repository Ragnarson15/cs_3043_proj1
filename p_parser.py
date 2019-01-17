import csv
import operator
import json

data = []


#-------------------------------------------------------------------------------

def main():

        permissions_data = {}
        permissions_data['id'] = 1
        permissions_data['name'] = 'Permissions'
        data.append(permissions_data)
        get_permissions()

        with open('data.json', 'w') as fp:
            json.dump(data, fp, sort_keys=False, indent=4)


#-------------------------------------------------------------------------------


def get_permissions():

        permissions = []

        needed_permissions = {}
        needed_permissions['id'] = 2
        needed_permissions['name'] = 'Needed Permissions'
        needed_permissions['parent'] = 1
        data.append(needed_permissions)

        wanted_permissions = {}
        wanted_permissions['id'] = 3
        wanted_permissions['name'] = 'Wanted Permissions'
        wanted_permissions['parent'] = 1
        data.append(wanted_permissions)

        no_permissions = {}
        no_permissions['id'] = 4
        no_permissions['name'] = 'Permissions Not Required'
        no_permissions['parent'] = 1
        data.append(no_permissions)

        node_id = get_needed_children(5, 2)
        node_id = get_wanted_children(node_id + 1, 3)
        node_id = get_no_children(node_id + 1, 4)

        node_id = get_cal_need_children(node_id, 5)
        node_id = get_cam_need_children(node_id, 6)
        node_id = get_con_need_children(node_id, 7)
        node_id = get_loc_need_children(node_id, 8)
        node_id = get_mic_need_children(node_id, 9)
        node_id = get_sms_need_children(node_id, 10)
        node_id = get_sto_need_children(node_id, 11)
        node_id = get_pho_need_children(node_id, 12)

        node_id = get_cal_want_children(node_id + 1, 13)
        node_id = get_cam_want_children(node_id + 1, 14)
        node_id = get_con_want_children(node_id + 1, 15)
        node_id = get_loc_want_children(node_id + 1, 16)
        node_id = get_mic_want_children(node_id + 1, 17)
        node_id = get_sms_want_children(node_id + 1, 18)
        node_id = get_sto_want_children(node_id + 1, 19)
        node_id = get_pho_want_children(node_id + 1, 20)

        node_id = get_cal_no_children(node_id + 1, 21)
        node_id = get_cam_no_children(node_id + 1, 22)
        node_id = get_con_no_children(node_id + 1, 23)
        node_id = get_loc_no_children(node_id + 1, 24)
        node_id = get_mic_no_children(node_id + 1, 25)
        node_id = get_sms_no_children(node_id + 1, 26)
        node_id = get_sto_no_children(node_id + 1, 27)
        get_pho_no_children(node_id + 1, 28)


#-------------------------------------------------------------------------------


def get_needed_children(node_id, parent_id):

    temp = {}
    temp['id'] = node_id
    temp['name'] = 'Calender'
    temp['parent'] = parent_id
    data.append(temp)

    temp = {}
    node_id += 1
    temp['id'] = node_id
    temp['name'] = 'Camera'
    temp['parent'] = parent_id
    data.append(temp)

    temp = {}
    node_id += 1
    temp['id'] = node_id
    temp['name'] = 'Contacts'
    temp['parent'] = parent_id
    data.append(temp)

    temp = {}
    node_id += 1
    temp['id'] = node_id
    temp['name'] = 'Location'
    temp['parent'] = parent_id
    data.append(temp)

    temp = {}
    node_id += 1
    temp['id'] = node_id
    temp['name'] = 'Microphone'
    temp['parent'] = parent_id
    data.append(temp)

    temp = {}
    node_id += 1
    temp['id'] = node_id
    temp['name'] = 'SMS'
    temp['parent'] = parent_id
    data.append(temp)

    temp = {}
    node_id += 1
    temp['id'] = node_id
    temp['name'] = 'Storage'
    temp['parent'] = parent_id
    data.append(temp)

    temp = {}
    node_id += 1
    temp['id'] = node_id
    temp['name'] = 'Phone'
    temp['parent'] = parent_id
    data.append(temp)

    return node_id


def get_wanted_children(node_id, parent_id):

    temp = {}
    temp['id'] = node_id
    temp['name'] = 'Calender'
    temp['parent'] = parent_id
    data.append(temp)

    temp = {}
    node_id += 1
    temp['id'] = node_id
    temp['name'] = 'Camera'
    temp['parent'] = parent_id
    data.append(temp)

    temp = {}
    node_id += 1
    temp['id'] = node_id
    temp['name'] = 'Contacts'
    temp['parent'] = parent_id
    data.append(temp)

    temp = {}
    node_id += 1
    temp['id'] = node_id
    temp['name'] = 'Location'
    temp['parent'] = parent_id
    data.append(temp)

    temp = {}
    node_id += 1
    temp['id'] = node_id
    temp['name'] = 'Microphone'
    temp['parent'] = parent_id
    data.append(temp)

    temp = {}
    node_id += 1
    temp['id'] = node_id
    temp['name'] = 'SMS'
    temp['parent'] = parent_id
    data.append(temp)

    temp = {}
    node_id += 1
    temp['id'] = node_id
    temp['name'] = 'Storage'
    temp['parent'] = parent_id
    data.append(temp)

    temp = {}
    node_id += 1
    temp['id'] = node_id
    temp['name'] = 'Phone'
    temp['parent'] = parent_id
    data.append(temp)

    return node_id


def get_no_children(node_id, parent_id):

    temp = {}
    temp['id'] = node_id
    temp['name'] = 'Calender'
    temp['parent'] = parent_id
    data.append(temp)

    temp = {}
    node_id += 1
    temp['id'] = node_id
    temp['name'] = 'Camera'
    temp['parent'] = parent_id
    data.append(temp)

    temp = {}
    node_id += 1
    temp['id'] = node_id
    temp['name'] = 'Contacts'
    temp['parent'] = parent_id
    data.append(temp)

    temp = {}
    node_id += 1
    temp['id'] = node_id
    temp['name'] = 'Location'
    temp['parent'] = parent_id
    data.append(temp)

    temp = {}
    node_id += 1
    temp['id'] = node_id
    temp['name'] = 'Microphone'
    temp['parent'] = parent_id
    data.append(temp)

    temp = {}
    node_id += 1
    temp['id'] = node_id
    temp['name'] = 'SMS'
    temp['parent'] = parent_id
    data.append(temp)

    temp = {}
    node_id += 1
    temp['id'] = node_id
    temp['name'] = 'Storage'
    temp['parent'] = parent_id
    data.append(temp)

    temp = {}
    node_id += 1
    temp['id'] = node_id
    temp['name'] = 'Phone'
    temp['parent'] = parent_id
    data.append(temp)

    return node_id


#-------------------------------------------------------------------------------


def get_cal_need_children(node_id, parent_id):

    with open('permissions.csv', 'rb') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:

            temp_child = {}
            if (row[4] == 'n'):
                node_id += 1
                temp_child['id'] = node_id
                temp_child['name'] = row[2]
                temp_child['parent'] = parent_id
                data.append(temp_child)

    return node_id


def get_cam_need_children(node_id, parent_id):

    with open('permissions.csv', 'rb') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:

            temp_child = {}
            if (row[5] == 'n'):
                node_id += 1
                temp_child['id'] = node_id
                temp_child['name'] = row[2]
                temp_child['parent'] = parent_id
                data.append(temp_child)

    return node_id


def get_con_need_children(node_id, parent_id):

    with open('permissions.csv', 'rb') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:

            temp_child = {}
            if (row[6] == 'n'):
                node_id += 1
                temp_child['id'] = node_id
                temp_child['name'] = row[2]
                temp_child['parent'] = parent_id
                data.append(temp_child)

    return node_id


def get_loc_need_children(node_id, parent_id):

    with open('permissions.csv', 'rb') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:

            temp_child = {}
            if (row[7] == 'n'):
                node_id += 1
                temp_child['id'] = node_id
                temp_child['name'] = row[2]
                temp_child['parent'] = parent_id
                data.append(temp_child)

    return node_id


def get_mic_need_children(node_id, parent_id):

    with open('permissions.csv', 'rb') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:

            temp_child = {}
            if (row[8] == 'n'):
                node_id += 1
                temp_child['id'] = node_id
                temp_child['name'] = row[2]
                temp_child['parent'] = parent_id
                data.append(temp_child)

    return node_id


def get_sms_need_children(node_id, parent_id):

    with open('permissions.csv', 'rb') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:

            temp_child = {}
            if (row[9] == 'n'):
                node_id += 1
                temp_child['id'] = node_id
                temp_child['name'] = row[2]
                temp_child['parent'] = parent_id
                data.append(temp_child)

    return node_id


def get_sto_need_children(node_id, parent_id):

    with open('permissions.csv', 'rb') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:

            temp_child = {}
            if (row[10] == 'n'):
                node_id += 1
                temp_child['id'] = node_id
                temp_child['name'] = row[2]
                temp_child['parent'] = parent_id
                data.append(temp_child)

    return node_id


def get_pho_need_children(node_id, parent_id):

    with open('permissions.csv', 'rb') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:

            temp_child = {}
            if (row[11] == 'n'):
                node_id += 1
                temp_child['id'] = node_id
                temp_child['name'] = row[2]
                temp_child['parent'] = parent_id
                data.append(temp_child)

    return node_id


#-------------------------------------------------------------------------------


def get_cal_want_children(node_id, parent_id):

    with open('permissions.csv', 'rb') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:

            temp_child = {}
            if (row[4] == 'w'):
                node_id += 1
                temp_child['id'] = node_id
                temp_child['name'] = row[2]
                temp_child['parent'] = parent_id
                data.append(temp_child)

    return node_id


def get_cam_want_children(node_id, parent_id):

    with open('permissions.csv', 'rb') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:

            temp_child = {}
            if (row[5] == 'w'):
                node_id += 1
                temp_child['id'] = node_id
                temp_child['name'] = row[2]
                temp_child['parent'] = parent_id
                data.append(temp_child)

    return node_id


def get_con_want_children(node_id, parent_id):

    with open('permissions.csv', 'rb') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:

            temp_child = {}
            if (row[6] == 'w'):
                node_id += 1
                temp_child['id'] = node_id
                temp_child['name'] = row[2]
                temp_child['parent'] = parent_id
                data.append(temp_child)

    return node_id


def get_loc_want_children(node_id, parent_id):

    with open('permissions.csv', 'rb') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:

            temp_child = {}
            if (row[7] == 'w'):
                node_id += 1
                temp_child['id'] = node_id
                temp_child['name'] = row[2]
                temp_child['parent'] = parent_id
                data.append(temp_child)

    return node_id


def get_mic_want_children(node_id, parent_id):

    with open('permissions.csv', 'rb') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:

            temp_child = {}
            if (row[8] == 'w'):
                node_id += 1
                temp_child['id'] = node_id
                temp_child['name'] = row[2]
                temp_child['parent'] = parent_id
                data.append(temp_child)

    return node_id


def get_sms_want_children(node_id, parent_id):

    with open('permissions.csv', 'rb') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:

            temp_child = {}
            if (row[9] == 'w'):
                node_id += 1
                temp_child['id'] = node_id
                temp_child['name'] = row[2]
                temp_child['parent'] = parent_id
                data.append(temp_child)

    return node_id


def get_sto_want_children(node_id, parent_id):

    with open('permissions.csv', 'rb') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:

            temp_child = {}
            if (row[10] == 'w'):
                node_id += 1
                temp_child['id'] = node_id
                temp_child['name'] = row[2]
                temp_child['parent'] = parent_id
                data.append(temp_child)

    return node_id


def get_pho_want_children(node_id, parent_id):

    with open('permissions.csv', 'rb') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:

            temp_child = {}
            if (row[11] == 'w'):
                node_id += 1
                temp_child['id'] = node_id
                temp_child['name'] = row[2]
                temp_child['parent'] = parent_id
                data.append(temp_child)

    return node_id


#-------------------------------------------------------------------------------


def get_cal_no_children(node_id, parent_id):

    with open('permissions.csv', 'rb') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:

            temp_child = {}
            if (row[4] == 'e'):
                node_id += 1
                temp_child['id'] = node_id
                temp_child['name'] = row[2]
                temp_child['parent'] = parent_id
                data.append(temp_child)

    return node_id


def get_cam_no_children(node_id, parent_id):

    with open('permissions.csv', 'rb') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:

            temp_child = {}
            if (row[5] == 'e'):
                node_id += 1
                temp_child['id'] = node_id
                temp_child['name'] = row[2]
                temp_child['parent'] = parent_id
                data.append(temp_child)

    return node_id


def get_con_no_children(node_id, parent_id):

    with open('permissions.csv', 'rb') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:

            temp_child = {}
            if (row[6] == 'e'):
                node_id += 1
                temp_child['id'] = node_id
                temp_child['name'] = row[2]
                temp_child['parent'] = parent_id
                data.append(temp_child)

    return node_id


def get_loc_no_children(node_id, parent_id):

    with open('permissions.csv', 'rb') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:

            temp_child = {}
            if (row[7] == 'e'):
                node_id += 1
                temp_child['id'] = node_id
                temp_child['name'] = row[2]
                temp_child['parent'] = parent_id
                data.append(temp_child)

    return node_id


def get_mic_no_children(node_id, parent_id):

    with open('permissions.csv', 'rb') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:

            temp_child = {}
            if (row[8] == 'e'):
                node_id += 1
                temp_child['id'] = node_id
                temp_child['name'] = row[2]
                temp_child['parent'] = parent_id
                data.append(temp_child)

    return node_id


def get_sms_no_children(node_id, parent_id):

    with open('permissions.csv', 'rb') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:

            temp_child = {}
            if (row[9] == 'e'):
                node_id += 1
                temp_child['id'] = node_id
                temp_child['name'] = row[2]
                temp_child['parent'] = parent_id
                data.append(temp_child)

    return node_id


def get_sto_no_children(node_id, parent_id):

    with open('permissions.csv', 'rb') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:

            temp_child = {}
            if (row[10] == 'e'):
                node_id += 1
                temp_child['id'] = node_id
                temp_child['name'] = row[2]
                temp_child['parent'] = parent_id
                data.append(temp_child)

    return node_id


def get_pho_no_children(node_id, parent_id):

    with open('permissions.csv', 'rb') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:

            temp_child = {}
            if (row[11] == 'e'):
                node_id += 1
                temp_child['id'] = node_id
                temp_child['name'] = row[2]
                temp_child['parent'] = parent_id
                data.append(temp_child)

    return node_id


#-------------------------------------------------------------------------------


if __name__ == '__main__':
    main()

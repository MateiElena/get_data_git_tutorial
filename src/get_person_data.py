"""Get person data"""
from sysconfig import get_path

DATA = {
    111: {
        "name": "Dan",
        "age": 20
    },
    112: {
        "name": "Maria",
        "age": 33
    },
}


def get_name_and_age(person_id):
    return DATA[person_id]

def save_data(file, person_data):
    """Save person data to file"""
    with open(file, "w") as fw:
        fw.write(person_data)


if __name__ == "__main__":
    try:
        person = get_name_and_age(112)
        print(person)
    except KeyError:
        print("Not a good user ID")
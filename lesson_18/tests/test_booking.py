def test_get_all_bookings(client):
    response = client.get_all_bookings()

    assert response.status_code == 200

def test_get_booking(client, booking_id):
    response = client.get_booking_by_id(booking_id)

    assert response.status_code == 200


def test_create_booking(client):
    response = client.create_booking()

    assert response.status_code == 200
    assert "bookingid" in response.json()


def test_patch_booking(client):
    booking = client.create_booking()
    booking_id = booking.json()["bookingid"]

    new_data = {
        "firstname": "Anna",
        "lastname": "Petrova"
    }

    response = client.patch_booking(booking_id, new_data)

    assert response.status_code == 200

    booking = client.get_booking_by_id(booking_id)

    assert booking.json()["firstname"] == "Anna"


def test_update_booking(client, booking_id):
    client.update_booking(booking_id)

    response = client.get_booking_by_id(booking_id)
    data = response.json()

    assert response.status_code == 200
    assert data["firstname"] == "Ivan"
    assert data["lastname"] == "Ivanov"
    assert data["totalprice"] == 111

def test_delete_booking(client, booking_id):
    client.delete_booking(booking_id)

    response = client.get_booking_by_id(booking_id)

    assert response.status_code == 201
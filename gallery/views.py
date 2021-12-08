from django.shortcuts import render

data = {
    "trucks": [
        {
            "id": 0,
            "name": "Caminhão de Frutas",
            "price": 25,
            "cargo_type": "Frutas",
            "cargo_limit": 24,
            "max_velocity": 200,
            "average_consumption": 23,
            "comfort_level": "Médio",
            "axle": 4,
            "image": "../static/images/nft_van.svg"
        },
        {
            "id": 1,
            "name": "Caminhão daora",
            "price": 25,
            "cargo_type": "Combustível",
            "cargo_limit": 24,
            "max_velocity": 200,
            "average_consumption": 23,
            "comfort_level": "Médio",
            "axle": 4,
            "image": "../static/images/nft_van.svg"
        },
        {
            "id": 2,
            "name": "Caminhão daora",
            "price": 25,
            "cargo_type": "Frutas",
            "cargo_limit": 24,
            "max_velocity": 200,
            "average_consumption": 23,
            "comfort_level": "Médio",
            "axle": 4,
            "image": "../static/images/nft_van.svg"
        },
        {
            "id": 3,
            "name": "Caminhão daora",
            "price": 25,
            "cargo_type": "Frutas",
            "cargo_limit": 24,
            "max_velocity": 200,
            "average_consumption": 23,
            "comfort_level": "Médio",
            "axle": 4,
            "image": "../static/images/nft_van.svg"
        },
        {
            "id": 4,
            "name": "Caminhão daora",
            "price": 25,
            "cargo_type": "Frutas",
            "cargo_limit": 24,
            "max_velocity": 200,
            "average_consumption": 23,
            "comfort_level": "Médio",
            "axle": 4,
            "image": "../static/images/nft_van.svg"
        },
    ]
}


def index(request):
    return render(request, 'gallery/index.html', data)


def nft_view(request, my_id):
    print(data["trucks"][my_id])
    return render(request, 'gallery/nft.html', data["trucks"][my_id])

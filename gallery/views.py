from django.shortcuts import render

data = {
    "trucks": [
        {
            "id": 0,
            "name": "Caminhão Toco",
            "price": 234,
            "cargo_type": "Caçamba",
            "cargo_limit": 15,
            "max_velocity": 80,
            "average_consumption": 2,
            "comfort_level": "Médio",
            "axle": 3,
            "image": "../static/images/nft_caminhao_cacamba.svg"
        },
        {
            "id": 1,
            "name": "Caminhão Baú",
            "price": 250,
            "cargo_type": "Secas",
            "cargo_limit": 24,
            "max_velocity": 80,
            "average_consumption": 3,
            "comfort_level": "Médio",
            "axle": 2,
            "image": "../static/images/nft_caminhao_bau.svg"
        },
        {
            "id": 2,
            "name": "Van",
            "price": 80,
            "cargo_type": "Expresso",
            "cargo_limit": 24,
            "max_velocity": 140,
            "average_consumption": 9,
            "comfort_level": "Médio",
            "axle": 2,
            "image": "../static/images/nft_van.svg"
        },
        {
            "id": 3,
            "name": "Carreta Articulavel",
            "price": 945,
            "cargo_type": "Granel",
            "cargo_limit": 28,
            "max_velocity": 80,
            "average_consumption": 1,
            "comfort_level": "Alto",
            "axle": 4,
            "image": "../static/images/nft_carreta_articulavel.svg"
        },
        {
            "id": 4,
            "name": "Carreta Tanque",
            "price": 674,
            "cargo_type": "Combustível",
            "cargo_limit": 24,
            "max_velocity": 80,
            "average_consumption": 2,
            "comfort_level": "Médio",
            "axle": 5,
            "image": "../static/images/nft_carreta_tanque.svg"
        },
        {
            "id": 5,
            "name": "Carreta Container",
            "price": 725,
            "cargo_type": "Secas",
            "cargo_limit": 28,
            "max_velocity": 90,
            "average_consumption": 23,
            "comfort_level": "Médio",
            "axle": 5,
            "image": "../static/images/nft_carreta_container.svg"
        },
        {
            "id": 6,
            "name": "Caminhão Baú Gold",
            "price": 575,
            "cargo_type": "Secas",
            "cargo_limit": 24,
            "max_velocity": 100,
            "average_consumption": 5,
            "comfort_level": "Alto",
            "axle": 4,
            "image": "../static/images/nft_caminhao_bau_gold.svg"
        },
        {
            "id": 7,
            "name": "Empilhadeira",
            "price": 575,
            "cargo_type": "Geral",
            "cargo_limit": 24,
            "max_velocity": 100,
            "average_consumption": 5,
            "comfort_level": "Alto",
            "axle": 4,
            "image": "../static/images/nft_empilhadeira.svg"
        },
        {
            "id": 8,
            "name": "Caminhão de frutas",
            "price": 575,
            "cargo_type": "Frutas",
            "cargo_limit": 24,
            "max_velocity": 100,
            "average_consumption": 5,
            "comfort_level": "Alto",
            "axle": 4,
            "image": "../static/images/nft_caminhao_fruta.svg"
        },
    ]
}


def index(request):
    return render(request, 'gallery/index.html', data)


def nft_view(request, my_id):
    print(data["trucks"][my_id])
    return render(request, 'gallery/nft.html', data["trucks"][my_id])

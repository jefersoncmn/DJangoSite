from django.shortcuts import render


data = {
    "trucks": [
        {"id": 0, "name": "Caminhão daora",
         "image": "../static/images/nft_van.svg"},
        {"id": 1, "name": "Caminhão grande",
         "image": "../static/images/nft_van.svg"},
        {"id": 2, "name": "Caminhão verde",
         "image": "..../assets/images/nft_van.svg"},
        {"id": 3, "name": "Caminhão grande",
         "image": "../static/images/nft_van.svg"},
        {"id": 4, "name": "Caminhão grande",
         "image": "../static/images/nft_van.svg"},
        {"id": 5, "name": "Caminhão grande",
         "image": "../static/images/nft_van.svg"},
        {"id": 6, "name": "Caminhão grande",
         "image": "../static/images/nft_van.svg"},
        {"id": 7, "name": "Caminhão grande",
         "image": "../static/images/nft_van.svg"},
        {"id": 8, "name": "Caminhão grande",
         "image": "../static/images/nft_van.svg"},
        {"id": 9, "name": "Caminhão grande",
         "image": "../static/images/nft_van.svg"},
    ]
}


def index(request):
    return render(request, 'gallery/index.html', data)


def nft_view(request, my_id):
    print(data["trucks"][my_id])
    return render(request, 'gallery/nft.html', data["trucks"][my_id])

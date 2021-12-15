from django.core.management.base import BaseCommand

from barber.models import Service, Product, Barber

LOREM_IPSUM = \
    '''Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's 
    standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make 
    a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, 
    remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing 
    Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions 
    of Lorem Ipsum. '''

service = [
    {'name': 'Hair Cut', 'description': LOREM_IPSUM, 'url': 'haircut', 'image': 'https://place-hold.it/100x60'},
    {'name': 'Beard Style', 'description': LOREM_IPSUM, 'url': 'beardstyle', 'image': 'https://place-hold.it/100x60'},
    {'name': 'Color & Wash', 'description': LOREM_IPSUM, 'url': 'colorandwash', 'image': 'https://place-hold.it/100x60'}
]

product = [
    {'name': 'Hair Cut', 'price': '9.99', 'image': 'https://place-hold.it/100x60', 'service': None},
    {'name': 'Hair Wash', 'price': '10.99', 'image': 'https://place-hold.it/100x60', 'service': None},
    {'name': 'Hair Color', 'price': '11.99', 'image': 'https://place-hold.it/100x60', 'service': None},
    {'name': 'Hair Shave', 'price': '12.99', 'image': 'https://place-hold.it/100x60', 'service': None},
    {'name': 'Hair Straight', 'price': '13.99', 'image': 'https://place-hold.it/100x60', 'service': None},
    {'name': 'Facial', 'price': '14.99', 'image': 'https://place-hold.it/100x60', 'service': None},
    {'name': 'Shampoo', 'price': '14.99', 'image': 'https://place-hold.it/100x60', 'service': None},
    {'name': 'Beard Trim', 'price': '16.99', 'image': 'https://place-hold.it/100x60', 'service': None},
    {'name': 'Beard Shave', 'price': '17.99', 'image': 'https://place-hold.it/100x60', 'service': None},
    {'name': 'Wedding Cut', 'price': '18.99', 'image': 'https://place-hold.it/100x60', 'service': None},
    {'name': 'Clean Up', 'price': '19.99', 'image': 'https://place-hold.it/100x60', 'service': None},
    {'name': 'Massage', 'price': '20.99', 'image': 'https://place-hold.it/100x60', 'service': None},
]

barber = [
    {'name': 'Adam Phillips', 'description': 'Adam Phillips', 'image': 'https://place-hold.it/100x60'},
    {'name': 'Dylan Adams', 'description': 'Hair Expert', 'image': 'https://place-hold.it/100x60'},
    {'name': 'Gloria Edwards', 'description': 'Beard Expert', 'image': 'https://place-hold.it/100x60'},
    {'name': 'Josh Dunn', 'description': 'Color Expert', 'image': 'https://place-hold.it/100x60'},
]


class Command(BaseCommand):

    help = 'Populating the database'

    def _populating_service(self, item_list=None):
        if isinstance(item_list, list) and item_list:
            count = 0
            for item in item_list:
                Service.objects.create(
                    name=item['name'],
                    description=item['description'],
                    url=item['url'],
                    image=item['image']
                )
                count += 1
            print(f'{count} "Service" objects have been added')

    def _populating_product(self, item_list=None):
        if isinstance(item_list, list) and item_list:
            count = 0
            for item in item_list:
                Product.objects.create(
                    name=item['name'],
                    price=item['price'],
                    image=item['image'],
                    service=item['service']
                )
                count += 1
            print(f'{count} "Product" objects have been added')

    def _populating_barber(self, item_list=None):
        if isinstance(item_list, list) and item_list:
            count = 0
            for item in item_list:
                Barber.objects.create(
                    name=item['name'],
                    description=item['description'],
                    image=item['image'],
                )
                count += 1
            print(f'{count} "Barber" objects have been added')

    def handle(self, *args, **options):
        self._populating_service(service)
        self._populating_product(product)
        self._populating_barber(barber)
from crm import create_app
from crm.models import Customer, Product, db


def create_test_customer():
    app = create_app()
    app.app_context().push()
    customer_1 = Customer(name='John', surname='Doe', email='john@email.com', phone='434-555-198')
    customer_2 = Customer(name='Peter', surname='Piper', email='peter@email.com', phone='123-868-108')
    customer_3 = Customer(name='Donald', surname='Peterson', email='donald@email.com', phone='112-812-912')
    customer_4 = Customer(name='Jacob', surname='Williams', email='jacob@email.com', phone='111-231-999')
    customer_5 = Customer(name='Daniel', surname='Brown', email='daniel@email.com', phone='812-325-141')

    db.session.add(customer_1)
    db.session.add(customer_2)
    db.session.add(customer_3)
    db.session.add(customer_4)
    db.session.add(customer_5)
    db.session.commit()


def create_test_product():
    app = create_app()
    app.app_context().push()
    product_1 = Product(name='Airpods Wireless Bluetooth Headphones', price=119.99,
                        description='Bluetooth technology lets you connect it with '
                                    'compatible devices wirelesses High-quality AAC audio offers immersive list')
    product_2 = Product(name='Cannon EOS 80D DSLR Camera', price=929.99,
                        description='Characterized by versatile imaging specs, the Canon EOS 80D further clarifies'
                                    ' itself using a pair of robust focusing systems and an intuitive design')
    product_3 = Product(name='iPhone 11 Pro 256GB Memory', price=699.99,
                        description='Introducing the iPhone 11 Pro. A transformative triple-camera system that adds '
                                    'tons of capability without complexity. An unprecedented leap in battery life')
    product_4 = Product(name='Sony Playstation 4 Pro White Version', price=399.99,
                        description='The ultimate home entertainment center starts with PlayStation. '
                                    'Whether you are into gaming, HD movies, television, music, brand')
    product_5 = Product(name='Amazon Echo Dot 3rd Generation', price=29.99,
                        description='Meet Echo Dot - Our most popular smart speaker with a fabric design. '
                                    'It is our most compact smart speaker that fits perfectly into small space')
    product_6 = Product(name='Logitech G-Series Gaming Mouse', price=49.99,
                        description='Get a better handle on your games with this Logitech LIGHTSYNC gaming mouse. '
                                    'The six programmable buttons allow customization for a smooth playing experience')

    db.session.add(product_1)
    db.session.add(product_2)
    db.session.add(product_3)
    db.session.add(product_4)
    db.session.add(product_5)
    db.session.add(product_6)
    db.session.commit()


def main():
    app = create_app()
    app.app_context().push()
    db.drop_all()
    db.create_all()
    create_test_customer()
    create_test_product()


if __name__ == '__main__':
    print('Populating database...')
    main()
    print('Successfully populated')

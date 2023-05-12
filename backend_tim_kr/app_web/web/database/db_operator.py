from .db_session import global_init, create_session
from .tables.user import User
from .tables.product import Product
from .tables.bucket import Bucket


class DBOperator:
    def __init__(self, db_host, db_port, db_login, db_password, logger):
        global_init(
            logger=logger,
            db_host=db_host,
            db_port=db_port,
            db_login=db_login,
            db_password=db_password,
        )
        self.logger = logger

    def registration(self, email, password) -> bool:
        session = create_session()
        some_user = session.query(User).filter(User.email == email).first()
        if some_user is not None:
            return False

        new_user = User(
            email=email,
            password=password,
            admin=False
        )
        session.add(new_user)
        session.commit()

        self.logger.debug("New user in DB")
        return True

    def auth(self, email, password) -> bool:
        session = create_session()
        some_user = session.query(User).filter(User.email == email, User.password == password).first()
        if some_user is not None:
            self.logger.debug("Success auth")
            return True
        return False

    def product(self):
        session = create_session()
        list_product = session.query(Product).all()
        response_json = {"product": []}
        for i in list_product:
            response_json['product'].append({
                "name": i.name,
                "price": i.price,
                "category": i.category,
                "namefile": i.namefile,
                "new": i.new,
                "sale": i.sale,
                "hit": i.hit
            })
        self.logger.debug("All product success")
        return response_json

    def product_with_id(self, product_id):
        session = create_session()
        list_product = session.query(Product).filter(Product.id == product_id).all()
        response_json = {"product": []}
        for i in list_product:
            response_json['product'].append({
                "name": i.name,
                "price": i.price,
                "category": i.category,
                "namefile": i.namefile,
                "new": i.new,
                "sale": i.sale,
                "hit": i.hit
            })
        self.logger.debug("ID product success")
        return response_json

    def product_with_category(self, product_category):
        session = create_session()
        list_product = session.query(Product).filter(Product.category == product_category).all()
        response_json = {"product": []}
        for i in list_product:
            response_json['product'].append({
                "name": i.name,
                "price": i.price,
                "category": i.category,
                "namefile": i.namefile,
                "new": i.new,
                "sale": i.sale,
                "hit": i.hit
            })
        self.logger.debug("Category product success")
        return response_json

    def product_with_hit(self):
        session = create_session()
        list_product = session.query(Product).filter(Product.hit == True).all()
        response_json = {"product": []}
        for i in list_product:
            response_json['product'].append({
                "name": i.name,
                "price": i.price,
                "category": i.category,
                "namefile": i.namefile,
                "new": i.new,
                "sale": i.sale,
                "hit": i.hit
            })
        self.logger.debug("Hit product success")
        return response_json

    def product_with_sale(self):
        session = create_session()
        list_product = session.query(Product).filter(Product.sale != 0).all()
        response_json = {"product": []}
        for i in list_product:
            response_json['product'].append({
                "name": i.name,
                "price": i.price,
                "category": i.category,
                "namefile": i.namefile,
                "new": i.new,
                "sale": i.sale,
                "hit": i.hit
            })
        self.logger.debug("Sale product success")
        return response_json

    def add_bucket(self, user_id, product_id):
        session = create_session()
        list_bucket = session.query(Bucket).filter(Bucket.user_id == user_id,
                                                   Bucket.product_id == product_id).first()
        if list_bucket is not None:
            list_bucket.count += 1
            session.commit()
        else:
            new_bucket = Bucket(
                user_id=user_id,
                product_id=product_id
            )
            session.add(new_bucket)
            session.commit()
        self.logger.debug("New bucket")

    def delete_bucket(self, user_id, product_id):
        session = create_session()
        list_bucket = session.query(Bucket).filter(Bucket.user_id == user_id,
                                                   Bucket.product_id == product_id).first()
        if list_bucket.count == 1:
            session.delete(list_bucket)
            session.commit()
        else:
            list_bucket.count -= 1
            session.commit()
        self.logger.debug("Delete bucket")

    def get_bucket(self, user_id):
        session = create_session()
        list_bucket = session.query(Bucket).filter(Bucket.user_id == user_id).all()
        response_json = {"bucket": []}
        for i in list_bucket:
            product = session.query(Product).filter(Product.id == i.product_id).first()
            response_json['bucket'].append({
                "name": product.name,
                "price": product.price,
                "category": product.category,
                "namefile": product.namefile,
                "new": product.new,
                "sale": product.sale,
                "hit": product.hit
            })
        self.logger.debug("Bucket success")
        return response_json
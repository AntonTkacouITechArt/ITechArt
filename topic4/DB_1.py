import psycopg2
from psycopg2 import Error


class SQLManager:
    def __init__(self, dbname, db_user, password, hostname):
        self.dbname = dbname
        self.user = db_user
        self.password = password
        self.host = hostname
        self.conn = None
        self.cur = None

    def __set_conn(self):
        try:
            self.conn = psycopg2.connect(user=self.user, password=self.password, host=self.host, database=self.dbname)
            print(f"Successfully connect to {self.dbname}")
        except (Exception, Error) as error:
            print("Error with work with PostgreSQL", error)

    def __set_cur(self):
        try:
            self.cur = self.conn.cursor()
            print(f"Successfully set cursor")
        except (Exception, Error) as error:
            print("Error with work with PostgreSQL", error)

    def __close_cur(self):
        try:
            self.cur.close()
        except (Exception, Error) as error:
            print("Error with work with PostgreSQL", error)

    def __close_conn(self):
        try:
            self.conn.close()
        except (Exception, Error) as error:
            print("Error with work with PostgreSQL", error)

    def __commit(self):
        try:
            self.conn.commit()
        except (Exception, Error) as error:
            print("Error with work with PostgreSQL", error)

    def connect_to_db(self):
        self.__set_conn()
        self.__set_cur()
        print("You successfully connect to DB")

    def disconnect_from_db(self):
        self.__close_cur()
        self.__close_conn()
        print("You successfully disconnect from DB")

    def create_table(self):
        try:
            self.cur.execute("""
                        CREATE TABLE IF NOT EXISTS Shops(
                            id SERIAL PRIMARY KEY,
                            name VARCHAR(100),
                            address TEXT NULL,
                            staff_amount INT CHECK (staff_amount > -1)
                        ); 
                        CREATE TABLE IF NOT EXISTS Departments(
                            id SERIAL PRIMARY KEY ,
                            sphere VARCHAR(100),
                            staff_amount INT CHECK (staff_amount > -1),
                            shop_id INT,
                            FOREIGN KEY (shop_id) REFERENCES Shops(id)
                        );
                        CREATE TABLE IF NOT EXISTS Items(
                            id SERIAL PRIMARY KEY,
                            name VARCHAR(100),
                            description TEXT NULL,
                            price DECIMAL(50,3),
                            department_id INT,
                            FOREIGN KEY (department_id) REFERENCES Departments(id)
                        );
                         """)
            self.__commit()
            print("You are successfully create tables")
        except (Exception, Error) as error:
            print("Error with work with PostgreSQL", error)

    def insert_data(self):
        self.cur.execute("""
            INSERT INTO Shops(name, address, staff_amount) VALUES (%s,%s,%s);
            """, ('Auchan', None, 250))
        self.cur.execute("""
            INSERT INTO Shops(name, address, staff_amount) VALUES (%s,%s,%s);
            """, ('IKEA', 'Street Žirnių g. 56, Vilnius, Lithuania.', 500))
        self.__commit()

        self.cur.execute("""
                INSERT INTO Departments(sphere, staff_amount, shop_id) VALUES (%s,%s,%s);
            """, ('Furniture', 250, 1))
        self.cur.execute("""
                INSERT INTO Departments(sphere, staff_amount, shop_id) VALUES (%s,%s,%s);
            """, ('Furniture', 300, 2))
        self.cur.execute("""
                INSERT INTO Departments(sphere, staff_amount, shop_id) VALUES (%s,%s,%s);
            """, ('Dishes', 200, 2))
        self.__commit()

        self.cur.execute("""
                INSERT INTO Items(name, description, price, department_id) VALUES (%s,%s,%s,%s);
            """, ('Table', 'Cheap wooden table', 300, 1))
        self.cur.execute("""
                INSERT INTO Items(name, description, price, department_id) VALUES (%s,%s,%s,%s);
            """, ('Table', None, 750, 2))
        self.cur.execute("""
                INSERT INTO Items(name, description, price, department_id) VALUES (%s,%s,%s,%s);
            """, ('Bed', 'Amazing wooden bed', 1200, 2))
        self.cur.execute("""
                INSERT INTO Items(name, description, price, department_id) VALUES (%s,%s,%s,%s);
            """, ('Cup', None, 10, 3))
        self.cur.execute("""
                INSERT INTO Items(name, description, price, department_id) VALUES (%s,%s,%s,%s);
            """, ('Plate', 'Glass plate', 20, 3))
        self.__commit()
        print("You are successfully insert data into Shops, Departments, Items")

    def drop_table(self):
        try:
            self.cur.execute("""DROP TABLE IF EXISTS Shops CASCADE ;""")
            self.cur.execute("""DROP TABLE IF EXISTS Departments CASCADE;""")
            self.cur.execute("""DROP TABLE IF EXISTS Items CASCADE;""")
            self.__commit()
            print("You are successfully drop tables")
        except (Exception, Error) as error:
            print("Error with work with PostgreSQL", error)

    def update_data(self):
        try:
            self.cur.execute("""
                UPDATE Items SET price = price + 100 WHERE name ~ '(^(B|b))|((E|e)$)'; 
            """)
            self.__commit()
        except (Exception, Error) as error:
            print("Error with work with PostgreSQL", error)

    def select_1(self):
        self.cur.execute("""
            SELECT * FROM Items
            WHERE description != NULL 
        """)


def select_menu():
    print("3.1) Все поля по товарам, у которых есть описание.")
    print("3.2) Все направления отделов, в которых более 200 сотрудников. Избегать повторений.")
    print("3.3) Все адреса магазинов с названием, начинающихся на английскую букву “i” без учета регистра.")
    print('3.4) Все названия товаров, которые продаются в отделах с мебелью (Furniture).')
    print("3.5) Названия магазинов, где в продаже есть товары с описанием.")
    print("3.6) Для каждого товара все его поля (кроме id) + все поля его отдела (кроме id), причем для всех полей "
          "отдела в ответе должна быть приписка department_{название_поля}, + все поля его магазина (кроме id) с "
          "припиской shop_{название_поля}.")
    print("3.7) Идентификаторы 3 - 4 по счету товаров из выборки, отсортированной по имени товара.")
    print("3.8) Названия товаров и названия их отделов, если и товар, и отдел существуют.")
    print("3.9) Названия товаров и названия их отделов. Если отдела не существует, то в его поле должен быть NULL.")
    print("3.10) Названия товаров и названия их отделов. Если в каком-то отделе нет товаров, то он должен попасть в "
          "ответ, а в колонке названия товара должен быть NULL.")
    print("3.11) Названия товаров и названия их отделов. Если отдел у товара не указан, то в его поле должен быть "
          "NULL. Если есть отдел без товаров - он должен появиться в ответе со значением NULL в колонке товара.")
    print("3.12) Все возможные сочетания названий товаров и названий отделов независимо от связей.")
    print("3.13) Количество товаров, сумму цен, максимальную цену, минимальную цену, среднюю цену для каждого "
          "магазина, где количество товаров больше одного.")
    print("3.14) Названия магазинов и массив названий всех товаров в них.")
    print("Выйти из меню select нажмите 0")


def switcher_menu(choice: int):
    if choice == 1:
        pass
    elif choice == 2:
        pass
    elif choice == 3:
        pass
    elif choice == 4:
        pass
    elif choice == 5:
        pass
    elif choice == 6:
        pass
    elif choice == 7:
        pass
    elif choice == 8:
        pass
    elif choice == 9:
        pass
    elif choice == 10:
        pass
    elif choice == 11:
        pass
    elif choice == 12:
        pass
    elif choice == 13:
        pass
    elif choice == 14:
        pass
    else:
        print("You input incorrect number, try again!")


sql1 = SQLManager(dbname="test", db_user="postgres", password="1111", hostname="127.0.0.1")
sql1.connect_to_db()
sql1.create_table()
sql1.insert_data()
while True:
    select_menu()
    try:
        choice = int(input("Input number > ..."))
        if choice == 0:
            break
        else:
            switcher_menu(choice)
    except Exception as error:
        print(f"{error}")

x = input('Pause press any key to continue ....')
sql1.update_data()
x = input('Pause press any key to continue ....')
sql1.drop_table()
sql1.disconnect_from_db()

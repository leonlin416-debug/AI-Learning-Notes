from abc import ABC,abstractmethod
import json

class Book:
    def __init__(self,book_id, title, author,total ):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.total = total
        self.__available = total

    def borrow_book(self):
        if self.__available >= 1:
            self.__available -= 1
            return True #借书成功
        return False    #结束失败

    def return_book(self):
        self.__available += 1

    def get__available(self):
        return self.__available


class Member(ABC): #抽象类不可以直接创建实例
    def __init__(self,card,name,password):
        self.card = card
        self.name = name
        self.password = password
        self.__borrowed_books = []

    def borrow_book(self,book:Book):
        if len(self.__borrowed_books) >= self.get_max_books() :
            print("您借阅的书籍数量已经达到上限！")
            return False    #直接截断不进行下面的操作

        if book.borrow_book():
            self.__borrowed_books.append(book)
            print(f"{self.name}借阅《{book.title}》成功")
            return True
        else:
            print("馆藏数量不足借阅失败")
            return False

    def return_book(self,book:Book):
        if book in self.__borrowed_books:
            book.return_book()
            self.__borrowed_books.remove(book)
            print(f"归还《{book.title}》成功")
        else:
            print(f"您没有借阅《{book.title}》,归还失败")

    def get_borrowed_books(self):
        return self.__borrowed_books

    @abstractmethod
    def get_max_books(self) -> int:
        pass

#普通会员
class NormalMember(Member):
    def get_max_books(self):
        return 3

#Vip会员
class VipMember(Member):
    def __init__(self,card,name,password,vip_level):
        super().__init__(card, name, password)
        self.vip_level = vip_level

    def get_max_books(self):
        return self.vip_level + 6

class LibrarySystem:
    def __init__(self):
        self.members = {}
        self.books = {}
        self.current_member: Member|None = None
        self.load_books_data()
        self.load_members_data()

    def load_members_data(self):
        with open("members.json", "r", encoding="utf-8") as f:
            menbers_data = json.load(f)
            for member in menbers_data:
                if member["卡号"].startswith("N"):
                    self.members[member['卡号']] = NormalMember(member['卡号'],member['姓名'],member['密码'])
                elif member["卡号"].startswith("V"):
                    self.members[member['卡号']] = VipMember(member['卡号'],member['姓名'],member['密码'],member['会员等级'])
        print("会员列表加载成功！")

    def load_books_data(self):
        with open("books.json","r",encoding="utf-8") as f:
            books_data = json.load(f)
            for book in books_data:
                self.books[book['book_id']]=Book(book['book_id'],book['title'],book['author'],book['total'])
        print("书籍列表加载成功！")


    def login(self):
        print('\n【登录】')
        while True:
            member_id = input('请输入会员卡号:')
            password = input('请输入密码:')
            if member_id in self.members:
                member = self.members[member_id]
                if self.members[member_id].password == password:
                    print(f'登陆成功!欢迎您,{member.name}')
                    self.current_member = member
                    return True
                else:
                    print('密码错误,请重新输入!')
                    continue
            else:
                print('用户不存在,请重新输入!')
                continue

    def borrow_book(self):
        #展示图书列表
        for book in self.books.values():
            print(f"编号:{book.book_id},标题:{book.title},作者:{book.author},总数:{book.total},可用:{book.get__available()}")
        #借书操作
        book_id = input("请输入要借的图书编号:")
        if book_id not in self.books:
            print("编号不存在,借阅失败")
            return
        self.current_member.borrow_book(self.books[book_id])
        #已经在member当中执行过borrow_book的操作了

    def return_book(self):
        borrowed_books  = self.current_member.get_borrowed_books()
        print("【已借阅的图书:】")
        for book in borrowed_books:
            print(f"编号:{book.book_id} 标题:{book.title}")
        while True:
            book_id = input("请输入要归还的图书编号:")
            if book_id not in self.books:
                print("编号不存在请重新输入")
            else:
                break
        self.current_member.return_book(self.books[book_id])

    def show_borrowed_books(self):
        borrowed_books = self.current_member.get_borrowed_books()
        for book in borrowed_books:
            print(f"编号:{book.id} 标题:{book.title}")

    def run(self):
        if self.login():
            while True:
                print("""MENU:
                1.借阅图书
                2.归还图书
                3.查看借阅
                4.退出系统
                """)
                choice = input("请选择操作(1-4):")
                match choice:
                    case "1":
                        self.borrow_book()
                    case "2":
                        self.return_book()
                    case "3":
                        self.show_borrowed_books()
                    case "4":
                        print("退出系统,bye")
                        break
                    case _:
                        print("无效的操作请重新输入！")
                        continue

if __name__ == '__main__':
    ls = LibrarySystem()
    ls.run()

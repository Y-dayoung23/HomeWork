class MemberStore:
    def __init__(self):
        self.members = {}
        self.next_id = 1

    def is_email_duplicate(self, email):
        return any(member['email'] == email for member in self.members.values())

    def add_member(self, name, email):
        if self.is_email_duplicate(email):
            return None, "중복된 이메일입니다."
        member_id = self.next_id
        self.members[member_id] = {'name': name, 'email': email}
        self.next_id += 1
        return member_id, "회원 등록 완료!"

    def member_exists(self, member_id):
        return member_id in self.members

    def update_member(self, member_id, name, email):
        if not self.member_exists(member_id):
            return "--해당 회원이 존재하지 않습니다.--"
        self.members[member_id] = {'name': name, 'email': email}
        return "회원 정보 수정 완료!"

    def delete_member(self, member_id):
        if not self.member_exists(member_id):
            return "--해당 회원이 존재하지 않습니다.--"
        del self.members[member_id]
        return "회원 삭제 완료!"

    def get_all_members(self):
        return self.members


def main():
    store = MemberStore()

    while True:
        print("\n메뉴를 선택하세요\n")
        print("1. 회원 등록")
        print("2. 회원 수정")
        print("3. 회원 삭제")
        print("4. 전체 회원 조회")
        print("0. 종료")

        choice = input("\n--> 번호 입력: ")

        if choice == "1":
            name = input("이름 : ")
            email = input("이메일 : ")
            member_id, message = store.add_member(name, email)
            if member_id:
                print(f"{message} (회원번호: {member_id})")
            else:
                print(message)

        elif choice == "2":
            try:
                member_id = int(input("수정할 회원번호: "))
                name = input("새 이름 : ")
                email = input("새 이메일 : ")
                result = store.update_member(member_id, name, email)
                print(result)
            except ValueError:
                print("회원번호는 숫자여야 합니다.")

        elif choice == "3":
            try:
                member_id = int(input("삭제할 회원번호 입력: "))
                result = store.delete_member(member_id)
                print(result)
            except ValueError:
                print("회원번호는 숫자여야 합니다.")

        elif choice == "4":
            members = store.get_all_members()
            if not members:
                print("--등록된 회원이 없습니다.--")
            else:
                for id, info in members.items():
                    print(f"회원번호: {id}, 이름: {info['name']}, 이메일: {info['email']}")

        elif choice == "0":
            print(">> 프로그램을 종료합니다.")
            break

        else:
            print("!!올바른 번호를 입력하세요.")

if __name__ == "__main__":
    main()

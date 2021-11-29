if __name__ == '__main__':
    email_address = input("Enter email address e.g (username@gmail.com): ")
    user_name , domain_name = email_address.split("@")
    print(f"Username: {user_name}\nDomainName: {domain_name}")
user_login = input('Ввідіть логін: ')
user_password = input('Ввідіть пароль: ')
user_name_only_letters = user_login.isalpha()
user_password_only_numbers = user_password.isalnum()
if user_name_only_letters and user_password_only_numbers:
    user_password_confirm = input('Підтвердити пароль: ')
    if user_password == user_password_confirm:
        print('Користувач залогінений')
        print('Користувач розлогінений через примхи викладача')

        user_login_2 = str(input('Ввідіть логін: '))
        user_password_2 = str(input('Ввідіть пароль: '))
        if user_login_2 == user_login and user_password_2 == user_password:
            print('Користувач залогінений')
        else:
            print('')
    else:
        print('Пароль не вірний')
else:
    print('Логін чи Пароль невірний')

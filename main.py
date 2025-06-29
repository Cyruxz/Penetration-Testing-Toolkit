import argparse
from modules import port_scanner, ftp_brute, ssh_brute, dir_brute, banner_grabber

parser = argparse.ArgumentParser(description="Penetration Testing Toolkit")
parser.add_argument("--mode", required=True, help="Mode: scan, ftp, ssh, dir, banner")
parser.add_argument("--target", help="Target IP or URL")
parser.add_argument("--user", help="Username for brute force")
parser.add_argument("--wordlist", help="Wordlist path")
parser.add_argument("--ports", help="Comma-separated ports", default="21,22,80,443")

args = parser.parse_args()

if args.mode == "scan":
    ports = [int(p) for p in args.ports.split(",")]
    port_scanner.scan_ports(args.target, ports)

elif args.mode == "ftp":
    ftp_brute.brute_force_ftp(args.target, args.user, args.wordlist)

elif args.mode == "ssh":
    ssh_brute.brute_force_ssh(args.target, args.user, args.wordlist)

elif args.mode == "dir":
    dir_brute.dir_brute(args.target, args.wordlist)

elif args.mode == "banner":
    ports = [int(p) for p in args.ports.split(",")]
    for port in ports:
        banner_grabber.grab_banner(args.target, port)

else:
    print("Invalid mode.")

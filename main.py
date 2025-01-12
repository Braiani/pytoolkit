import argparse
from ascii_splash import AsciiSplash
from Certificates import Certificates


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--terminal', '-T', action='store_true', help='Execute the program in terminal mode (no print ascii splash)')
    parser.add_argument('--hostname', '-H', type=str, help='The hostname to check the certificate for')
    args = parser.parse_args()

    if not args.terminal:
        AsciiSplash.print_main_ascii()
        if args.hostname:
            cert = Certificates(args.hostname)
            cert.get_certificate_details()
        while True:
            try:
                print()
                print("Please enter the following information:")
                hostname = input("Hostname to check certificate for: ")
                cert = Certificates(hostname)
                cert.get_certificate_details()
            except KeyboardInterrupt:
                AsciiSplash.print_exit_ascii()
                break
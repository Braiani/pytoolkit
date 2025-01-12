class AsciiSplash:

    def print_main_ascii():
        print(f"""
    >>==========================================================<<
    ||                                                          ||
    ||                                                          ||
    ||{TerminalColors.OKBLUE}     ______      _____              _  _   __ _  _        {TerminalColors.ENDC}||
    ||{TerminalColors.OKBLUE}     | ___ \    |_   _|            | || | / /(_)| |       {TerminalColors.ENDC}||
    ||{TerminalColors.OKBLUE}     | |_/ /_   _ | |  ___    ___  | || |/ /  _ | |_      {TerminalColors.ENDC}||
    ||{TerminalColors.OKBLUE}     |  __/| | | || | / _ \  / _ \ | ||    \ | || __|     {TerminalColors.ENDC}||
    ||{TerminalColors.OKBLUE}     | |   | |_| || || (_) || (_) || || |\  \| || |_      {TerminalColors.ENDC}||
    ||{TerminalColors.OKBLUE}     \_|    \__, |\_/ \___/  \___/ |_|\_| \_/|_| \__|     {TerminalColors.ENDC}||
    ||{TerminalColors.OKBLUE}             __/ |                                        {TerminalColors.ENDC}||
    ||{TerminalColors.OKBLUE}            |___/                                         {TerminalColors.ENDC}||
    ||                                                          ||
    ||                                                          ||
    >>==========================================================<<
        """)
        print("Welcome to the main program!")
        print("Please enter the following information:")
        
        print("Press Ctrl+C to exit the program.")
        print("\n")
    
    def print_exit_ascii():
        print(f"""
    >>==========================================================<<
    ||                                                          ||
    ||                                                          ||
    ||{TerminalColors.FAIL}     ______      _____              _  _   __ _  _        {TerminalColors.ENDC}||
    ||{TerminalColors.FAIL}     | ___ \    |_   _|            | || | / /(_)| |       {TerminalColors.ENDC}||
    ||{TerminalColors.FAIL}     | |_/ /_   _ | |  ___    ___  | || |/ /  _ | |_      {TerminalColors.ENDC}||
    ||{TerminalColors.FAIL}     |  __/| | | || | / _ \  / _ \ | ||    \ | || __|     {TerminalColors.ENDC}||
    ||{TerminalColors.FAIL}     | |   | |_| || || (_) || (_) || || |\  \| || |_      {TerminalColors.ENDC}||
    ||{TerminalColors.FAIL}     \_|    \__, |\_/ \___/  \___/ |_|\_| \_/|_| \__|     {TerminalColors.ENDC}||
    ||{TerminalColors.FAIL}             __/ |                                        {TerminalColors.ENDC}||
    ||{TerminalColors.FAIL}            |___/                                         {TerminalColors.ENDC}||
    ||                                                          ||
    ||                                                          ||
    >>==========================================================<<
        """)
        print("Goodbye!")
        print("\n")

class TerminalColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
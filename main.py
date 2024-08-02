import getpass
import sys
from zxcvbn import zxcvbn
import pprint


def test_single_password():
    """
    Prompts the user to enter a password and evaluates its strength.
    """
    password = getpass.getpass("[?] Enter your password: ")
    result = zxcvbn(password)
    display_result(result)


def test_multiple_passwords(password_file):
    """
    Evaluates the strength of multiple passwords from a specified file.

    Args:
        password_file (str): Path to the file containing passwords.
    """
    try:
        with open(password_file, 'r') as passwords:
            for password in passwords:
                password = password.strip()
                if password:
                    result = zxcvbn(password)
                    print('\n[+] ######################')  # for readability
                    display_result(result)
    except FileNotFoundError:
        print(f'[!] File not found: {password_file}')
    except Exception as e:
        print(f'[!] An error occurred: {e}')


def display_result(result):
    """
    Displays the results of the password strength evaluation.

    Args:
        result (dict): The result from zxcvbn evaluation.
    """
    print(f"Value: {result['password']}")
    print(f"Password Score: {result['score']}/4")
    print(f"Crack Time: {result['crack_times_display']['offline_slow_hashing_1e4_per_second']}")
    feedback = result['feedback']['suggestions']
    print(f"Feedback: {' '.join(feedback) if feedback else 'No suggestions'}")
    # pprint.pp(result)  # Uncomment this line for detailed output


def main():
    """
    Main function to handle user input and run the appropriate test.
    """
    if len(sys.argv) == 2:
        test_multiple_passwords(sys.argv[1])
    elif len(sys.argv) == 1:
        test_single_password()
    else:
        print('Usage:')
        print('  python test_password_strength.py <file>  (for a file containing passwords)')
        print('  python test_password_strength.py         (for a single password)')


if __name__ == "__main__":
    main()

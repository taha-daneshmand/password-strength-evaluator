# Password Strength Evaluator

![License](https://img.shields.io/github/license/taha-daneshmand/password-strength-evaluator)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Contributions](https://img.shields.io/badge/Contributions-Welcome-brightgreen)
![Zxcvbn](https://img.shields.io/badge/Zxcvbn-4.4.1-orange)

A command-line tool to evaluate the strength of passwords using the zxcvbn library.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
  - [Single Password Evaluation](#single-password-evaluation)
  - [Multiple Passwords Evaluation](#multiple-passwords-evaluation)
- [Example Output](#example-output)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The Password Strength Evaluator is a command-line tool that helps you assess the strength of passwords using the zxcvbn library. It provides useful feedback and suggestions to improve password security.

## Features

- **Single Password Evaluation:** Prompts the user to enter a password and evaluates its strength.
- **Multiple Passwords Evaluation:** Reads passwords from a specified file and evaluates the strength of each.
- **Detailed Feedback:** Provides feedback and suggestions to improve password strength.
- **Crack Time Estimates:** Displays estimated crack times for different attack scenarios.

## Installation

### Prerequisites

- Python 3.8 or higher
- zxcvbn 4.4.1

### Clone the Repository

```bash
git clone https://github.com/taha-daneshmand/password-strength-evaluator.git
cd password-strength-evaluator
```

### Install Dependencies

```bash
pip install zxcvbn
```

## Usage

### Single Password Evaluation

```bash
python test_password_strength.py
```

You will be prompted to enter a password for evaluation.

### Multiple Passwords Evaluation

```bash
python test_password_strength.py <file>
```

Replace `<file>` with the path to a file containing passwords (one per line).

## Example Output

### Single Password Evaluation

```
[?] Enter your password:
Value: yourpassword
Password Score: 3/4
Crack Time: 1 hour
Feedback: Add another word or two. Uncommon words are better.
```

### Multiple Passwords Evaluation

```
[?] python test_password_strength.py passwords.txt

[+] ######################
Value: password1
Password Score: 0/4
Crack Time: less than a second
Feedback: Use a few words, avoid common phrases.

[+] ######################
Value: Pa$$w0rd!
Password Score: 2/4
Crack Time: 1 minute
Feedback: Add another word or two. Uncommon words are better.
```

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a Pull Request.

Please make sure to update tests as appropriate.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

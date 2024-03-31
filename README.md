# GoLogin Profile Creator

This script creates multiple profiles using GoLogin, a tool for managing browser profiles. It iterates through a specified number of times, creating a new profile each time and saving information about the profile in a text file.

## Installation

1. Clone this repository:
2. Install the required dependencies:
3. Update the `token` variable in the script with your GoLogin authorization token.

## Usage

1. Run the script:
2. The script will create profiles based on the specified number of iterations and save profile information in text files.

## Script Overview

The script consists of the following components:

- Importing necessary modules: `time`, `GoLogin`, `requests`, `os`, `datetime`.
- Setting up variables such as `token`, `API_URL`, `PROFILES_URL`, and `response`.
- Initializing GoLogin with the provided token.
- Setting up iteration parameters: `num_iterations` and `path`.
- Creating a directory if it doesn't exist.
- Looping through iterations to create profiles and save profile information.

## Disclaimer

Please note that the use of this script may be subject to the terms and conditions of the services it interacts with. Ensure compliance with all applicable regulations and policies before use.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)



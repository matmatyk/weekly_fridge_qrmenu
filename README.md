# weekly\_fridge\_qrmenu
<!-- PROJECT SHIELDS -->
[![Contributors][contributors-shield]][contributors-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]
[![Telegram][telegram-shield]][telegram-url]

<!-- TABLE OF CONTENTS -->
## Table of Contents

- [weekly\_fridge\_qrmenu](#weeklyfridgeqrmenu)
  - [Table of Contents](#table-of-contents)
  - [About The Project](#about-the-project)
  - [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
  - [Usage](#usage)
    - [Example](#example)
  - [Roadmap](#roadmap)
  - [Contributing](#contributing)
  - [License](#license)
  - [Contact](#contact)

<!-- ABOUT THE PROJECT -->
## About The Project

![Printed lunch menu on the fridge][product-screenshot]

**TLDR;** put into [a text file][example_config] your lunch recipes for next few days and generate printable HTML file with QR codes which link directly to the recipes!

**Idea:** I came across this idea during social distancing phase of COVID-19 epidemic.
I decided to prepare a lunch menu for circa 10 – 14 days, print it and put on the fridge.
Additional plus of such planning is that very likely it will be enough to make a shopping just once per two weeks!

This Python module does exactly that. Generates HTML file with QR codes linking to recipes.

<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

This script is written in [Python 3](https://www.python.org/). Additionally you will need `pip3` to install dependencies.

### Installation

1. Clone the repo

   ```sh
   git clone https://github.com/matmatyk/weekly_fridge_qrmenu.git
   ```

2. Install required dependencies

   ```sh
   pip3 install -r requirements.txt
   ```

<!-- USAGE EXAMPLES -->
## Usage

Go to source directory and run as python module

```sh
python3 -m weekly_fridge_qrmenu path/to/menu_file.json
```

or shell script

```sh
./weekly_fridge_qrmenu.sh path/to/menu_file.json
```

In outcome you het an html file in `output` directory, which you can open using your web browser and print.

### Example

We will use here [exemplary input file.][example_config].

1. Run `./weekly_fridge_qrmenu.py example_input/menu.json`
2. Open the result file in your favourite browser, eg. `chromium output/menu_2020-04-28.html`
3. Print it horizontally on A4 paper:
   ![Printing generated HTML file](images/menu_printing.png)
4. Put on your fridge:
   ![Lunch menu on fridge](images/menu_on_fridge.png)

<!--_For more examples, please refer to the [Documentation](https://example.com)_-->

<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/matmatyk/weekly_fridge_qrmenu/issues) for a list of proposed features (and known issues).

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

<!-- CONTACT -->
## Contact

matmatyk - [@matmatyk](https://twitter.com/matmatyk)

Project Link: [https://github.com/matmatyk/weekly\_fridge\_qrmenu](https://github.com/matmatyk/weekly_fridge_qrmenu)

<!-- ACKNOWLEDGEMENTS -->
<!-- ## Acknowledgements

* []()
* []()
* []() -->

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/matmatyk/weekly_fridge_qrmenu.svg?style=flat-square
[contributors-url]: https://github.com/matmatyk/weekly_fridge_qrmenu/graphs/contributors
[stars-shield]: https://img.shields.io/github/stars/matmatyk/weekly_fridge_qrmenu.svg?style=flat-square
[stars-url]: https://github.com/matmatyk/weekly_fridge_qrmenu/stargazers
[issues-shield]: https://img.shields.io/github/issues/matmatyk/weekly_fridge_qrmenu.svg?style=flat-square
[issues-url]: https://github.com/matmatyk/weekly_fridge_qrmenu/issues
[license-shield]: https://img.shields.io/github/license/matmatyk/weekly_fridge_qrmenu.svg?style=flat-square
[license-url]: https://github.com/matmatyk/weekly_fridge_qrmenu/blob/master/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://pl.linkedin.com/in/michal-richter
[telegram-shield]: https://img.shields.io/badge/-Telegram-black.svg?style=flat-square&logo=telegram&color=555
[telegram-url]: https://t.me/matmatyk

[product-screenshot]: images/menu_main_photo.jpg
[example_config]: example_input/menu.json

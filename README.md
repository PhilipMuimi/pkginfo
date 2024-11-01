# pkginfo Python Script

This Python script, `pkginfo.py`, is a command-line utility inspired by the Unix `pkginfo` command. It is designed to read information about software packages from a specified file and perform various operations based on command-line options.

## Table of Contents
- [Features](#features)
- [Requirements](#requirements)
- [Usage](#usage)
  - [-a: List Installed Packages](#-a-list-installed-packages)
  - [-s: Show Total Size of Packages](#-s-show-total-size-of-packages)
  - [-l name: Show Specific Package Info](#-l-name-show-specific-package-info)
  - [-v: Display Author Information](#-v-display-author-information)
- [File Format](#file-format)
- [Example Commands](#example-commands)
- [Error Handling](#error-handling)

## Features

This script allows users to:
1. List the names of all installed packages.
2. Display the total size of all installed packages in kilobytes.
3. Show information about a specific package by name.
4. Display author information and assignment completion date.

## Requirements

- Python 3.x
- Ensure the argument file containing package data is in the correct format (see below).

## Usage

The script is run from the command line with the following syntax:

```bash
python pkginfo.py <option> <argument_file>

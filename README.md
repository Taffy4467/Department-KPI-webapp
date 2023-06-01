# Department-KPI-web app

## Overview
This project is a web application developed using Streamlit, MySQL, and various other modules. The application allows users from different departments in an organization to upload Excel files, analyze data, and visualize key performance indicators (KPIs) using interactive charts and graphs. The app allows for users in different locations in the same organization to have access to the data and can analyze it.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Database Configuration](#database-configuration)
- [File Structure](#file-structure)
- [Contributing](#contributing)
- [License](#license)

## Installation
To run this project locally, follow the steps below:

1. Clone the repository:
   ```shell
   git clone <repository_url>
   ```
   
2. Install the required dependencies:
   ```shell
   pip install -r requirements.txt
   ```

3. Set up the MySQL database:
   - Install MySQL server and create a new database.
   - Update the database connection details in the code (e.g., host, username, password, database name) to match your MySQL configuration.

4. Run the application:
   ```shell
   streamlit run main.py
   ```

## Usage
Once the application is running, follow these steps to use it:

1. Upload Excel File:
   - Click on the "Upload Data" button and select an Excel file (.xlsx) to upload.
   - The file will be saved in the "uploads" folder and added to the database.

2. Analyze Data:
   - The uploaded files will be displayed under the "Uploaded Files" section.
   - Select a file to analyze.
   - Choose a department from the dropdown menu.
   - Select a date range for the analysis.
   - Choose the desired KPIs (Key Performance Indicators) for visualization.
   - Click the "Submit" button.

3. View Data:
   - The filtered data will be displayed in a tabular form.
   - Download the filtered data as an Excel file using the "Download Excel File" link.

4. Visualize Data:
   - Select the desired graphs (Line Chart, Clustered Bar Chart, Stacked Bar Chart, Donut Chart, Sankey Chart) for visualization.
   - The selected graphs will be displayed based on the filtered data and chosen KPIs.

## Features
- File upload: Users can upload Excel files for analysis.
- Data filtering: Users can filter data based on department, date range, and selected KPIs.
- Tabular view: Filtered data is displayed in a tabular format.
- Excel download: Users can download the filtered data as an Excel file.
- Data visualization: Various interactive charts and graphs are available for data visualization.
- Graph download: Users can download individual graphs as HTML files.

## Technologies Used
- Streamlit: A Python framework for building interactive web applications.
- MySQL: A relational database management system for data storage and retrieval.
- Plotly Express: A data visualization library for creating interactive charts and graphs.
- Pandas: A data manipulation library for data analysis and manipulation.
- pymysql: A Python library for connecting to MySQL databases.
- numpy: A library for numerical computing in Python.
- base64: A library for encoding and decoding data in base64 format.
- io: A library for handling input and output operations.
- uuid: A library for generating universally unique identifiers.
- os: A library for interacting with the operating system.

## Database Configuration
To configure the MySQL database, follow these steps:

1. Install MySQL Server: Install MySQL server

 on your local machine or use a remote MySQL server.
2. Create a Database: Create a new database for the application.
3. Update Connection Details: In the code, update the MySQL connection details in the `myconn` variable (e.g., host, username, password, database name) to match your MySQL configuration.

## File Structure
The project's file structure is organized as follows:

```
- main.py              # Main application file
- requirements.txt    # List of dependencies
- uploads/            # Folder for storing uploaded files
- README.md           # Project documentation
```

## Contributing
Contributions to this project are welcome. If you encounter any issues or have suggestions for improvements, please feel free to submit a pull request or create an issue.

## License
This project is licensed under the [MIT License](LICENSE). You are free to modify, distribute, and use the code for personal or commercial purposes.


This README provides an outline of the project, its features, installation instructions, and other relevant details. Customize it further based on your specific project requirements, ensuring to provide clear instructions and highlight the technologies and functionalities that would impress a future employer.
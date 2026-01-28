# OUST Honours Eligibility System

A distributed systems application for determining student eligibility for honours enrollment at OUST (Oxford University of Science and Technology). The system evaluates student academic performance and calculates eligibility based on average scores.

## Project Overview

This is a client-server distributed system built with Python that:

- Verifies student information and validates user inputs
- Retrieves student grades from a SQL Server database
- Calculates overall grade averages and best 8 scores average
- Determines eligibility for honours enrollment

The project uses **Pyro4** for remote object communication between server and database interface components.

## Architecture

The system consists of three main components:

### 1. **Database Interface** (`InterfaceDb.py`)

- Manages connection to SQL Server database
- Exposes database query methods via Pyro4
- Handles student score retrieval
- Executes SQL queries safely with parameters

### 2. **Server** (`OUSTProjectServer1.py`)

- Central processing hub
- Communicates with database interface
- Calculates grade statistics:
  - Overall average score
  - Best 8 scores average
  - Honours eligibility determination
- Listens for client requests on port 51515

### 3. **Client** (`OUSTProjectClient.py`)

- User-facing interface
- Validates student input (ID, name, email, etc.)
- Sends requests to server
- Displays eligibility results

## Prerequisites

- Python 3.x
- SQL Server (MSSQL)
- SSMS (SQL Server Management Studio)

## Installation & Setup

### Step 1: Install Python Dependencies

```bash
pip install pyro4
pip install pyodbc
```

### Step 2: Setup Database

1. Open SQL Server Management Studio (SSMS)
2. Open the database file: `OUSTProject_database.sql`
3. Execute the SQL script to create the database and tables

### Step 3: Configure Database Interface

1. Open a terminal and navigate to the project folder
2. Run the database interface:
   ```bash
   python InterfaceDb.py
   ```
3. Enter your SQL Server name when prompted

### Step 4: Start the Server

1. Open a second terminal and navigate to the project folder
2. Run the server:
   ```bash
   python OUSTProjectServer1.py
   ```

### Step 5: Run the Client

1. Open a third terminal and navigate to the project folder
2. Run the client application:
   ```bash
   python OUSTProjectClient.py
   ```
3. Follow the on-screen prompts to enter student information

## Usage Example

Test the system with the sample student in the database:

- **Student ID:** 20241201
- **First Name:** jim
- **Last Name:** max
- **Email:** j.max@our.oust.edu.au

## Database Schema

The system uses SQL Server with the following structure:

- **Students Table:** Contains student ID, name, email information
- **Unit Table:** Contains Student_ID, Unit_Code, and Score information

## Project Structure

```
OUSTProject/
├── README.md                          # This file
├── OUSTProjectClient.py               # Client application
├── OUSTProjectServer1.py              # Server application
├── InterfaceDb.py                     # Database interface
├── ClientSocket.py                    # Client socket utilities
├── Server1Socket.py                   # Server socket utilities
├── OUSTProject_database.sql           # Database schema and initialization
├── Solution1.ssmssln                  # SQL Server solution file
└── READ ME.txt                        # Original instructions (deprecated)
```

## Key Features

- **Input Validation:** Validates student ID, name format, and email addresses
- **Grade Calculation:** Automatically calculates averages and identifies top 8 scores
- **Honours Eligibility:** Determines if student qualifies for honours program
- **Distributed Architecture:** Uses Pyro4 for remote communication between components
- **Error Handling:** Robust exception handling for database and network failures

## Configuration

### Server Settings

- **Default Port:** 51515
- **Default Server:** localhost

### Database Settings

- **Database Name:** OUSTProject
- **Connection Type:** Windows Authentication (Trusted Connection)

To change these settings, edit the configuration variables in:

- `InterfaceDb.py` - Database configuration
- `OUSTProjectServer1.py` - Server configuration
- `OUSTProjectClient.py` - Client configuration

## Troubleshooting

### Database Connection Issues

- Ensure SQL Server is running
- Verify the SQL Server name is correct in `InterfaceDb.py`
- Check that you have Windows Authentication enabled

### Pyro4 Connection Errors

- Ensure the database interface and server are running before starting the client
- Verify that port 51515 is not blocked by firewall
- Check that all three components are on the same network

### Student Not Found

- Verify the Student ID is correct
- Ensure the student record exists in the database
- Run the SQL initialization script to populate test data

## Future Enhancements

- Web-based user interface
- Support for multiple database engines
- Email notifications for eligibility results
- Admin dashboard for data management
- Enhanced security with authentication

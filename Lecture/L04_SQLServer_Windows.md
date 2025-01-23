# How to Install Microsoft SQL Server

This tutorial will guide you through the process of installing Microsoft SQL Server on a Windows machine. 

[Refernece](https://learn.microsoft.com/en-us/sql/sql-server/install/what-s-new-in-sql-server-installation?view=sql-server-ver16) 


## Prerequisites

Before you begin, ensure that your system meets the following requirements:

- A Windows 10 or later operating system.
- At least 6 GB of available disk space.
- Minimum 2 GB of RAM (4 GB recommended).

## Step 1: Download SQL Server

1. Go to the official Microsoft SQL Server download page:  
   [Download SQL Server](https://www.microsoft.com/en-us/sql-server/sql-server-downloads)
   
2. Select the edition you want to install. For most users, the **SQL Server 2022 Developer Edition** (free for development and testing) is a great option.
   
3. Click the **Download Now** button to begin the download.

## Step 2: Run the Installer

1. Once the download is complete, open the installer `.exe` file.

2. You will be presented with several installation options. Select **Basic** for a simple, guided installation process. This will install the default features and configurations.

3. The installer will check for any required prerequisites. If everything is in order, click **Install**.

   *Note:* The installation process may take several minutes depending on your system's performance.

## Step 3: Choose the Features to Install

1. If you selected **Custom** installation, you will be prompted to choose the features you want to install. You can leave the default features selected or customize based on your needs.

   Some common features include:
   - **SQL Server Database Engine**: For database management.
   - **SQL Server Management Studio (SSMS)**: GUI tool for managing your SQL Server.
   - **SQL Server Reporting Services**: For reports and analysis.
   - **SQL Server Integration Services**: For data migration tasks.

2. Select your desired features and click **Next**.

## Step 4: Configure SQL Server Instance

1. In the **Instance Configuration** step, you can either use the default instance name (`MSSQLSERVER`) or specify a custom name for your SQL Server instance.

2. Choose the **SQL Server Authentication** mode:
   - **Windows Authentication**: This uses your Windows login credentials.
   - **Mixed Mode**: Allows both SQL Server and Windows authentication.

3. If you select **Mixed Mode**, you’ll need to specify a password for the `sa` (System Administrator) account.

4. Select the appropriate **SQL Server administrators** (you can add Windows users/groups).

5. Click **Next**.

## Step 5: Install the Features

1. The installer will proceed with installing the selected features and configuring SQL Server based on your preferences.

2. You’ll be prompted to allow the installer to make changes to your system. Click **Yes** if prompted by User Account Control (UAC).

3. The installation process may take several minutes. Once finished, click **Next**.

## Step 6: Complete the Installation

1. When the installation is complete, the installer will display a **Summary** screen with the installation details.

2. Click **Next** and then **Close** to finish the installation process.

## Step 7: Install SQL Server Management Studio (SSMS)

1. SQL Server Management Studio (SSMS) is a tool that allows you to interact with SQL Server via a graphical user interface.

2. Download SSMS from the following link:  
   [Download SSMS](https://aka.ms/ssmsfullsetup)

3. Once downloaded, run the SSMS installer and follow the prompts to install it.

## Step 8: Connect to SQL Server

1. Open **SQL Server Management Studio (SSMS)**.

2. In the **Connect to Server** window, enter the following information:
   - **Server Name**: `localhost` (if using the default instance) or the name of your custom instance.
   - **Authentication**: Choose the authentication method you configured earlier (Windows Authentication or SQL Server Authentication).
   - If you selected SQL Server Authentication, enter the **username** and **password** for the `sa` account.

3. Click **Connect** to establish a connection to your SQL Server instance.

## Step 9: Test Your Installation

To verify that SQL Server is working correctly, run the following query in SSMS:

```sql
SELECT @@VERSION;

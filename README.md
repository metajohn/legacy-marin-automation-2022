# Legacy Excel & CMS Automation (2022)

## Project Overview
This repository contains a collection of Python scripts developed between 2019-2022 to automate the annual auditing and updating of the entirety of Marin Bikes' digital catalog across 15 synchronized CMS instances.

I taught myself Python after managing this process manually for several years; this was my first real coding project. 
Many mistakes were made. Some of the "bad coding" was intentional SEE BELOW.

The primary challenge was managing extremely high-latency server responses and inconsistent spreadsheet formatting.
The CMS was never designed with any ability for automation so it all had to be done manually. 
In the words of the backend developer, I automated this process by "DDOSing the server".
This is obviously a joke, and for complete accuracy, I was able to enter the data manually just as fast as the script given the incredibly high-latency (to say nothing of my APM).

These scripts were designed as a "manual state machine" to allow for granular control and easy recovery during long-running tasks.

## Key Features
* **Openpyxl Integration:** Automated data extraction and mapping from complex Excel workbooks.
* **Selenium Webdriver:** Navigated deeply nested XPaths to update product categories and specifications.
* **Telegram Bot Integration:** Implemented a real-time notification system to alert the user of script status or server timeouts.
* **Resilient Operational Logic:** Includes the original "OrderOfOperationsForNewYear.txt" and "Bike_Map_2022.txt" used to manage annual product rollouts for hundreds of items.

## Why This Approach?
The "loose" structure of these scripts (manually calling and commenting out functions) was a deliberate choice to handle a volatile environment:
1. **Resume-ability:** If a server timed out on a specific item, the script could be restarted from that exact point by simply moving comments without need for complex state management.
2. **Adaptability:** As XPaths or spreadsheet headers changed annually, the scripts could be updated in minutes rather than requiring a full system refactor.
3. **Efficiency:** Prioritized "Worse is Better" pragmatism to meet business deadlines in a high-latency ecosystem.

---
*Note: This code is preserved in its original 2022 state. Sensitive data, and API tokens have been redacted.*
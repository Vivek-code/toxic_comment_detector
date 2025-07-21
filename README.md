# Live Stream Chat Moderator 🛡️

![Python](https://img.shields.io/badge/Python-3.11+-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.36.0-orange?style=for-the-badge&logo=streamlit)
![Hugging Face](https://img.shields.io/badge/%F0%9F%A4% hugging%20face-Transformers-yellow?style=for-the-badge)

A multi-page web application designed to automatically detect and moderate toxic comments in real-time, helping to create a safer environment for live streamers and their communities.

---

## 📖 About The Project

Online live streaming platforms often struggle with toxic, offensive, or abusive comments in their chat feeds. Manual moderation is often impractical during high-traffic sessions. This project solves that problem by providing an automated moderation assistant.

It uses a sophisticated machine learning model (`unitary/toxic-bert`) to analyze chat messages and classify them across multiple toxicity categories. The results are stored in a database and visualized on a powerful analytics dashboard, giving moderators a high-level view of their community's health.

<br>

### ✨ Key Features

* **Multi-Page Interface:** A clean, organized application with separate pages for adding comments, live moderation, and overall analytics.
* **Real-Time Analysis:** A live dashboard allows for both manual one-by-one analysis and a "fire-and-forget" auto-analysis mode.
* **Database Storage:** Uses **SQLite** to persistently store all comments and their analysis results.
* **Powerful Analytics:** An interactive dashboard visualizes key metrics like overall toxicity rates, toxicity types, and trends over time on both daily and hourly scales.
* **User-Friendly Design:** A beautiful landing page with a custom background and clear instructions guides the user through the application.

<br>

### 🚀 Built With

* **Backend:** Python
* **Web Framework:** Streamlit
* **ML/NLP:** Hugging Face Transformers, PyTorch
* **Database:** SQLite3
* **Data Handling:** Pandas

---

## ⚙️ Getting Started

Follow these simple steps to get a local copy up and running.

### Prerequisites

* Python 3.8 or higher
* `pip` package manager

### Installation & Setup

1.  **Clone the Repository**
    ```sh
    git clone [https://github.com/Vivek-code/toxic-comment-detector.git](https://github.com/Vivek-code/toxic-comment-detector.git)
    cd toxic-comment-detector
    ```

2.  **Create and Activate a Virtual Environment**
    * This creates an isolated environment for your project's dependencies.
    ```sh
    python -m venv venv
    ```
    * **On Windows:**
    ```sh
    .\venv\Scripts\activate
    ```
    * **On macOS/Linux:**
    ```sh
    source venv/bin/activate
    ```

3.  **Install Required Packages**
    * This command reads the `requirements.txt` file and installs all necessary libraries.
    ```sh
    pip install -r requirements.txt
    ```

4.  **Run the Application**
    * Make sure you have deleted any old `chat_moderation.db` file to start fresh with the new database schema.
    ```sh
    streamlit run Moderator_Dashboard.py
    ```
    Your browser should automatically open with the application's welcome page!

---

## 🎮 Usage

Using the application is straightforward:

1.  **➕ Add Comments:** Navigate to the **'Add Comments'** page from the sidebar to add new comments to the moderation queue.
2.  **🛡️ Moderate Comments:** Go to the **'Moderator Dashboard'** to analyze comments from the queue one by one or start the auto-analysis feature.
3.  **📊 View Analytics:** Visit the **'Overall Analytics'** page to see a high-level view of all analyzed comments, including charts and trends.

---

## 📞 Contact

Have questions or feedback? Feel free to reach out!

* **Emails:**
    * `hfskksjfjsjfhk@gmail.com`
    * `djhsaadaksdbahs@gmail.com`
* **Phone:**
    * `+91 98981 65456`
    * `033 4565 8489`

Project Link: [https://github.com/Vivek-code](https://github.com/Vivek-code)

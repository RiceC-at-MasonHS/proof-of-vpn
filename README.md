# proof-of-vpn

A simple website designed to prove network membership, particularly useful when studying VPNs in cybersecurity contexts. It's built to look good in web browsers and provide a clear, terminal-friendly output for `cURL` requests.

## Features

-   **Browser-Friendly Display:** Presents a clean, modern web page displaying the network domain/IP address.
-   **cURL-Friendly Output:** Detects `cURL` requests and provides a concise, ASCII art-formatted text output of the server's IP address.
-   **Dynamic Network Information:**
    -   When hosted on GitHub Pages, the browser view automatically shows the `window.location.hostname`.
    -   When served by the included Python server, the browser view dynamically displays the server's local IP address using Jinja2 templating.
-   **GitHub Pages Deployment Ready:** Easily deployable as a static site on GitHub Pages.
-   **Local Hosting Server:** Includes a lightweight Python HTTP server for local hosting on devices like Raspberry Pis or VMs.

## Setup and Deployment

You have two main options for deploying and using this project:

### Option 1: Deploying to GitHub Pages (Static Hosting)

This option provides a publicly accessible version of your `proof-of-vpn` page, with the hostname derived from the GitHub Pages URL.

1.  **Create a Repository:**
    *   Create a new **public** GitHub repository (e.g., `proof-of-vpn`).
2.  **Push Code:**
    *   Push the `index.html` and `404.html` files to the `main` branch of your new repository.
3.  **Enable GitHub Pages:**
    *   Navigate to your repository's **Settings** tab on GitHub.
    *   In the sidebar, under "Code and automation", click **Pages**.
    *   Under "Build and deployment", for "Source", select **Deploy from a branch**.
    *   For "Branch", select `main` and `/ (root)`, then click **Save**.
4.  **Access Your Site:**
    *   After a few minutes, your site will be live at `https://<your-username>.github.io/<your-repository-name>`.

### Option 2: Local Hosting with Python Server (Dynamic IP & cURL Handling)

This option is ideal for self-hosting on a local machine, Raspberry Pi, or VM, providing dynamic IP address display and specialized `cURL` responses.

1.  **Prerequisites:**
    *   Python 3 installed.
    *   Jinja2 library: `pip install Jinja2`
2.  **Clone or Download:**
    *   Ensure you have `index.html`, `404.html`, and `server.py` in the same directory.
3.  **Run the Server:**
    *   Open your terminal in the project directory.
    *   Execute the command: `python server.py`
    *   The server will start on port `8000`.
4.  **Access and Test:**
    *   **Browser:** Open your web browser and go to `http://localhost:8000`. The page will display the server's local IP address.
    *   **cURL:** Open a *new* terminal and run `curl http://localhost:8000`. You will receive a terminal-friendly text output of the server's IP.

## Project Structure

```
.
├── LICENSE
├── README.md
├── index.html
├── 404.html
└── server.py
```
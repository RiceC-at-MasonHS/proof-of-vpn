# proof-of-vpn

A simple tool designed to prove network membership, particularly useful when studying VPNs and network routing in cybersecurity contexts. It's built to provide clear evidence of network proximity through both web browsers and terminal-friendly `cURL` requests.

## Features

-   **Automatic Network Classification:** Identifies if a connection is coming from a Local Network (RFC 1918), Loopback, or the Public Internet.
-   **Detailed Client/Server Reporting:** Displays critical network facts for verification and screenshots:
    -   **Server IP:** The internal IP address of the responding server.
    -   **Client IP:** The IP address the server sees for the visitor.
    -   **Host Header:** The exact address or hostname used to reach the server.
-   **Smart cURL Detection:** Provides a structured, ASCII-formatted report for CLI users, including a "Verdict" on the connection type.
-   **Modern Browser Interface:** A clean, responsive UI with an "Information Grid" designed for high-quality screenshots for lab submissions.
-   **Dual-Mode Compatibility:** 
    -   **Dynamic Mode:** Full features enabled when served by the included Python server.
    -   **Static Mode:** Gracefully falls back to basic hostname display when hosted on static services like GitHub Pages.

## Local Hosting with Python Server

This is the recommended way to use the project for lab environments (Raspberry Pis, VMs, or local machines).

1.  **Prerequisites:**
    *   Python 3 installed.
    *   Jinja2 library: `pip install Jinja2`
2.  **Clone or Download:**
    *   Ensure you have `index.html`, `404.html`, and `server.py` in the same directory.
3.  **Run the Server:**
    *   Open your terminal in the project directory.
    *   Execute: `python server.py`
    *   The server will start on port `8000`.
4.  **Access and Test:**
    *   **Browser:** Visit `http://<server-ip>:8000`.
    *   **cURL:** Run `curl http://<server-ip>:8000`.

## Project Structure

```
.
├── LICENSE
├── README.md
├── index.html
├── 404.html
└── server.py
```

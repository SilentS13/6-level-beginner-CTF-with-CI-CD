# Beginner Web Security CTF

Welcome to the **Beginner Web Security CTF**! This is a multi-level challenge designed to teach the fundamentals of web security in a fun and interactive way.

## How to Play

Each level is contained within its own folder. Start from `level-1` and work your way up!

### Prerequisites
- A modern web browser (Chrome, Firefox, Edge, etc.)
- Python 3 (for Level 6)

---

## Levels

### Level 1: The Hidden Path
*   **Topic:** HTML Comments & Source Code
*   **Task:** Find the flag hidden in the page's source code.
*   **Hint:** Right-click the page and select "View Page Source" or use `Ctrl+U`.

### Level 2: The Secret List
*   **Topic:** Information Disclosure (`robots.txt`)
*   **Task:** Find the secret directory hidden from web crawlers.
*   **Hint:** Every website has a `robots.txt` file. Try visiting `/robots.txt`.

### Level 3: The Cookie Jar
*   **Topic:** Cookie Manipulation
*   **Task:** Find the flag stored in your browser's cookies.
*   **Hint:** Open Developer Tools (`F12`), go to the **Application** or **Storage** tab, and look for "Cookies".

### Level 4: The Script Kiddie
*   **Topic:** Client-side Validation Bypass
*   **Task:** The button to get the flag is disabled. Find a way to click it.
*   **Hint:** Use the "Select Element" tool in DevTools to find the button and remove the `disabled` attribute from the HTML.

### Level 5: The Encoded Message
*   **Topic:** Data Encoding (Base64)
*   **Task:** Decode the message to reveal the flag.
*   **Hint:** The string ends with `==`. Search for a "Base64 Decoder" online.

### Level 6: The Command Room
*   **Topic:** Command Injection
*   **Task:** Execute a command on the server to read the `flag.txt` file.
*   **Setup:** 
    1. Navigate to `level-6/`
    2. Install requirements: `pip install -r requirements.txt`
    3. Run the app: `python app.py`
    4. Visit `http://localhost:5000`
*   **Hint:** Try chaining commands using `;` (Linux/Mac) or `&` (Windows). Example: `127.0.0.1; cat flag.txt`

---

## Team Members
*   **Member 1 (Lead)** - Vinnet Shinde
*   **Member 2** - Prathamkumar Kalidas Solanki
*   **Member 3** - Manush Patel
*   **Member 4** - Parth Patel
*   **Member 5** - Mahi Shah

---

## Solutions (Spoilers!)
1. `CTF{inspect_element_is_step_one}`
2. `CTF{robots_keep_secrets_too}`
3. `CTF{cookies_are_not_just_for_eating}`
4. `CTF{frontend_is_not_a_wall}`
5. `CTF{base64_is_everywhere}`
6. `CTF{the_final_command_executed}`

---

Good luck and happy hacking!

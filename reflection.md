# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

---

Bug 1 - The hints were backwards; when I was supposed to pick a higher number the game told me to go lower and vice versa
Bug 2 - The 'New Game' button does not work; even though the Secret changes in the developer debug info it stores the previous game state in other fields. The Attempts gets set to 0 as well and when you try to guess the new number it doesn't let you and says you must start a new game.
Bug 3 - The Hard mode is 1-50 and Normal mode is 1-100. These should be flipped. Also for Hard mode, even though it sets 1-50 you still get secret numbers outside of that range.

## 2. How did you use AI as a teammate? 

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

I used ChatGPT to figure out how to use the test suite and move the functions in app.py into logic_utils.py. I used Copilot as instructed for explaining what bugs existed in the initial game logic.

When I described Bug 1 to Copilot, it correctly told me how to swap the opposite hint messages in the code. It pointed out the relevant block of code and said 
    "The hint messages are reversed. When the guess is greater than the secret, the message should say "Go LOWER," and when the guess is less than the secret, it should say "Go HIGHER."

    Fix: Swap the messages in the check_guess function."
I verified the result by making the minor change in the code and testing it.

When I described how Hard mode chooses numbers that are outside of its 1-50 range, it was not helpful. All it said was to "ensure the new_game button respects the difficulty range when generating a new secret", which I think is too vague.


## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

- I decided whether a bug was really fixed by adding test cases to the test suite.
- I ran pytest after fixing Bug 1 to make sure the upper and lower guessing bounds were functioning properly.
- I asked AI to explain how to use the pytest test suite before altering anything. This gave me a better understanding of the architecture of my game.

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

Streamlit reruns the entire script every time the user interacts with the app. Because the script restarts each time, normal variables would reset on every interaction. Session state solves this possible problem by storing specific information to persist across reruns.

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

--- 

- One habit I want to reuse in my future work is building a test suite to use and build by increments.
- One thing I would do differently is read through all of the code I am given through more thoroughly before zoning in on specific problems.
- This project changed how I think about AI generated code by showing me that if you already have a good idea of what you want to fix and how you want to fix it, it can lead to AI being better equipped to help in a more structured fashion.